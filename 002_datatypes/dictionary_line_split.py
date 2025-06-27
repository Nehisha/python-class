user_ko_input = input("Enter your input: ")

words = user_ko_input.split()

counter_dictionary = {}

for word in words:
    if word in counter_dictionary:
        counter_dictionary[word] += 1
    else:
        counter_dictionary[word] = 1
print(counter_dictionary)


number = [1, 2, 3, 4, 5]

new_dict = {}

for n in number:
    if n % 2 == 0:
        new_dict[n] = "even"

    else:
        new_dict[n] = "odd"

print(new_dict)
