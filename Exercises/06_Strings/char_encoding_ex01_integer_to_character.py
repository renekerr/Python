'''
Character Encoding Exercise 1 (Integer to Character)
Write a function that accepts a positive integer n and returns the ASCII character associated with it.
'''

# Define Function
def integer_to_char(n):
    result = chr(n)
    return result

# Main Program
print('Enter an integer number : ')
n = int(input())

fn = integer_to_char(n)
print(fn)


'''
################### Sample Solution ###################
def _integer_to_character_sample_(a):
    character = chr(a)
    return character
'''

