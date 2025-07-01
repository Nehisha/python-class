# Reverse Words in Sentence (Strings and Loops)
# Write a function reverse_words(sentence) that
#  takes a sentence and reverses the order of characters
#  in each word while keeping the word order intact.
#  For example, reverse_words("Hello World") returns "olleH dlroW".
#  Use string methods like split() and join() and a loop to reverse each word.

def reverse_words(sentence):

    reversed_bhako = []
    words = sentence.split()

    for letters in words:
        reversed_word = letters[::-1]
        reversed_bhako.append(reversed_word)
    return "___".join(reversed_bhako)


print(reverse_words("Hello World"))
