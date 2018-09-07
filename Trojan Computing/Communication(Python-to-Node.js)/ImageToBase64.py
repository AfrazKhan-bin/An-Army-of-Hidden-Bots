from Naked.toolshed.shell import execute_js, muterun_js
import base64
import os
directory = os.getcwd()
with open(directory + "\\Capture.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())        
    
    encoded_string = str(encoded_string)

success = execute_js('main.js',encoded_string)