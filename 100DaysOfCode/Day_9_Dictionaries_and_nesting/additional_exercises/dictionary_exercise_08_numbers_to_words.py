'''
Dictionary Exercise 8 (Numbers To Words)

Write a function that takes an integer as input argument and returns the integer using words.
For example if the input is 4721 then the function should return the string "four seven two one".
Note that there should be only one space between the words and
they should be all lowercased in the string that you return.

'''

# Define Function(s)
def numbers_to_words(n):
    result = ''
    i = str(n)
    dict_letters_numbers ={'1':'one',
                           '2':'two',
                           '3':'three',
                           '4':'four',
                           '5':'five',
                           '6':'six',
                           '7':'seven',
                           '8':'eight',
                           '9':'nine',
                           '0':'zero'}

    for k in i:
        result += dict_letters_numbers[k] + ' '

    result = result.strip() # remove any blank space
    return result

# Main Program
m = 123
fn = numbers_to_words(m)
print(fn)


'''
################### Sample Solution ###################
def _single_digit_words_sample(sample_integer):
    string_input = str(sample_integer)      # convert the integer input into a string
    splitted = list(string_input)           # split the string into a list of characters
    sample_dictionary = {"1" : "one",
                         "2" : "two",
                         "3" : "three",
                         "4" : "four",
                         "5" : "five",
                         "6" : "six",
                         "7" : "seven",
                         "8" : "eight",
                         "9" : "nine",
                         "0" : "zero"}
    output_string = ""
    for integer in splitted:
        output_string += sample_dictionary[integer] + " "
    # remove any trailing whitespace
    stripped = output_string.rstrip(" ")
    return stripped
'''