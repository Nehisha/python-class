# Inverted Right-Angle Triangle Pattern

# Task: Print an inverted right-angle triangle of stars with 5 rows.
# Example Output:
# *****
# ****
# ***
# **
# *

for i in range(5,0,-1):
    stars = "*" * i
    print(stars)