"""
Strings Exercise 9 (Preserve and Reverse)

Write a function that accepts a string of words separated by spaces consisting of
alphabetic characters and returns a string such that each word in the input string is reversed while the
order of the words in the input string is preserved. The length of the input string must be equal to the
length of the output string i.e. there should be no extra trailing or leading spaces in your output string.

For example if:

input_string   = “this is a sample test”
then the function should return a string such as:
"siht si a elpmas tset"
"""

# Define Function
def preserve_reverse(string):
    string = string.split()
    output_string = ''

    for word in string:
        word = word[::-1]
        output_string += word + ' '


    # Strip any white space
    output_string = output_string.strip()

    # Another way to strip white space
    """
    if output_string[-1] == ' ':
        output_string = output_string[0:-1]
    """

    return output_string

# Main Program
input_string = 'this is a sample test'
fn = preserve_reverse(input_string)
print(fn)


"""
################### Sample Solution ###################
def _preserve_and_reverse_sample_(string):

    splitted_list = string.split()

    for x in range(0, len(splitted_list)):
        splitted_list[x] = splitted_list[x][::-1]

    # Initialize an output string
    output_string = ""
    for x in range(0, len(splitted_list)):
        output_string += splitted_list[x] + " "

    # Strip any white spaces
    output_string = output_string.strip()
    return output_string
"""
