# Vowel Counter
# Write a function count_vowels that takes a string and returns
# the number of vowels (a, e, i, o, u, both lowercase and uppercase) in it.

def vowel_counts(vowel):
    vowel_characters = ["a", "e", "i", "o", "u"]
    count = 0
    for vowels in vowel:
        if vowels.lower() in vowel_characters:
            count += 1
    return count


print(vowel_counts("NEhisha"))
