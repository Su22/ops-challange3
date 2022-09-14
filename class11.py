#!/usr/bin/python3

# Script: Ops 301 Class 11 Ops Challenge Solution
# Author: sujan thapa magar             
# Date of latest revision: 13SEP2022      
# Purpose: Create a Python script that creates a new .txt file, appends three lines, prints to the screen the first line, then deletes the .txt file.

# Importing os module
import os

# Main
# Create a new text file
file_object = open('newtextfile.txt', 'w')
file_object.close()

# Prints out that newtextfile.txt has been created
print("newtextfile.txt has been created.\n")

# Opens text file with access mode append
file_object = open("newtextfile.txt", "a")

# Adds 3 new lines to the text file
file_object.write('Hello\nhow are you\nsee-you\n')
file_object.close()

# Opens the text file
file_object = open("newtextfile.txt", "r")

# Prints out thst newtextfile.txt has been appended
print("newtextfile.txt has been appended.\nHere is what your newtextfile.txt says:\n")
# Variable set for number of lines to read
num_of_lines = 3

# For loop that reads lines of variable num_of_lines
for i in range(num_of_lines):
    line = file_object.readline()
    print(line)

# Removes the text file
os.remove('newtextfile.txt')
print("newtextfile.txt has been removed.")

# End
