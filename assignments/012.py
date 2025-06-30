# Reverse a String
# Write a function reverse_string that takes a string as input and returns the string reversed.

user_input = input("Enter a string: ")
print(f"The reversed version of {user_input} is {user_input[::-1]}")
# : means “use the whole thing”
# -1 means “go backward”
# So [::-1] is just a shortcut to read a word backward.
