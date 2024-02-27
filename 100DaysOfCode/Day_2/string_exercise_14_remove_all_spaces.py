"""
Strings Functions Exercise 4 (Remove All Spaces)

Write a function which accepts an input string consisting of alphabetic characters and spaces and returns the string
with all the spaces removed. Do NOT use any string methods for this problem.

"""

# Define Function
def remove_spaces(s):
    output_string = ''

    for char in s:
        if char != ' ':
            output_string = output_string + char
    return output_string

# Main Program
input_string = ' This That These Those '
print(input_string, '\n')

fn = remove_spaces(input_string)
print(fn)


"""
################### Sample Solution ###################
def _remove_spaces_sample_(string):
    out_string = ""
    for x in range(0, len(string)):
        if string[x] != " ":
            out_string = out_string + string[x]
    return out_string
"""