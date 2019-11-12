import os
import ctypes
import time

def cd(d):
    os.chdir(d)
    
cd("H:\\Desktop")

def set(name):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.getcwd() + "\\" + name, 3)

filename = input("Name of file on desktop: ")
if len(filename.split('.')) > 1:
    #you fool
    filename = filename.split('.')[0] #doesnt work if filename contains a `.` ex: "my.image.jpg"

try:
    allfiles = os.listdir()
    for file in allfiles:
        sep = file.split(".")
        if len(sep) == 2:
            if sep[0] == filename:
                set(file)
                raise KeyboardInterrupt("expected")
    raise Exception("Couldn't find file!")
except Exception as e:
    print(e)
    print("exiting in 5 seconds")
    time.sleep(5)
except KeyboardInterrupt:
    print("Set " + filename + "; exiting")
    
            
