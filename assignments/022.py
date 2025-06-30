# Write a function capitalize_words that takes a sentence (a string)
# and returns a new sentence where the first letter of each word
# is capitalized.

def capitalize_words(text):
    words = text.split()
    # This cuts the sentence into small word pieces.So "hello mero nam" becomes ["hello", "mero", "nam"].

    capital = []

    for word in words:
        capital.append(word.capitalize())
#     "Go through each word, one by one.
# Make the first letter big using capitalize().
# Then put that nice new word in the basket."

    return " ".join(capital)
# Finally, this sticks all the words in the basket back together using spaces like glue!


print(capitalize_words("hello mero nam nehisha ho!"))
