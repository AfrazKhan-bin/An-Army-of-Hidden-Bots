import os, time
import Tkinter as tk
import tkMessageBox
import getpass

path_to_watch = "C://Users//"

root = tk.Tk()
root.withdraw()
username = getpass.getuser()

path_to_watch = path_to_watch + "//" + username + "//Downloads"

before = []  	#Initial representation of directory
after = []		#
for dirpath,dirnames,folder in os.walk(path_to_watch):
	for eachFile in folder:
		before.append(eachFile)

while 1:
	added = ""
	removed = ""
	time.sleep(5)
	for dirpath,dirnames,folder in os.walk(path_to_watch):
		for eachFile in folder:
			after.append(eachFile)

	# print(after)

	for f in after:
		if not f in before:
			# print (f)
			added =  added + f + ","

	for f in before:
		if not f in after:
			# print(f)
			removed = "" + f + ","

	if added:
		print ("Added: " + ", ".join (added))
		tkMessageBox.showinfo("Information","New File:" + added + " is added")

	if removed: 
		print ("Removed: " + ", ".join (removed))
		tkMessageBox.showinfo("Information","File:" + removed + " is deleted")

	before = after
	after = []



