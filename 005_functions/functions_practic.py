# 1.Write a Python function to find the maximum of three numbers.

def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print(maximum(2, 9, 3))

# 2.Write a Python function to sum all the numbers in a list.


def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(sum_list([1, 2, 3, 4, 5]))

# 3.Write a Python function to multiply all the numbers in a list.


def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


print(multiply_list([1, 2, 3, 4, 5]))
