# String Methods, Exercise 6
# These are a few examples about how some string methods work
"""
split()
str.split(sep=None, maxsplit=-1)
This method returns a list of the words in the string, using sep as the delimiter string.
If maxsplit is given, at most maxsplit splits are done.
If maxsplit is not specified or -1, then there is no limit on the number of splits.
"""

print('Example_1')
x="hello are you there"
print (x.split())
print('\n')

print('Example_2')
my_str = "hello hello"
print (my_str.split('l'))
print('\n')

print('Example_3')
my_str='Computer science'
print (my_str.split ('e'))
print('\n')

print('Example_4')
x="frequency of letters"
print (x.split("e",2))
print('\n')

print('Example_5')
x="Mississippi"
print (x.split("s",3))
print('\n')
