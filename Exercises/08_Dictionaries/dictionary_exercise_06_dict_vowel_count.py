'''
Dictionary Exercise 6 (Dictionary of Vowel Count)

Write a function that takes a string as input argument and returns a dictionary of vowel counts i.e.
the keys of this dictionary should be individual vowels and the values should be the total count of those vowels.
You should ignore white spaces and they should not be counted as a character. Also note that a small letter vowel
is equal to a capital letter vowel.
'''

# Define Function(s)
def dict_vowel_count(sample_str):
    s = sample_str.replace(' ','').lower()
    vowels = 'aeiou'
    output_dict = {}

    for character in s:
        if character in vowels:
            output_dict[character] = s.count(character)

    return output_dict

# Main Program
sample_string = 'The quick brown fox jumps over the lazy dog'
fn = dict_vowel_count(sample_string)

print(fn)

'''
################### Sample Solution ###################
def _dictionary_of_vowel_counts_sample_(sample_string):
    stripped_string = sample_string.replace(" ", "")        # remove all white spaces
    lowercase_stripped_string = stripped_string.lower()     # convert to lower case
    sample_dictionary = {}
    vowels = ["a", "e", "i", "o", "u"]
    # Iterate through the given string and set each
    # character as a key and its count as the value
    for character in lowercase_stripped_string:
        if character in vowels:
            sample_dictionary[character] = sample_string.count(character)
    return sample_dictionary
'''
