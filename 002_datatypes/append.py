user_input = input("Enter your name: ")

VOWEL_CHARACTERS = ["a", "e", "i", "o", "u"]

vowel_ko_list = []

for vowel in user_input:
    if vowel in VOWEL_CHARACTERS:
        vowel_ko_list.append(vowel)
print(vowel_ko_list)
