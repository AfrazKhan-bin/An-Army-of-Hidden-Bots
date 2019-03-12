import filecmp
import hashlib
import time
import socket, os, time, threading, sys
from queue import Queue
import server
import client as cl
from collections import Counter

Hash1 = 0
Hash3 = 0
Hash2 = 0
listOfPeers = []

with open('peers.txt','r') as f:
        listOfPeers = f.readlines()
        for index,each in enumerate(listOfPeers):
            listOfPeers[index] = each.splitlines()[0]

with open(('signatures.txt').encode(),'rb') as File:
            hash1 = hashlib.sha1()
            chunk = 0
            while chunk != b'':
                chunk = File.read(1024)
                hash1.update(chunk)
                Hash1 = hash1.hexdigest()

def compare(list1,list2):
    return Counter(list1) == Counter(list2)

while True:
    with open(('signatures.txt').encode(),'rb') as File:
            hash2 = hashlib.sha1()
            chunk2 = 0
            while chunk2 != b'':
                chunk2 = File.read(1024)
                hash2.update(chunk2)
                Hash2 = hash2.hexdigest()
            
            print("Matching Files")
            if Hash1 != Hash2:
                print ("Changed")
                print('updated')
                Hash1 = Hash2
                updated  = open('signatures.txt', 'r')
                Update = updated.readlines()
                
                i = 0
                j = 0
                updated.close()
                
                print (listOfPeers)
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
                    # print(cl.objSocket())
                    # cl.execute_command()
                    with open(('signatures.txt').encode(),'rb') as File:
                        hash3 = hashlib.sha1()
                        chunk3 = 0
                        while chunk3 != b'':
                            chunk3 = File.read(1024)
                            hash3.update(chunk3)
                            Hash3 = hash3.hexdigest()
                            Hash1 = Hash3   

            time.sleep(3)             


