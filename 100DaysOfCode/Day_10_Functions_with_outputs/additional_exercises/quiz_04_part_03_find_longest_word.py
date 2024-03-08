'''
Quiz 4, Part 3 (Longest Word)
Write a function named find_longest_word that receives a string as parameter and returns the longest word in the string.
Assume that the input to this function is a string of words consisting of alphabetic characters that are separated
by space(s). In case of a tie between some words return the last one that occurs
'''

# Define Function
def find_longest_word(s):
    s = s.split()                           # Convert string into a list using split()
    longest_word = s[0]                     # Set first list element as the longest one
    max_length = len(s[0])                  # Set first list element's length as maximum length

    for elem in s:                          # Loop through elements in the list
        elem_length = len(elem)
        if elem_length  >= max_length:      # Compare length of each element with maximum set (max_length)
                                            # len(elem) >= max_length, in case of a tie, return 'last' longest word
                                            # len(elem) > max_length, in case of a tie, return 'first' longest word

            max_length = elem_length        # If True, set max_length to length of current element
            longest_word = elem             # And set as longest_word current element

    return longest_word                     # Return results

# Main Program
input_string = 'The lazy fox jumps over the crazy dog'
f = find_longest_word(input_string)
print('Longest word is',f)


'''
################### Instructor function ###################
def _longest_word_sample_(input_string):
    # Create a list of strings by splitting the original string
    splitted_string = input_string.split()
    # First arbitrarily set the maximum length
    # as the length of the first string
    maximum_length = len(splitted_string[0])
    # Also set the longest word as the first string
    longest_word = splitted_string[0]
    # Go through each string in the list we created
    # calculate the length of each string
    # check to see if its length is larger than maximum length
    # if so update it and return the string
    for string in splitted_string:
        # check the length of each string   # it resets for each string
        string_length = len(string)
        if string_length >= maximum_length:
            # maximum_length = string_length
            longest_word = string
    return longest_word
'''