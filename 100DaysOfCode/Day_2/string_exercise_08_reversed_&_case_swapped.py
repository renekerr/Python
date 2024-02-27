"""
Strings Exercise 8 (Reversed and Case Swapped)

Write a function which accepts an input string and returns a reverse of the input string
while the case for every single character is reversed. The input string for this function
would be a sentence (words separated by spaces) consisting of alphabetic characters.
For example if:

input_string = "Hello Python World"
then the function should return a string such as:
"DLROw NOHTYp OLLEh"

"""

# Define Function
def reverse_swap_case(string):
    output_string = string[::-1].swapcase()
    return output_string


# Main Program
input_string = 'Hello Python World'
print(input_string)
fn = reverse_swap_case(input_string)

print(fn)


"""
################### Sample Solution ###################
def _reverse_string_sample_(sample_string):
    output = ""
    i = -1
    # iterate the list from end to the front
    while i != (- (len(sample_string) + 1)):
        output = output + sample_string[i].swapcase()
        i = i - 1
    return output
"""

