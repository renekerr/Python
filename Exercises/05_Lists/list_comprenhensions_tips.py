# The Python Way: 10 Tips.
# http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/


print('1: List Comprehensions')                       # LIST COMPREHENSIONS
bag = [1,2,3,4,5]
print('Original list')
print('bag =', bag, '\n')

"""
If you want to double elements in the list
Beginners way

for i in range(len(bag)):
    bag[i] = bag[i] * 2
"""

print('Simplified way')
bag = [1,2,3,4,5]
bag = [elem * 2 for elem in bag]


print(bag, '\n\n')


print('2: Iterating through a list')              # ITERATING THROUGH A LIST
bag = [1, 2, 3, 4, 5]
print('Original list')
print('bag =', bag, '\n')
"""
Again, suppose you have a list.
Try to avoid doing this if you can:

for i in range(len(bag)):
    print(bag[i])
"""


print('Simplified way')
# Rather, you should do this:
for i in bag:
    print(i)

print('\n')

"""
Since x is a list, you can iterate over the elements of it.
Most of the time, you won't need the index of the elements anyways,
but in case you do, there's the enumerate function available. It works like this:

For more info:
https://docs.python.org/2/library/functions.html#enumerate

enumerate(sequence, start=0)
Return an enumerate object. sequence must be a sequence, an iterator, or some other object which supports iteration


"""

print('Using the enumerate function')
bag = ['cat', 'dog', 'duck', 'text']

for index, element in enumerate(bag):
    print(index, element)

print('\n')

print('Another example of function enumerate()')
list_sample = ['elem1', 'elem2', 'elem3', 'elem4', 'elem5']
y = list(enumerate(list_sample))
print(y,'\n')

print('Different start index')
y = list(enumerate(list_sample, start = 1))
print(y,'\n\n')


print('3. Swapping Elements')                       # SWAPPING ELEMENTS
"""
Traditional programming
a = 5
b = 10

# Swap a and b
tmp = a
a = b
b = tmp
"""

print('Python way')
a = 5
b = 10
print('a=', a, 'b=', b)
# Swap a and b
a, b = b, a
print('a=', a, 'b=', b, '\n\n')


print('4. Initializing a List')                 # INITIALIZING A LIST
# Suppose you needed a list of 10 integers set to 0.
# You may be tempted to do something like this:
list_sample = []
for _ in range(10):
    list_sample.append(0)
print(list_sample,'\n')


print('Do this instead')
y = list_sample[0]*10
print(y, '\n\n')


print('5. String building')                 # STRING BUILDING
"""
Avoid doing this if you have lots of variables to print:

name = "Raymond"
age = 22
born_in = "Oakland, CA"
string = "Hello my name is " + name + "and I'm " + str(age) + " years old. I was born in " + born_in + "."
print(string)
"""

print('Use instead function format()')
name = 'Alex'
age = 41
born_in = 'Havana'
output_string = 'Hello. My name is {0}, I am {1} years old. I was born in {2}.'.format(name, age, born_in)
print(output_string,'\n\n')


print('6. Returning tuples')                # RETURNING TUPLES
"""
Python allows you to return multiple elements in a function. This makes life a lot easier.
However, this is common mistake when unpacking the tuple:


def binary():
    return 0, 1

result = binary()
zero = result[0]
one = result[1]
"""
print('Simplified way')

def binary():
    return 0,1
zero, one = binary()
print(binary())









































