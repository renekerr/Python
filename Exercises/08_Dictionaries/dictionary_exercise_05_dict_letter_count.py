'''
Dictionary Exercise 5 (Dictionary of Letter Count)

Write a function that takes a string as input argument and returns a dictionary of letter counts i.e. the keys of
this dictionary should be individual letters and the values should be the total count of those letters.
You should ignore white spaces and they should not be counted as a character. Also note that a small letter
character is equal to a capital letter character.
'''

# Define Function(s)
def dict_letter_count(sample_str):

    s = sample_str.replace(' ','').lower()
    sample_dict = {}


    for char in s:
        #print(char)
        sample_dict[char] = s.count(char)

    return sample_dict


# Main Program
sample_string =' Hard Work'
fn = dict_letter_count(sample_string)
print(fn)


'''
def _dictionary_of_letter_counts_sample_(sample_string):

    stripped_string = sample_string.replace(" ", "")        # remove all white spaces
    lowercase_stripped_string = stripped_string.lower()     # convert to lower case
    sample_dictionary = {}

    # Iterate through the lowercase stripped string and set each
    # character as a key and its count as the value
    for character in lowercase_stripped_string:
        sample_dictionary[character] = lowercase_stripped_string.count(character)
    return sample_dictionary
'''
