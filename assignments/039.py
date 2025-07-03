# Centered Triangle (Pyramid) Pattern

# Task: Print a centered triangle of stars with 5 rows, using spaces to align the stars.
# Example Output:
#     *
#    ***
#   *****
#  *******
# *********


for i in range(1, 6):
    space = 5 - i
    stars = 2 * i - 1
    print(" " * space + "*" * stars)
