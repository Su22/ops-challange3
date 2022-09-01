#!/bin/bash

# Script: Ops 301 Class 03 Ops Challenge Solution
# Author: sujan thapa magar
# Date of latest revision: 8/31/2022
# Purpose: Navigates to directory input by user and changes files inside, then prints directory contents and permissions

# Main

# Prompts user for input directory path

echo " enter directory path:"

read path

# Prompts user for input permissions number

echo " input permissions number:"

read number

# Navigates to the directory input by the user and changes all files inside it to the input setting

chmod -R $number $path

ls -l . 

# End
