import filecmp
import hashlib
import time
import socket, os, time, threading, sys
from queue import Queue
import server

Hash1 = 0

with open(('D:\drive\BS\Army of Hidden Bots ( FYP )\TSR\My virus\process List\signatures.txt').encode(),'rb') as File:
            hash1 = hashlib.sha1()
            chunk = 0
            while chunk != b'':
                chunk = File.read(1024)
                hash1.update(chunk)
                Hash1 = hash1.hexdigest()

while True:
    Hash2 = 0
    with open(('D:\drive\BS\Army of Hidden Bots ( FYP )\TSR\My virus\process List\signatures.txt').encode(),'rb') as File:
            hash2 = hashlib.sha1()
            chunk = 0
            while chunk != b'':
                chunk = File.read(1024)
                hash2.update(chunk)
                Hash2 = hash2.hexdigest()
            
            if Hash1 != Hash2:
                print('updated')
                Hash1 = Hash2
                updated  = open('D:\drive\BS\Army of Hidden Bots ( FYP )\TSR\My virus\process List\signatures.txt', 'r')
                previous = open('D:\\drive\\BS\Army of Hidden Bots ( FYP )\TSR\\My virus\\process List\\updated_sig\\signatures.txt','r')
                Update = updated.readlines()
                Previous = previous.readlines()
                
                i = 0
                j = 0
                updated.close()
                previous.close()
                
                server.create_threads()
                server.create_jobs()
            else:
                print('same')
    
    time.sleep(3)


