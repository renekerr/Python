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
    keys_dict = list(dict_letters_numbers.keys())
    values_dict = list(dict_letters_numbers.values())

    #print(i)
    #print(keys_dict)
    #print(values_dict)



    return None

# Main Program
m = 4721
fn = numbers_to_words(m)

print(fn)
