# Example of functions


#1
# Nothing goes in, nothing comes out.
print("Example_1")
print("¨¨¨¨¨¨¨¨¨")
def display_message(): # this function does not take any arguments
    print("****   PYTHON IS GREAT   ****")
    print("=============================")

# Main Program #
radius = 5
print("The radius of the circle is: ", radius)
display_message()    # The function call

circumference = 2*3.14*radius
print("The circumference of the circle is:", circumference)
display_message()    # The function call
print("\n")



#2
# Nothing goes in, something comes out.
print("Example_2")
print("¨¨¨¨¨¨¨¨¨")
import random

def report_random(): # this function does not receive any arguments **
    my_number = random.randint(20, 100)
    return my_number # ** but each time it's called it returns a random integer

# Main Program #
a = report_random()    # return a random int and assign it to a
print("a is equal to ", a)
b = report_random()    # return a random int and assign it to b
print("b is equal to ", b)
c = report_random()    # return a random int and assign it to c
print("c is equal to ", c)
print("\n")



#3
# Something goes in, nothing comes out.
print("Example_3")
print("¨¨¨¨¨¨¨¨¨")
def calculate_area(length, breadth):
    area = length * breadth
    perimeter = 2*length + 2*breadth
    print("area is equal to", area)
    print("perimeter is equal to", perimeter)

# Main Program #
calculate_area(10, 20)
print("\n")


#4
# Something goes in, something comes out.
print("Example_4")
print("¨¨¨¨¨¨¨¨¨")
def calculate_area(length, breadth):
    area = length * breadth
    perimeter = 2*length + 2*breadth
    my_result = [area, perimeter]    # put results in a list
    return my_result               # return the list

# Main Program #
my_list = calculate_area(10, 20) # two arguments are supplied
print("The resulting list looks like:", my_list)



