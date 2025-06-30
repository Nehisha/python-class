# Ask the user to input a number. Use an if statement to check if
# the number is even or odd, and print the result. (Hint: A number
#  is even if number % 2 == 0.)

user_input = int(input("Enter a number: "))
if user_input % 2 != 0:
    print("It is a odd number.")
else:
    print("It is a even number.")
