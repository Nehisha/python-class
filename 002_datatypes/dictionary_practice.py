# 1.Write a Python script to add a key to a dictionary.

mero_dictionary = {"0": "10", "1": "20"}

mero_dictionary[2] = 30

print(mero_dictionary)
 # 2.Write a Python script to concatenate the following dictionaries to create a new one.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

new_dict = {}
new_dict.update(dic1)
new_dict.update(dic2)
new_dict.update(dic3)

print(new_dict)

# 3.Write a Python program to iterate over dictionaries using for loops.

my_dict = {'name': 'Nehisha', 'age': 19, 'city': 'Kathmandu'}

print("KEYS")
for key in my_dict:
    print(key)

print("\nVALUES")
for value in my_dict:
    print(value)

print("\nKEY VALUES")
for key, value in my_dict.items():
    print(f"{key}:{value}")
