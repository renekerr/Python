'''
Character Encoding Exercise 2 (Character to Integer)

Write a function that accepts an alphabetic character and returns the number
associated with it from the ASCII table.
'''

# Define Function
def character_to_integer(character):
    result = ord(character)
    return result

# Main Program
print('Enter a character : ')
character = input()

fn = character_to_integer(character)
print(fn)

'''
################### Sample Solution ###################
def _character_to_integer_sample_(a):
    integer = ord(a)
    return integer
'''



