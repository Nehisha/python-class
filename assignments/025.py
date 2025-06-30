# Sum of Arguments
# Create a function sum_all that accepts any number of
# numeric arguments and returns their sum. Use *args
# for variable arguments.
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_all(2, 3))
print(sum_all(2, 3, 4))
print(sum_all(2, 3, 5, 6, 7))
print(sum_all())
