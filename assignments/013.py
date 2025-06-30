# Palindrome Check
# Create a function is_palindrome that takes a string and returns
#  True if it is a palindrome (reads the same forwards and backwards),
#  False otherwise. Ignore case and non-alphabetic characters.


# def is_palindrome(user):
#     words = ""
#     for char in user:
#         if char.isalpha():
#             words += char.lower()
#     return words == words[::-1]


# user_input = input("Enter a string :")
# if is_palindrome(user_input):
#     print("Yes, It is palindrome.")
# else:
    # print("It is not palindrome")

def is_palindrome(user):
    words = ""
    for char in user:
        if char.isalpha():
            words += char.lower()
    return words == words[::-1]


user_input = input("Enter a string :")
if is_palindrome(user_input):
    print("Yes, It is palindrome.")
else:
    print("It is not palindrome")
