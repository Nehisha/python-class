# Pascal’s Triangle Pattern
# Task: Print the first 5 rows of Pascal’s triangle using numbers.
# Example Output:
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
# Hint: Use the binomial coefficient formula or precompute values. Focus on spacing to align the numbers centrally.

row = 5
for i in range(1, 6):
    space = " " * (row - i)
    number = "1" * (2 * i - 1)
    print(space + number)
