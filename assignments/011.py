# Write a program that simulates rolling a six-sided die. Use random.randint(1, 6)
# to pick a random number between 1 and 6. Ask the user how many times they want to
# roll the die, then print the result of each roll.

import random

user_input = int(input("How many time do you wan to roll the dice? : "))
for i in range(user_input):
    dice_roll = random.randint(1, 6)
    print(f"Roll {i + 1} : {dice_roll}")
