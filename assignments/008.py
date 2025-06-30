# Write a program that uses the os module to list all the files in the current folder (use os.listdir()).
# Print each file name on a new line.

import os
items = os.listdir()

for item in items:
    print(item)
