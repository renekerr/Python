"""
Strings Exercise 7 (Most Common Character)

Write a function that takes a string consisting of alphabetic characters as input argument and returns the most common character.
Ignore white spaces i.e. Do not count any white space as a character. Note that capitalization does not matter here i.e.
that a lower case character is equal to a upper case character.
In case of a tie between certain characters return the last character that has the most count

"""
# Define Function
def most_common_character(string):

    string = string.lower()
    max_count = 0
    most_common_char = ''

    for k in range(len(string)):
        sub = string[k]

        if sub == ' ':
            continue

        else:
            c = string.count(sub)

        if c >= max_count:                  # Compare with a preset variable ( max_count = 0 )
                                            # c >= max_count, in case of a tie, return 'last' character most counted
                                            # c >  max_count, in case of a tie, return 'first' character most counted

            max_count = c                   # If True, assign to preset variable (max_count)
            most_common_char = sub          # Assign most common character to preset variable (most_common_char = '')


    return most_common_char


# Main Program

input_string = 'ya gotta make do with what ya got'
fn = most_common_character(input_string)

print(fn)




"""
################### Sample Solution ###################
def _most_common_character_(sample_string):
    stripped_string = sample_string.replace(" ", "")    # remove all white spaces
    lowercase_stripped_string = stripped_string.lower()    # convert to lower case
    sample_character = None
    sample_maximum_count = 0

    # Iterate through the given string and for each character
    # set a count, among these counts,  return the character whose count is maximum
    # On case of tie, return the last character that occurs that has the most count
    for character in lowercase_stripped_string:
        each_character_count = lowercase_stripped_string.count(character)
        if each_character_count >= sample_maximum_count:
            sample_maximum_count = each_character_count
            sample_character = character
    return sample_character
"""

















