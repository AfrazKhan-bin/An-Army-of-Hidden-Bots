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
            
            if Hash1 != Hash2:
                print('updated')
                Hash1 = Hash2
                updated  = open('signatures.txt', 'r')
                Update = updated.readlines()
                
                i = 0
                j = 0
                updated.close()
                
                server.create_threads()
                server.create_jobs()
            else:
                with open('listOfPeers.txt','r') as f:
                    listOfPeers = f.readlines()
                    for x in listOfPeers:
                        cl.strHost = str(x)
                        cl.connect_socket()
                        # time.sleep(1)
                        cl.execute_command()
                        # cl.objSocket.close()
    
    time.sleep(3)


