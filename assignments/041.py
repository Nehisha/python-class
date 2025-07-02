# Diamond Pattern

# Task: Print a diamond pattern of stars with 5 rows in the upper half (total 9 rows).
# Example Output:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

row = int(input("Enter how many rows: "))

for i in range(1, row + 1):
    spaces = " " * (row - i)
    stars = "*" * (2 * i - 1)
    print(f"{spaces + stars}")

for i in range(row):
    spaces = " " * i
    stars = "*" * (2 * (row - i) - 1)
    print(f"{spaces + stars}")
