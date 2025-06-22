# 1.Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot be divided by 0.")

# 2.Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

user_input = input("Enter an integer: ")
try:
    number = int(user_input)
    print(f"You entered the integer: {number}")
except ValueError:
    msg = "Invalid input!"
    raise ValueError(msg)

# 3.Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

file_name = "example.txt"

try:
    with open(file_name, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: The file {file_name} not found.")
