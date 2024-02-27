"""
Write a function which returns the total number of vowels in an input string which consists of alphabetic characters.
Note that capitalization does not matter here i.e. a lower case character should be considered the same as an
upper case character. For this problem, the vowels are considered to be A, E, I, O, U.
"""

# Define Function
def vowels_count(input_string):
    string = input_string.lower()
    vowels = 'aeiou'
    total_vowels = 0

    for char in string:
        if char in vowels:
            total_vowels = total_vowels + 1

    return total_vowels

# Main Program
input_string = 'He would learn to fly one day'
fn = vowels_count(input_string)

print('In the string:\n', "\'" ,input_string, "\'", '\nthere are',fn, 'vowels')

"""
################### Sample Solution ###################
def _total_vowels_sample_(sample_string):
    count = 0
    sample_string=sample_string.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']

    for char in sample_string:
        if char in vowels:
            count = count + 1
    return count
"""
