# Longest Word Finder (Strings and Loops)
# Write a function longest_word(sentence)
#  that takes a sentence and returns the longest
#  word. If multiple words have the same maximum
#  length, return the first one. Use string methods
#  like split() and a loop. For example, longest_word("I love programming")
#  returns "programming".

def longest_word(sentence):
    longest_sentence = ""
    words = sentence.split()
    for word in words:
        if len(word) > len(longest_sentence):
            longest_sentence = word
    return longest_sentence


print(longest_word("I love programming"))
