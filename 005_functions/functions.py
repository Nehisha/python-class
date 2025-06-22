1.
def input_taker():
    num = int(input("Enter the number: "))
    sum = 0
    for i in range(1, num + 1):
        sum += i
    print(f"The sum of first {num} natural numbers is {sum}.")


input_taker()

while True:
    user_input = int(input("Enter the lucky number: "))
    number = 10

    if user_input == number:
        print("You have guessed the write number.")
    break


2. 

def perimeter_rectangle(l, b):
    return 2 * (l + b)


def area_rectangle(l, b):
    return l * b


print(perimeter_rectangle(2, 3))
print(area_rectangle(3, 4))


3.
def area_circle(radius, pi=3.14):
    circle = pi * (radius**2)
    print(f"The area of circle is: {circle}")


area_circle(2)


4.
def perimeter(l, b):
    return 2 * (l + b)
print(perimeter(1, 2))


