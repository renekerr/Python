# Functions Exercise 11 (Magnitude of a Vector)
# This program calculates the magnitud of a vector
# The magnitude of a vector is the square root of sum of squares of all the components of the vector.

def magnitude_vector(vector):
    x = vector[0]
    y = vector[1]
    z = vector[2]

    mag = ((x**2) + (y**2) + (z**2)) ** (1/2) # the square root of sum of squares of all the components of the vector.


    return mag


# Main program
vector = [2,3,-4]
m = magnitude_vector(vector)

print(m)
