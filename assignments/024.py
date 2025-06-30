# Reverse All Strings
# Write a function reverse_all that takes a list of strings
# and returns a new list where each string is reversed.

def reverse_all(text):
    new_list = []
    for lists in text:
        new_list.append(lists[::-1])
    return new_list


print(reverse_all(["nehisha", "simran"]))
