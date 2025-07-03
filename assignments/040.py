# Inverted Centered Triangle Pattern

# Task: Print an inverted centered triangle of stars with 5 rows.
# Example Output:
# *********
#  *******
#   *****
#    ***
#     *


for i in range(5, 0, -1):
    space = 5 - i
    stars = 2 * i - 1
    print(" " * space + "*" * stars)
