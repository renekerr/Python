"""
Strings Exercise 4 (Count Input Character)

Write a function that accepts a string and a character as input and returns the number of times the character
is repeated in the string. Note that capitalization does not matter here i.e. a lower case character should be
treated the same as an upper case character.
"""

# Define Function
def count_input_character(input_string, character):

    count = 0
    input_string = input_string.lower()
    character = character.lower()

    for char in input_string:
        if char == character:
            count = count + 1

    return count


# Main Program
input_string = 'One day he would learn to fly'
character = 'O'
x = count_input_character(input_string, character)

print(x)

"""
def _count_character_sample_(input_string, input_character):

    # Instantiate a variable for counting
    my_count = 0

    # Iterate through each character in the given string
    # and check if the input character is equal to the
    # character in the string. If it does increase the
    # count by 1 and finally return the count

    for character in input_string.lower():
        if character == input_character.lower():
            my_count = my_count + 1
    return my_count
"""
