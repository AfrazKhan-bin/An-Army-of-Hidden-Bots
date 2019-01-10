import socket
hostAddr = '10.5.30.15'
portNum = 5000
conn = ''

#socket object
s = socket.socket()

#creating socket with addr and port
s.bind((hostAddr,portNum))

#listen for connections at maximum
s.listen(5)
print("connection done . . . . .")


#browse files in any of the directories
def browse_file():
	conn.send("filebrowser")
	strDrives = conn.recv(1024)
	print(strDrives) 

	strDrive = raw_input("Enter the drive:")
	print (strDrive)
	conn.send(strDrive)

	message = conn.recv(1024)
	if message == "Invalid Directory":
		print ("Invalid Directory")
	else:
		print (message)	

	option = raw_input("Enter Y to open a file and N to exit")	
	if option == "Y":
		filename = raw_input("Enter the filename which you want to transfer")
		conn.send(filename)

	elif option=="N":
		exit()
	else:
		print ("Invalid Option")

#to transfer files from client to server 
def transfer_file():
	strFiles = conn.recv(1024)
	print (strFiles + "\n")

	filename = raw_input("Enter the name of the file--")
	conn.send(filename)
	message = conn.recv(1024)
	if message=="Invalid Filename":
		print ("Invalid File Name")
	else:
		filesize = int(message)
		message = raw_input("file size " + message + " bytes, Download (Y/N)?  ---")	
		conn.send(message)

		#receive file
		f = open("new_"+ filename , 'wb')
		Bytes = conn.recv(filesize)
		received = len(Bytes)
		f.write(Bytes)
		while received < filesize:
			Bytes = conn.recv(1024)
			received += len(Bytes)
			f.write(Bytes)
		print ("Download Compelete...")
 
def shutdown_restart():
	shutdowntype = raw_input("Do you want ot shutdown or restart (s/r) ?")
	conn.send(shutdowntype)  # get shutdown type


def receive_screenshot():
	message = raw_input("Download Image (Y/N)?--")
	conn.send(message)
	filesize = conn.recv(1024)
	filesize = int (filesize)

	#receive image
	f = open("new_Image.png" , 'wb')
	Bytes = conn.recv(filesize)
	received = len(Bytes)
	f.write(Bytes)
	print (received)
	while received < filesize:
		print (received)
		Bytes = conn.recv(1024)
		received += len(Bytes)
		f.write(Bytes)
	print ("Download Compelete...")

#keep listening for connections untill no error or exit
while True:
	conn , addr = s.accept()
	print ("Client with ip " + str(addr) + " has connected.")
	shutdown_restart()

s.close()



