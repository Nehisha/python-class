# Hollow Diamond Pattern

# Task: Print a hollow diamond pattern with 5 rows in the upper half (total 9 rows), where only the border is made of stars.
# Example Output:
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *

row = int(input("Enter how many rows: "))
for i in range(1, row + 1):
    space = " " * (row - i)
    if i == 1:
        print(space + "*")
    else:
        middle_space = " " * (2 * i - 3)
        print(space + "*" + middle_space + "*")

for i in range(row - 1, 0, -1):
    space = " " * (row - i)
    if i == 1:
        print(space + "*")
    else:
        middle_space = " " * (2 * i - 3)
        print(space + "*" + middle_space + "*")
