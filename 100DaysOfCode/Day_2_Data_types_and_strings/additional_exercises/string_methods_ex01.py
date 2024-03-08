# String Methods, Exercise 1
# These are a few examples about how some string methods work

"""
islower()
lower()
isupper()
upper()
swapcase()
title()
"""

print('Example_1')
my_str = "Hello"
print (my_str.islower(), '\n')      # Boolean result

print('Example_2')
my_str = "Goodbye"
print (my_str.lower(),'\n')

print('Example_3')
my_str = "GoodBye"     # Boolean result (False)
#my_str = "GOODBYE"      # True
print (my_str.isupper(), '\n')

print('Example_4')
my_str = "Hello"
print (my_str.upper(), '\n')

print('Example_5')
my_str = "GoodBye"
print (my_str.swapcase())

print('Example_6')
my_str = "computer science engineering"
print (my_str.title())