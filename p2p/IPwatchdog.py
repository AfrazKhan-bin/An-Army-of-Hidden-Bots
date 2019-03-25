import filecmp
import hashlib
import time
import socket, os, time, threading, sys
from queue import Queue
import IPserver
import IPclient as cl
from collections import Counter
import wmi

Hash1 = 0
Hash2 = 0
listOfPeers = []

def getListOfPeers():
    with open('peers.txt','r') as f:
        listOfPeers = f.readlines()
        # if (len(listOfPeers) == 0):
        #     sys.exit(0)
        for index,each in enumerate(listOfPeers):
            listOfPeers[index] = each.splitlines()[0]

        return listOfPeers


def computeHash():
    with open(('peers.txt').encode(),'rb') as File:
        hash1 = hashlib.sha1()
        chunk = 0
        while chunk != b'':
            chunk = File.read(1024)
            hash1.update(chunk)
            Hashed = hash1.hexdigest()
        File.close()
    return Hashed

Hash1 = computeHash()

def compare(list1,list2):
    return Counter(list1) == Counter(list2)

while True:
            Hash2 = computeHash()
            
            print("Matching Files")
            if Hash1 != Hash2:
                print ("Changed")
                print('updated')
                Hash1 = Hash2
                updated  = open('peers.txt', 'r')
                Update = updated.readlines()
                
                i = 0
                j = 0
                updated.close()
                
                # print (listOfPeers)
                while (not (compare(listOfPeers,server.updatedPeers))):
                    server.create_socket()
                    server.socket_bind()
                    print ("Accept socket now")
                    server.socket_accept()
                    print ("Socket Accepted")
                    print ("Going to send file")
                    server.main_menu()
                    print (server.updatedPeers)
                # global server.updatedPeers
                server.updatedPeers = []

                # server.refresh_connections()
                
                
            else:
                for x in listOfPeers:
                    cl.strHost = str(x)
                    cl.create_socket()
                    print ("Back here")

                    if (cl.fileChanged == 1):
                        Hash1 = computeHash()
                        cl.fileChanged = 0

            time.sleep(3)      
            listOfPeers =  getListOfPeers()     

