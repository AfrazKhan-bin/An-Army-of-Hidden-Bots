import wmi
import os
import time

c = wmi.WMI()
i = 0
for process in c.Win32_Process ():
    if (process.Name == 'UI.exe'):
        print('its found')
        result = process.Terminate()
        if(i == 0):

            os.system('start UI.exe')
            i+=1