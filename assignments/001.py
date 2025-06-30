# # fruits = ["apple", "banana", "orange", "mango", "grape"]
# Create a list of your 5 favorite fruits (as strings, like "apple" or "banana"). Then:

# Print the entire list.
# Print the first and last fruit in the list.
# Add a new fruit to the list using the append() method and print the updated list.

fruits = ["apple", "banana", "orange", "mango", "grape"]
print(f"Fruits list: {fruits}")
print(f"First fruit:{fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
fruits.append("kiwi")
print(f"Updated fruits list: {fruits}")

fruits.insert(2, "pineapple")
fruits.remove("banana")
print(f"Final fruits list: {fruits}")
