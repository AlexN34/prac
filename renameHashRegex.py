#filler text - fill in after regex chapter
import os
import shutil
import re

curDir = os.getcwd
for file in os.listdir('.'):
    # print (file) #gives file name inside this dir
    # print (os.path.realpath(file)) # gives path to file
    # regex = re.compile(r'(.*)\#(.*)')
    # matchObj = regex.findall(file)
    # print (re.sub(r'\#', '', file)) #sub replaces ALL unless count provided
    cleanedName = re.sub(r'\#', '', file)
    shutil.move(file, cleanedName)
