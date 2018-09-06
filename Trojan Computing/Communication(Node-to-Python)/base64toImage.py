import os
import base64
currentDirectory = os.getcwd()

#file with base64 string
base64File = os.path.join(currentDirectory + "\\base64.txt")

filename = "decoded.jpg"  #resultant image

#reading base64 string
with open(base64File, 'rb') as file:
	imageString = file.read()

#writing decoded string to image 
imageString = base64.b64decode(imageString)
with open(filename, 'wb') as f:
    f.write(variable)
