# Python Modules Exercise 3 (Find Distance between two points)
# Write a function that finds the distance between two points and returns it.
# The distance between two points with x,y, and z components can be calculated as:
# distance = sqrt{(x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2}

from math import *
def my_math_fn(a,b):

    x1, y1, z1 = a[0], a[1], a[2]
    x2, y2, z2 = b[0], b[1], b[2]

    distance = sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    ## or distance = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**(1/2)
    return distance


# Main program
a = [2, 3, -5]
b = [4, -3, 12]
m = my_math_fn(a,b)

print(m)