# Hollow Right-Angle Triangle

# Task: Print a hollow right-angle triangle with 5 rows, where only the border is made of stars.
# Example Output:
# *
# **
# * *
# *  *
# *****

row = int(input("Enter how many rows: "))

for i in range(1, row + 1):
    if i == 1:
        print("*")
    elif i == row:
        print("*" * i)
    else:
        print("*" + " " * (i - 2) + "*")
