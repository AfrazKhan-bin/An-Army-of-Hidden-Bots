import hashlib
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox


def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()


def checkSignature(hashedString):
   with open('signatures.txt','r') as f:
      listOfSignatures = f.readlines()
      for index,each in enumerate(listOfSignatures):
          listOfSignatures[index] = each.splitlines()[0]
      listOfSignatures[-1] = listOfSignatures[-1].split('\t')[0]
      f.close()

      if hashedString in listOfSignatures:
         return True
      else:
         return False
# root = Tk()
# root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file, whose signature is to be saved . . .",filetypes = (("full files","*.*"),("all files","*.*")))
# message = hash_file(root.filename)
# f = open("signatures.txt","a+")
# f.write("\n"+message)
# f.close()
# messagebox.showinfo('Success',"Hash is saved, successfully")