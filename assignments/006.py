# Ask the user to input the current temperature (as a number). Then:

# If the temperature is above 30, print "It's hot! Wear sunglasses!"
# If the temperature is between 15 and 30 (inclusive), print "It's nice outside! Enjoy!"
# If the temperature is below 15, print "It's cold! Wear a jacket!"

user_input = int(input("Enter the current tempearture: "))
if user_input > 30:
    print("It's hot! Wear sunglasses!")
elif 15 <= user_input <= 30:
    print("It's nice outside! Enjoy!")
elif user_input < 15:
    print("It's cold! Wear a jacket!")
else:
    print("invalid input!!")
