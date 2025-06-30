# Write a function print_details that takes three parameters: name, age, and city,
# and prints them in the format "Name: [name], Age: [age], City: [city]".
# Call this function using keyword arguments.

def print_details(name, age, city):
    return f"Name: {name} , Age: {age} , City: {city}"


print(print_details(name="Simran Sharma", age=20, city="Australia"))
