import os, time

path_to_watch = "C://Users//hassa/Downloads"


# for path,subdirs,files in os.walk(path_to_watch):
# 	for name in files:
# 		print (name)

# before = [f for f in os.listdir (path_to_watch)]
# print (before)


# while 1:
#   time.sleep (10)
#   after =  [f for f in os.listdir (path_to_watch)]
#   added = [f for f in after if f not in before]
#   removed = [f for f in before if f not in after]
#   if added: print ("Added: " + ", ".join (added))
#   if removed: print ("Removed: " + ", ".join (removed))
#   before = after


# files = []
# count = 1
# for (dirpath, dirnames, folder) in os.walk(path_to_watch):
#     for each in folder:
#     	files.append(each)

    	# print (str(count)  + "." + each )
    	# count +=1t


before = []  	#Initial representation of directory
after = []		#
for dirpath,dirnames,folder in os.walk(path_to_watch):
	for eachFile in folder:
		before.append(eachFile)

print (before)


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

	if removed: 
		print ("Removed: " + ", ".join (removed))

	before = after
	after = []	
	# if added:
	# 	print ("New files are added:" + "," .join(added))

	# if removed:
	# 	print ("Files deleted:"+ ",".join(removed))



