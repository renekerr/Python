'''
Day 2 - Beginner - Understanding Data Types and How to Manipulate Strings


DATA TYPES & STRINGS


'''

#Data Types
#String

#Susbcripting
print('Hello'[0])
print('Hello'[4])

print('123' + '345')

#Integer
print(123 + 345)

#Float
pi = 3.14159

#Boolean
'''
True or False
'''

#Functions

num_char = len(input('What is your name?\n'))
print(type(num_char))
num_char_str = str(num_char)
print(type(num_char_str))
#print('Your name has ' + str(num_char) + ' characters.')
print('Your name has ' + num_char_str + ' characters.')

#Converting data types
a = 123
print(type(a))
a = str(123)

print(70 + float('100.5'))

#Mathematical Operations
#Order

#PEMDASLR (left-to-right)
#  () Parentheses
#  ** Exponents
#  * Multiplication
#  / Division // Floor Division
#  + Addition
#  - Subtraction

#Math functions
print(round(8 / 3, 2))

#f-String
score = 0
height = 1.95
isWinning = True
print(f'Your score is {score}, your height is {height}, you are winning is {isWinning}')
