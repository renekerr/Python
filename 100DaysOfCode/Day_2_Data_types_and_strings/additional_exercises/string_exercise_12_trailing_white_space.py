"""
Strings Functions Exercise 2 (Trailing White Space)

Write a function that accepts an input string consisting of alphabetic characters and removes all the trailing
whitespace of the string and returns it without using any .strip() method. For example if:

input_string = "  Hello       "
then your function should return an output string such as:
output_string = "  Hello"
"""

# Define Function
def trailing_white_space(string):
    index = None
    k = len(string)
    while k > 0:

        if string[k-1] != " ":
            index = k
            break
        k = k - 1

    output_string = string[:index]
    return output_string


# Main Program
input_string = ' start  Hello     '
fn = trailing_white_space(input_string)

print(fn)

"""
################### Sample Solution ###################
def _remove_trailing_whitespace_sample_(string):
    my_index = None
    i = len(string)
    while i > 0:
        if string[i-1] != " ":
            my_index = i
            break
        i = i - 1
    # slice the string from 0 to that index
    new_string = string[:my_index]
    return new_string
"""