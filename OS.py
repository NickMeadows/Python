# -*- coding: utf-8 -*-

import os

#shutil is used for the 
import shutil

#fetch the current working directory
print(os.getcwd())

#start chrome
os.system('start chrome "www.youtube.com"')


#create a new directory
os.mkdir("New Directory")


#rename that directory
os.rename("New Directory", "Renamed Directory")


#remove the renamed directory too!
os.rmdir("Renamed Directory")