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

for i in range(1, 6):
    space = 5 - i
    stars = 2 * i - 1
    print(" " * space + "*" * stars)

for i in range(5, 0, -1):
    space = 5 - i
    stars = 2 * i - 1
    print(" " * space + "*" * stars)
