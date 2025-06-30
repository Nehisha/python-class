# Write a program that asks the user to enter a number between 1 and 10
# using a while loop. Keep asking until they enter a number in that range.
#  Once they do, print "Great choice!" and stop.

while True:
    user_input = int(input("Enter the number: "))
    if user_input > 0 and user_input <= 10:
        print("Great choice!")
        break
    else:
        print(f"That's not between 1 and 10! Try again: {user_input}")
