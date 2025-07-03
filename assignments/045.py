# Hollow Diamond Pattern

# Task: Print a hollow diamond pattern with 5 rows in the upper half (total 9 rows), where only the border is made of
#  stars.

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

row = 5
for i in range(1, 6):
    space = 5 - i
    if i == 1:
        print(" " * space + "*")
    else:
        bich_ko_space = 2 * i - 3
        print(" " * space + "*" + " " * bich_ko_space + "*")

for i in range(5, 0, -1):
    space = 5 - i
    if i == 1:
        print(" " * space + "*")
    else:
        bich_ko_space = 2 * i - 3
        print(" " * space + "*" + " " * bich_ko_space + "*")
