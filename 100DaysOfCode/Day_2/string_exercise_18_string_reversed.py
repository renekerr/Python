"""
Practice With Strings. Part 1
These two functions accept a string as input and returns the string reversed
"""


# Define Function Version 1
def reverse_string(s):                                   # Version 1
    output_string = ''

    for char in s:                                       # Go over characters of the  string (from the beginning to the end)
        output_string = char + output_string             # Append characters before the output string
                                                         # This will append it backwards
    return output_string


# Define Function Version 2
def reverse_string_(s):                                  # Version 2
    output_string = ''

    for k in range(len(s)-1, -1, -1):                    # Go over indexes of each character (from last index and back to the first)
        output_string = output_string + s[k]             #

    return output_string



# Main Program
input_string = input('Enter a string: ')
x = reverse_string(input_string)
y = reverse_string_(input_string)

print('ver1:    ', x)
print('ver2:    ', y)




