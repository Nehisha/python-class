1.

fruits = ["apple", "banana", "mango", "watermelon"]

for fruit in fruits:
    print(fruit)

for i in range(1, 6):
    print(i)

for i in range(0, 1000):
    print(f"{i + 1} Nehisha Hirachan")

2.

i = 0
while i < 1000:
    i += 1
    if i == 5:
        continue
    print(f"{i}. Swift Academy")
    if i == 100:
        break
3.


def calculator(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "/":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    else:
        return None


sum = calculator(1, "+", 3)
print(f"The sum is {sum}.")

diff = calculator(1, "-", 3)
print(f"The difference is {diff}.")

division = calculator(1, "/", 3)
print(f"The division is {division}.")

multi = calculator(1, "*", 3)
print(f"The multiplication is {multi}.")

4.

n = int(input("Enter a number: "))
number = 0

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")

