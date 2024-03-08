"""
Strings Functions Exercise 1 (Leading White Space)

Write a function that accepts an input string consisting of alphabetic characters and removes all the leading whitespace
of the string and returns it without using .strip(). For example if:

input_string = "    Hello  "
then your function should return a string such as:
output_string = "Hello  "
"""

# Define Function
def leading_white_space(input_string):

    i = 0
    for k in range(0, len(input_string)):
        if input_string[k] != ' ':
            i = k
            break

    output_string = input_string[i::]
    return output_string

# Main Program
input_string = '        Hello all in one '
fn = leading_white_space(input_string)
print(fn)

