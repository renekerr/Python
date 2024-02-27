"""
Character Encoding Exercise 3 (Sum of Character Code Values)

Write a function that accepts an alphabetic string and returns an integer which is the sum of all the UTF-8 codes
of the character in that string. For example if the input string is "hello" then your function should return 532
"""

# Define Function
def sum_character_code_values(character):
    s = 0
    for i in character:
        s = s + ord(i)
    return s

# Main Program
string = input('Enter string : ')
fn = sum_character_code_values(string)

print(fn)

"""
################### Sample Solution ###################
def sum_of_ascii_codes_sample_(a):
    my_sum = 0
    for character in a:
        my_sum = my_sum + ord(character)
    return my_sum
"""
