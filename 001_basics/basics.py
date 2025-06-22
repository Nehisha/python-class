# Q1. Age Group Checker
# Write a program that takes the user's age as input.
# Then print whether the person is a:

# Child (age < 13)

# Teenager (13–19)

# Adult (20–59)

# Senior (60+)


# > Hint: Use input(), int(), and if-elif-else.

user_age = int(input("Enter your age: "))
if user_age < 13:
    print("Child")
elif 13 <= user_age <= 19:
    print("Teenager")
elif 20 <= user_age <= 59:
    print("Adult")
elif user_age > 60:
    print("Senior")
else:
    print("Invalid Input.")

# ---

# Q2. Number Operations
# Take two numbers from the user and display:

# Their sum

# Their difference

# Their product

# Whether the first number is divisible by the second


# > Hint: Use arithmetic and modulus % operator.

user_num1 = int(input("Enter the first number: "))
user_num2 = int(input("Enter the second number: "))
user_operator = input("Enter the operator: ")

if user_operator == "+":
    print(f"The sum is {user_num1 + user_num2}")
elif user_operator == "-":
    print(f"The difference is {user_num2 - user_num2}")
elif user_operator == "*":
    print(f"The multiplication is {user_num1 * user_num2}")
elif user_operator == "/":
    print(f"The reminder is {user_num1 % user_num2}")
else:
    print("Input is invalid.")


# ---

# Q3. Odd or Even with a Twist
# Take a number from the user. If it is even, print "Even number and its square is: " followed by its square.
# If it is odd, print "Odd number and its cube is: " followed by its cube.

# > Use if-else, ** operator.

user_input = int(input("Enter your number: "))

if user_input % 2 == 0:
    print(f"Even number and its square is: {user_input**2}")

else:
    print(f"Odd number and its cube is: {user_input**3}")


# ---

# Q4. Sum of N Natural Numbers
# Ask the user to enter a number n, and print the sum of the first n natural numbers using a loop.

# > Use a for loop and range().


numbers = int(input("Enter a number: "))
n = 0
for i in range(1, numbers + 1):
    n += i
print(f"The sum of first {numbers} natural number is: {n}")


# ---

# Q5. Multiplication Table Generator
# Ask the user to input a number. Print its multiplication table from 1 to 10.

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")

# #6.Write a Python program to print the following string in a specific format (see the output).
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# Output :

# Twinkle, twinkle, little star,
# 	How I wonder what you are!
# 		Up above the world so high,
# 		Like a diamond in the sky.
# Twinkle, twinkle, little star,
# 	How I wonder what you are

print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are!")
print("\t\tUp above the world so high,")
print("\t\tLike a diamond in the sky,")
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are!")

# 7.Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

import datetime

aile_ko_time = datetime.datetime.now()
print("Current date and time: ")
print(aile_ko_time.strftime("%Y-%M-%D %H:%M:%S"))

# 8. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

user_input = input("Enter your First name: ")
user_input1 = input("Enter your Last name: ")

print("Ulto nam: ")
print(f"{user_input1} {user_input}")

# 9.Write a Python program to find the median among three given numbers.

first_number = int(input("Enter 1st number: "))
second_number = int(input("Enter 2nd number: "))
third_number = int(input("Enter 3rd number: "))

if first_number < second_number < third_number or third_number < second_number < first_number:
    print(second_number)
elif second_number < first_number < third_number or third_number < first_number < second_number:
    print(first_number)
else:
    print(third_number)

# 10. Write a Python program that removes and prints every third number from a list of numbers until the list is empty

number = [1, 2, 3, 4, 5]

index = 0
while number:
    index = (index + 2) % len(number)
    removed = number.pop(index)
    print(f"Removed: {removed}")

#11. Write a Python program to find common divisors between two numbers in a given pair.

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
common = []

if a < b:
    small = a
else:
    small = b
for i in range(1, small + 1):
    if a % i == 0 and b % i == 0:
        common.append(i)

print(f"Common divisors: {common}")
