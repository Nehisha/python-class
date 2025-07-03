# Hollow Right-Angle Triangle

# Task: Print a hollow right-angle triangle with 5 rows, where only the border is made of stars.
# Example Output:
# *
# **
# * *
# *  *
# *****


row = 5
for i in range(1, row + 1):
    if i == 1 or i == row:
        print("*" * i)
    else:
        space = i - 2
        print("*" + " " * space + "*")
