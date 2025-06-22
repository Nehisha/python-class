#1.Write a Python program to calculate the length of a string.

num = input("Enter a string: ")
length = len(num)
print(f"The length of {num} is: {length}")

#2. Replace first char occurrences with $.

user_input = input("Enter your word: ")
first_character = user_input[0]

word = first_character + user_input[1:].replace(first_character, "$")

print(word)
 
#3. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9


def lamo_word(words):
    lamo = words[0]
    for word in words:
        if len(word) > len(lamo):
            lamo = word
    return lamo, len(lamo)

words =["nehisha","software","engineering"]

lamo,len = lamo_word(words)
print(lamo)
print(len)

