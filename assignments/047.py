# Zigzag Pattern
# Task: Print a zigzag pattern of stars across 5 rows, with stars forming a diagonal path.
# Example Output:
# *
#    *
# *
#    *
# *
# Hint: Use a condition to place a star based on the row and column indices, creating a diagonal or alternating pattern.

row = 5
for i in range(1, 6):
    if i % 2 != 0:
        print("*")
    else:
        print("  *")
