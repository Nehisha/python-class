# Create a list of 5 nice compliments (like "You are awesome!" or "Great job!").
# Use the random module (specifically random.choice()) to pick one compliment
# randomly and print it.


import random


compliments = ["You are nice", "You are the best", "You are awesome", "You are great", "I love you"]
nice_compliments = random.choice(compliments)
print(nice_compliments)
