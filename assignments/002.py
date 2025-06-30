# Ask the user to input two numbers (use input()). Then:

# Add the two numbers together and print the result.
# Multiply the two numbers and print the result.
# Make sure to convert the inputs to numbers (use float() or int()) so you can do math with them!

num1 = (input("Enter the first number: "))
num2 = input("Enter the second number: ")
num1 = int(num1)
num2 = int(num2)
sum_result = num1 + num2
product_result = num1 * num2
print(f"The sum of {num1} and {num2} is: {sum_result}")
print(f"The product of {num1} and {num2} is: {product_result}")
