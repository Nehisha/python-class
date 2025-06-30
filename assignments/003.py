# Write a program that uses a for loop to print the numbers 1 to 10,
# and for each number, print that many stars (*). For example, for
# the number 3, print ***.
for i in range(1, 11):
    stars = '*' * i
    print(f"{i}: {stars}")
