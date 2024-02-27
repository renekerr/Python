"""
Strings Exercise 6 (Count Words of a Length)

Write a function which returns the number of words in the input string which have more than 4 characters.
Assume that the input string consists of alphabetic characters separated by spaces and capitalization
does not matter i.e. an upper case character should be treated the same as a lower case character.
"""

# Define Function
def count_words_length(input_string):

    count = 0
    string = input_string.lower().split()

    for word in string:
        if len(word) > 4:
            count += 1
    return  count


# Main Program
input_string = 'This is just an example of how this function works'
x = count_words_length(input_string)

print(x)


"""
################### Sample Solution ###################
def _count_of_words_sample_(input_string):
    # Create a list of strings by splitting the original string
    splitted_string = input_string.lower().split()
    # set the maximum length
    maximum_length = 4
    # Go through each string in the list we created
    count = 0
    for string in splitted_string:
        # check the length of each string
        #  it resets for each string
        string_length = len(string)
        if string_length > maximum_length:
            count = count + 1
    return count
"""
