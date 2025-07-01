# Number Pattern Generator (Loops and Conditionals)
# Write a function number_pattern(n) that prints a pattern of numbers up to n rows,
#  where each row contains numbers from 1 to the row number, but only prints
# odd numbers. For example, number_pattern(4) should print:

# 1
# 1 3
# 1 3 5
# 1 3 5 7

def number_pattern(n):
    for i in range(1, n + 1):
        num = 1
        count = 0

        while count < i:
            print(num, end="")
            num += 2
            count += 1
        print()


number_pattern(4)
