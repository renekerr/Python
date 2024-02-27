"""
Strings Functions Exercise 3 (Changing Cases)

Write a function which accepts an input string and returns a string where the case of the characters are changed, i.e. all the uppercase characters are changed to lower case and all the lower case characters are changed to upper case. The non-alphabetic characters should not be changed. Do NOT use the string methods upper(), lower(), or swap().
"""

# Define Function
def swap_string_case(s):
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    output_string = ''

    for char in s:
        if char in upper_case:
            x = upper_case.index(char)
            swap_case = lower_case[x]
            output_string = output_string + swap_case

        elif char in lower_case:
            x = lower_case.index(char)
            swap_case = upper_case[x]
            output_string = output_string + swap_case

        else:
            output_string = output_string + char

    return output_string

# Main Program
input_string = "Happy New Year 2016"
print(input_string,'\n')


fn = swap_string_case(input_string)

print(fn)



