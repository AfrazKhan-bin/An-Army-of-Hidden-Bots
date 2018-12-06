import os, time
import Tkinter as tk
import tkMessageBox
import win32api
import getpass

path_to_watch = ""

root = tk.Tk()
root.withdraw()
username = getpass.getuser()
# path_to_watch = path_to_watch + "//" + username + "//Downloads"

addedDrives = ""

def monitorDirectory():

	before = []  	#Initial representation of directory
	after = []		#
	beforeDrives= []
	afterDrives = []

	for dirpath,dirnames,folder in os.walk(path_to_watch):
		for eachFile in folder:
			before.append(eachFile)

	while 1:
		if os.path.isdir(path_to_watch) == True:
			added = ""
			removed = ""
			time.sleep(5)
			for dirpath,dirnames,folder in os.walk(path_to_watch):
				for eachFile in folder:
					after.append(eachFile)

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
		else:
			break


Drives = win32api.GetLogicalDriveStrings()
beforeDrives = Drives.split('\000')[:-1]
while 1:
	time.sleep(3)
	Drives = win32api.GetLogicalDriveStrings()
	afterDrives = Drives.split('\000')[:-1]

	for f in afterDrives:
		if not f in beforeDrives:
			# print (f)
			addedDrives = f[0:2]
			path_to_watch = path_to_watch + addedDrives + "//"
			monitorDirectory()
			break

	beforeDrives = afterDrives
	afterDrives = []