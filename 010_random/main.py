import random

times = int(input("How many time do you want to roll dice?"))

for i in range(times):
   values = random.randint(1, 6)
   print(f"Values of the diced rolled {values}")
