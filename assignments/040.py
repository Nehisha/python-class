# Inverted Centered Triangle Pattern

# Task: Print an inverted centered triangle of stars with 5 rows.
# Example Output:
# *********
#  *******
#   *****
#    ***
#     *


row = int(input("Enter how many rows : "))
for i in range(row):
    spaces = " " * i
    star = "*" * (2 * (row - i) - 1)
    print(f"{spaces + star}")
