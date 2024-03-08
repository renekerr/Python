"""
Strings Exercise 1 (Palindrome Test)

Write a function that takes a string consisting of alphabetic characters as input argument and returns True
if the string is a palindrome. A palindrome is a string which is the same backward or forward.
Note that capitalization does not matter here i.e. a
lower case character can be considered the same as an upper case character.

"""

# Define Function
def palindrome_string(input_string):            # Version 1
    s = input_string.lower()
    length = len(s)
    reverse_string = ''
    is_palindrome = False

    for i in range(length-1, -1, -1):
        reverse_string = reverse_string + s[i]  # Invert string and compare with original
    if reverse_string == s:
        is_palindrome = True

    return is_palindrome



def palindrome_string_(input_string):           # Version 2. Simplified version

    if str(input_string).lower() == str(input_string)[::-1].lower():
        return True
    else:
        return False



# Main Program
input_string = 'hello'
x = palindrome_string(input_string)
y = palindrome_string_(input_string)
print(x)
print(y)




"""
################### Sample Solution ###################
def _is_palindrome_sample_(sample_string):
    # Check if the inverted string  equals the original string
    if str(sample_string).lower() == str(sample_string)[::-1].lower():
        return True     # Sample string is a palindrome
    else:
        return False    # Sample string is not a palindrome
"""