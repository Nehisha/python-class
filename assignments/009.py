# Ask the user to input a file name (like "myfile.txt").
# Use the os module (specifically os.path.exists()) to check
# if that file exists in the current folder. Print whether the file exists or not.

import os

user_input = input("Enter the file name: ")

if os.path.exists(user_input):
    print(f"{user_input} does exists.")
else:
    print(f"{user_input} does not exists")
