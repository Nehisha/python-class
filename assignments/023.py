# Create a function replace_substring that takes three
# strings: the original string, the substring to replace,
# and the replacement string. Return the modified string
# with all occurrences of the substring replaced.

def replace_substring(original, to_replace, replacement):
    return original.replace(to_replace, replacement)


print(replace_substring("cat", "cat", "dog"))
