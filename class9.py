#!usr/bin/python 3

# Script: Ops 301 Class 03 Ops Challenge Solution
# Author: sujan thapa magar
# Date of latest revision: September 9, 2022
# Purpose: This Python script utilizes a list 

# Assign to a variable a list of ten string elements
coding_languages = ["Java", "C++", "C" , "C#", "JavaScript" , "Python" , "R", "Kotlin", "Go", "Ruby"]
print("List of coding languages: ")
print(coding_languages)

# Print the fourth element of the list
print("\nPrint the fourth element of the list: ")
print(coding_languages[3])

# Print the sixth through tenth element of the list
print("\nPrint the sixth through tenth element of the list: ")
print(coding_languages[5:11])

# Change the value of the seventh element to "onion"
print("\nChange the value of the seventh element to 'onion'")
coding_languages[6] = "onion"
print(coding_languages)

# End 
