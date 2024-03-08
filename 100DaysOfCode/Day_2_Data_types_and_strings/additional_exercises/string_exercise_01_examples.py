"""
Strings, Exercise 1

What will be printed after each of the following code segments? If error, then write Error
These examples show how to use/manipulate strings
"""

print('Example1')
x="university"
print (x[0:4])  # Element 4 (e) is not included.
print('\n')


print('Example2')
x="university"
print (x[-5:-3])    # Start with index -5 and go to index -4 and notice that element -3 is not included
print('\n')


print('Example3')
x="university"
print (x[-5:-2])    # r is element with index -5, s is element with index -4 and i is element with index -3,
print('\n')         # element with index -2 will not be included



print('Example4')
x="university"
print (x[5:0:-2])   # Start from index 5 going back to index 1 in steps of two.
print('\n')