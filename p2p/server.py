import socket, os, time, threading, sys
from queue import Queue
import datetime

intThreads = 2
arrJobs = [1, 2]
queue = Queue()

updatedPeers = []
arrAddresses = []
arrConnections = []

strHost = socket.gethostbyname(socket.gethostname())
intPort = 5688

# function to return decoded utf-8
decode_utf8 = lambda data: data.decode("utf-8")

# function to return string with quotes removed
remove_quotes = lambda string: string.replace("\"", "")

# function to return title centered around string
center = lambda string, title: f"{{:^{len(string)}}}".format(title)


def create_socket():
    global objSocket
    # arrAddresses = []
    # arrConnections = []
    try:
        objSocket = socket.socket()
        objSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # reuse a socket even if its recently closed
    except socket.error() as strError:
        print("Error creating socket " + str(strError))


def socket_bind():
    global objSocket
    try:
        print("Listening on port " + str(intPort))
        objSocket.bind((strHost, intPort))
        objSocket.listen(20)
        print ("Listening Finished")
    except socket.error() as strError:
        print("Error binding socket " + str(strError) + " Retrying...")
        socket_bind()


def socket_accept():
    global blnFirstRun, arrAddresses
    try:
        conn, address = objSocket.accept()
        conn.setblocking(1)  # no timeout
        arrConnections.append(conn)  # append connection to array
        client_info = decode_utf8(conn.recv(1024)).split("`,")
        address += client_info[0], client_info[1], client_info[2],
        arrAddresses.append(address)
        if address[0] not in updatedPeers:
            updatedPeers.append(address[0])
            saveTransaction(address[0])
            
        print (updatedPeers)
        print("\n" + "Connection has been established: {0} ({1})".format(address[0], address[2]))
    except socket.error:
        print("Error accepting connections!")


def saveTransaction(address):
    currentDT = datetime.datetime.now()
    currentDT = str(currentDT)
    with open("Transactions.txt",'a+') as f:
        f.write("File sent to " + address + " at " + currentDT + "\n")
        f.close()

def main_menu():
    print ("In main menu")
    # while True:
    strChoice = "--i"
    strChoice = str(strChoice)
    # refresh_connections()  # refresh connection list

    if strChoice == "--i":
        print ("I am in main menu")
        send_commands()
    elif strChoice == "--x":
        close()
    else:
        print("Invalid choice, please try again!")
        sys.exit(0)


def close():
    global arrConnections, arrAddresses
    print (" in close connections at beginning")
    if len(arrAddresses) == 0:  # if there are no computers connected
        print("No any connection")
        return

    for intCounter, conn in enumerate(arrConnections):
        conn.send(str.encode("exit"))
        conn.close()
    del arrConnections; arrConnections = []
    del arrAddresses; arrAddresses = []

    print(arrConnections )
    print (" in close connections at the end")
    global objSocket
    objSocket.close()


def refresh_connections():  # used to remove any lost connections
    global arrConnections, arrAddresses
    for intCounter, conn in enumerate(arrConnections):
        try:
            conn.send(str.encode("test"))  # test to see if connection is active
            print ("I am in refresh exception 1")
            print(arrConnections)
            print (" in referesh Connections try part")
        except socket.error:
            print ("I am in refresh exception 2")
            del arrAddresses[intCounter]
            del arrConnections[intCounter]
            conn.close()
    print(arrConnections )
    print ("In refresh Connections at the end")


# def user_info():
#     print("IP: " + arrInfo[0])
#     print("PC Name: " + arrInfo[1])
#     print("OS: " + arrInfo[2])
#     print("User: " + arrInfo[3])


def send_file():
    print ("I am in send file")
    strFile = "signatures.txt"
    strOutputFile = "signatures.txt"
    global arrConnections,arrAddresses
    for conn in arrConnections:
        if not os.path.isfile(strFile):
            print("Invalid File!")
            return
        if strOutputFile == "":  # if the input is blank
            return
        conn.send(str.encode("send" + str(os.path.getsize(strFile))))

        objFile = open(strFile, "rb")  # send file contents and close the file
        time.sleep(1)
        conn.send(objFile.read())
        objFile.close()

        conn.send(str.encode(strOutputFile))
    print("Total bytes sent: " + str(os.path.getsize(strFile)))
    strClientResponse = decode_utf8(conn.recv(1024))
    print (strClientResponse)
    close()


def send_commands():
    # show_help()
    try:
        print ("I am in send Commands")
        send_file()
    except socket.error as e:  # if there is a socket error
        print("Error, connection was lost! :" + "\n" + str(e))
        return


def create_threads():
    for _ in range(intThreads):
        objThread = threading.Thread(target=work)
        objThread.daemon = True
        objThread.start()
    queue.join()


def work():  # do jobs in the queue
    while True:
        intValue = queue.get()
        if intValue == 1:
            create_socket()
            socket_bind()
            socket_accept()
        elif intValue == 2:
            while True:
                time.sleep(0.2)
                if len(arrAddresses) > 0:
                    main_menu()
                    break
        queue.task_done()
        queue.task_done()
        sys.exit(0)


def create_jobs():
    for intThread in arrJobs:
        queue.put(intThread)  # put thread id into list
    queue.join()