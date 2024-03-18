'''
NOTES ON FUNCTIONS



Most of the time we provide some arguments to a function and it returns something. However, this may not always be the case. While trying to write a function we need to decide if the function needs any arguments or notand if the function needs to return something or not. Broadly, we can attempt to classify the combination of function parameters and their return types as follows:

    1. Nothing goes in, nothing comes out. 
    2. Nothing goes in, something comes out.
    3. Something goes in, nothing comes out. 
    4. Something goes in, something comes out. 
'''


## 1. Nothing goes in, nothing comes out.
""" 
Sometimes we need to do some task repeatedly and that task never changes. In this case, the function does not need any arguments (parameters) and it does not need to return anything. 
 """

def display_message():
    print("****   PYTHON IS GREAT   ****")
    print("=============================")
    
# Main Program #
radius = 5
print("The radius of the circle is: ", radius)
display_message()    # The function call 

circumference = 2*3.14*radius
print("The circumference of the circle is:", circumference)
display_message()    # The function call 


""" Note that the parentheses in the function call do not have any anything which means the function does not take any arguments. Also nothing is set equal to the function call i.e. the function call is on a line by itself which means it does not need to return anything. So basically, this function just keeps printing the same message every time it is called (Printing something is notthe same as returning something). Even though, there is noreturn keyword in this function, it returns a None by default. 

This program produces:
The radius of the circle is:  5
****   PYTHON IS GREAT   ****
=============================
The circumference of the circle is: 31.400000000000002
****   PYTHON IS GREAT   ****
=============================
"""

##2. Nothing goes in, something comes out. 
""" A great example of a function that does not receive anything but does return something is the following.   """

import random

def report_random():
    my_number = random.randint(20, 100)
    return my_number

# Main Program #
a = report_random()    # return a random int and assign it to a
print("a is equal to ", a)
b = report_random()    # return a random int and assign it to b
print("b is equal to ", b)
c = report_random()    # return a random int and assign it to c
print("c is equal to ", c)

""" Notice that this function does not receive any arguments but each time we call this function it returns a random integer between 20 and 100 and assigns the returned value to the variable the function call was set equal to.
Sample run of this program produced: 

a is equal to  82
b is equal to  75
c is equal to  94
"""

## 3. Something goes in, nothing comes out. 
""" In this scenario, the function needs some arguments to do some task but it does not need to return anything.   """ 


def calculate_area_2(length, breadth):
    area = length * breadth
    perimeter = 2*length + 2*breadth
    print("area is equal to", area)
    print("perimeter is equal to", perimeter)

# Main Program #
calculate_area_2(10, 20)

""" Notice that this function does receive two arguments length and breadth and when we call this function, it calculates the area and perimeter of a rectangle and prints the results but it does not return anything! And again printing something is not the same as returning some value. The return value once again for this function is None as there is no return keyword.

Sample run of this program produces: 

area is equal to 200
perimeter is equal to 60
"""

## 4. Something goes in, something comes out. 
""" This is probably the most meaningful scenario where the function takes some arguments and performs some task using those arguments and returns some result as well.   """

def calculate_area(length, breadth):
    area = length * breadth
    perimeter = 2*length + 2*breadth
    my_result = [area, perimeter]    # put results in a list
    return my_result                 # return the list

# Main Program #
my_list = calculate_area(10, 20) # two arguments are supplied 
print("The resulting list looks like:", my_list)


""" Sample run of this program produces: 

The resulting list looks like: [200, 60]
Note that we can return multiple things in python by separating them with a comma. For example instead of returning the results in a list we could have done the following:
return area, perimeter
In this situation, python would have returned the two values as a 'tuple', which would have looked like:
(200, 60)
We will discuss tuples in more detail later in the course.   """


# Built-in Functions
""" The python interpreter has a number of functions built into it that are always available.  """

""" 
abs()
dict()
help()
min()
setattr()

all()
dir()
hex()
next()
slice()

any()
divmod()
id()
object()
sorted()

ascii()
enumerate()
input()
oct()
staticmethod()

bin()
eval()
int()
open()
str()

bool()
exec()
isinstance()
ord()
sum()

bytearray()
filter()
issubclass()
pow()
super()

bytes()
float()
iter()
print()
tuple()

callable()
format()
len()
property()
type()

chr()
frozenset()
list()
range()
vars()

classmethod()
getattr()
locals()
repr()
zip()

compile()
globals()
map()
reversed()
__import__()

complex()
hasattr()
max()
round()

delattr()
hash()
memoryview()
set()

 """