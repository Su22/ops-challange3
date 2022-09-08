#!usr/bin/env python 3

# import libraries 
import os

# Script: Ops 301 Class 03 Ops Challenge Solution
# Author: sujan thapa magar
# Date of latest revision: 9/7/2022
# Purpose: This Python script generates directories,
# subdirectories, and files for user-provided directory path

# Read user input and assign to a variable
root = input("Enter root: ")
dirs = input("Enter dirs: ")
files = input("Enter files: ")

# file = input("Enter the filename: ")
# extension = file.split("/")
# print("The directory is : " + (extension[-1]))
# Declare function
# def generate_directory():
for(root, dirs, files) in os.walk("testdir"):
    print(root)
    print(dirs)
    print(files)


# Main
# Pass variable into function 

# End 
