# String Methods, Exercise 5
# These are a few examples about how some string methods work
"""
strip()
lstrip()
rstrip()
join()
"""

print('Example_1')
x="oops too"
print (x.strip("o")) # This method returns a copy of the string with the leading and trailing characters removed
print('\n')

print('Example_2')
my_str = "oops too"
print (my_str.lstrip('o'))
print('\n')

print('Example_3')
my_str = "oops too"
print (my_str.rstrip('o'))
print('\n')

print('Example_4')
my_str = "hello hello"
print (my_str.rstrip('h'))
print('\n')

print('Example_5')
print ("NO".join("test"))
print('\n')

print('Example_6')
x= "test".join(["A","B","C"])
print (x)
print('\n')

