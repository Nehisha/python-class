# Centered Triangle (Pyramid) Pattern

# Task: Print a centered triangle of stars with 5 rows, using spaces to align the stars.
# Example Output:
#     *
#    ***
#   *****
#  *******
# *********


row = int(input("Enter a number :"))
for i in range(1, row + 1):
    spaces = " " * (row - i)
    stars = "*" * (2 * i - 1)
    print(f"{spaces + stars}")
