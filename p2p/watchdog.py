import filecmp
import hashlib
import time
import socket, os, time, threading, sys
from queue import Queue
import server
import client as cl

Hash1 = 0
listOfPeers = []

with open(('signatures.txt').encode(),'rb') as File:
            hash1 = hashlib.sha1()
            chunk = 0
            while chunk != b'':
                chunk = File.read(1024)
                hash1.update(chunk)
                Hash1 = hash1.hexdigest()

while True:
    Hash2 = 0
    with open(('signatures.txt').encode(),'rb') as File:
            hash2 = hashlib.sha1()
            chunk = 0
            while chunk != b'':
                chunk = File.read(1024)
                hash2.update(chunk)
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
                
                server.create_socket()
                server.socket_bind()
                print ("Accept socket now")
                server.socket_accept()
                print ("Socket Accepted")
                print ("Going to send file")
                server.main_menu()
                server.refresh_connections()
            else:
                with open('listOfPeers.txt','r') as f:
                    listOfPeers = f.readlines()
                    for x in listOfPeers:
                        cl.strHost = str(x)
                        cl.create_socket()
                        print ("Back here")
                        # print(cl.objSocket())
                        # cl.execute_command()
                
                with open(('signatures.txt').encode(),'rb') as File:
                    hash1 = hashlib.sha1()
                    chunk = 0
                    while chunk != b'':
                        chunk = File.read(1024)
                        hash1.update(chunk)
                        Hash1 = hash1.hexdigest()
                        
    
    time.sleep(3)


