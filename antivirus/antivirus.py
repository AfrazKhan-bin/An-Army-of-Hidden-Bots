import wmi
import hashlib
from win10toast import ToastNotifier
import time



def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()


c = wmi.WMI()
while(True):

    for proc in c.Win32_Process():
        if proc.ExecutablePath is not None:
            msg = hash_file(proc.ExecutablePath.encode())
            with open("D:/drive/BS/Army of Hidden Bots ( FYP )/TSR/My virus/process List/signatures.txt",'r') as FileObj:
                for line in FileObj:
                    line=line.strip()
                    if (msg == line):
                        toaster = ToastNotifier()
                        toaster.show_toast("Army of Hidden Bots",
                    "Running virus is detected . . .",
                    icon_path="D:/drive/BS/Army of Hidden Bots ( FYP )/TSR/My virus/process List/logo.ico",
                    duration=2)
    time.sleep(2)
    