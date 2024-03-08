"""
Strings Exercise 5 (Count Words Starting With a Character)

Write a function that accepts a string and a character as input and returns the count
of all the words in the string which start with the given character. Assume that capitalization does not matter here.
You can assume that the input string is a sentence i.e. words are separated
by spaces and consists of alphabetic characters.
"""

# Define Function
def count_words_start_character(input_string, character):

    count = 0
    list_string = input_string.lower().split()          # Create a list from original string (lowercased)
    character = character.lower()                       # Lowercase character as well

    for items in list_string:                           # Loop over list
        first_char = items[0]
        if first_char == character:                     # Check/compare character with first_char
            count = count + 1                           # If True, count it


    return count                                        # Return result (count)

# Main Program
input_string = 'The dog quick brown fox dog jumps over the lazy dog'
character = 'D'

x = count_words_start_character(input_string, character)

print('There are',x, 'words which start(s) with character', character, '/', character.lower())




"""
################### Sample Solution ###################
def _count_words_given_character_sample_(input_string, template_character):
    # Create a list of strings by splitting the original string
    splitted_string = input_string.lower().split()
    template_character=template_character.lower()
    # Instantiate a variable for counting
    my_count = 0
    # Iterate through each string in the list that was produced
    # and check if the first character of each string is equal
    # to the template character. If it does increase the
    # count by 1 and finally return the count
    for string in splitted_string:
        if string[0] == template_character:
            my_count = my_count + 1
    return my_count
"""



