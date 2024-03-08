# String Methods, Exercise 3
# These are a few examples about how some string methods work

"""
find()
rfind()
replace()
"""


print('Example_1')
print ("abcdef".find("e"))
print('\n')

print('Example_2')
x="Mississippi"
print (x.rfind('si',3))
print('\n')

print('Example_3')
my_string = "knickknack"
print (my_string.rfind('k',3,-2))
print('\n')

print('Example_4')
my_str='Engineering'
print (my_str.replace('e','x'))
print('\n')

print('Example_5')
print ("Mississippi".replace('i','z',2))
print('\n')