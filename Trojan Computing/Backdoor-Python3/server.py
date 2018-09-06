import socket
hostAddr = '192.168.43.44'
portNum = 5000
conn = ''

#socket object
s = socket.socket()

#creating socket with addr and port
s.bind((hostAddr,portNum))

#listen for connections at maximum
s.listen(5)


#browse files in any of the directories
def browse_file():
	conn.send(str.encode("filebrowser"))
	strDrives = str(conn.recv(1024),"utf-8")
	print(strDrives)

	strDrive = input("Enter the drive:")
	print (strDrive)
	conn.send(str.encode(strDrive))

	message = str(conn.recv(1024),"utf-8")
	if message == "Invalid Directory":
		print ("Invalid Directory")
	else:
		print (message)

	option = input("Enter Y to open a file and N to exit")
	if option == "Y":
		filename = input("Enter the filename which you want to transfer")
		conn.send(str.encode(filename))

	elif option=="N":
		exit()
	else:
		print ("Invalid Option")

def transfer_file():
	strFiles = str(conn.recv(1024),"utf-8")
	print (strFiles + "\n")

	filename = input("Enter the name of the file--")
	conn.send(str.encode(filename))
	message = str(conn.recv(1024),"utf-8")
	if message=="Invalid Filename":
		print ("Invalid File Name")
	else:
		filesize = int(message)
		message = input("file size " + message + " bytes, Download (Y/N)?  ---")
		conn.send(str.encode(message))

		#receive file
		f = open("new_"+ filename , 'w')
		Bytes = str(conn.recv(filesize),"utf-8")
		received = len(Bytes)
		f.write(Bytes)
		while received < filesize:
			Bytes = str(conn.recv(1024),"utf-8")
			received += len(Bytes)
			f.write(Bytes)
		print ("Download Compelete...")		

#keep listening for connections untill no error or exit
while True:
	conn , addr = s.accept()
	print ("Client with ip " + str(addr) + " has connected.")
	transfer_file()		