"""
Strings Functions Exercise 3 (Changing Cases)

Write a function which accepts an input string and returns a string where the case of the characters are changed, i.e. all the uppercase characters are changed to lower case and all the lower case characters are changed to upper case. The non-alphabetic characters should not be changed. Do NOT use the string methods upper(), lower(), or swap().
"""

################### Sample Solution ###################


# Define Function
def swap_case(s):
    output_string =''

    for char in s:
        n = ord(char)                               # Determine ordinal value of character

        if 90 >= n >= 65:                           # Characters in uppercase A-Z
            x = chr(n+32)                           # Convert to lowercase
            output_string = output_string + x       # Add to new string

        elif 122 >= n >= 97:                        # Character in lowercase  a-z
            x = chr(n-32)                           # Convert to uppercase
            output_string = output_string + x       # Add to new string

        else:                                       # Other characters
            output_string = output_string + char    # Add to new string

    return output_string

# Main Program
input_string = 'Happy New Year [2016]'
print(input_string)
fn = swap_case(input_string)

print(fn)