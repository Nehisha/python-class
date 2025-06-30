# Double List Elements
# Write a function double_list that takes a list of
# numbers and returns a new list where each element
# is doubled. Use a loop instead of map().

def double_list(number_haru):
    doubled_numbers = []

    for numbers in number_haru:
        doubled_numbers.append(numbers**2)
    return doubled_numbers


print(double_list([1, 2, 3, 4, 5]))
