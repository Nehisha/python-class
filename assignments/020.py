# Filter Even Numbers
# Write a function get_evens that takes a list of numbers
# and returns a new list containing only the even numbers.
# Use a loop instead of filter().

def get_evens(numbers):
    even = []
    for number_haru in numbers:
        if number_haru % 2 == 0:
            even.append(number_haru)
    return even


print(get_evens([1, 2, 3, 4, 5, 6, 7, 8]))
