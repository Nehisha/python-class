1.
user_age = int(input("Enter your Age: "))

if (user_age >= 18):
    print("the user is eligible.")
else:
    print("The user is not eligible.")

2.
number = int(input("Enter a number: "))

if (number == 0):
    print(f"{number}")
elif (number % 2 == 0):
    print(f"{number} is a even number.")
else:
    print(f"{number} is a odd number.")

3.
user_number = int(input("Enter your Number: "))
if user_number % 7 == 0 and user_number % 5 == 0:
    print(f"{user_number} is divisible by 7 and 5.")
elif user_number % 5 == 0:
    print("Divisivle by 5.")
elif user_number % 7 == 0:
    print("Divisible by 7.")
else:
    print("Not Divisble.")

4.
user_number1 = int(input("Enter First number: "))
user_operator = input("Enter the operator: ")
user_number2 = int(input("Enter Second number: "))

if user_operator == "+":
    print(user_number1 + user_number2)

elif user_operator == "-":
    print(user_number1 - user_number2)

elif user_operator == "*":
    print(user_number1 * user_number2)
elif user_operator == "%":
    print(user_number1 % user_number2)
else:
    print("Invalid.")
