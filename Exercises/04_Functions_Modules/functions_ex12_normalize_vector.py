# Functions Exercise 12 (Normalizing a Vector)
# This program normalize a vector
# A vector can be normalized by dividing each individual component of the vector by its magnitude.

def magnitude_vector(vector):
    x = vector[0]
    y = vector[1]
    z = vector[2]

    mag = ((x**2) + (y**2) + (z**2)) ** (1/2) # the square root of sum of squares of all the components of the vector.

    # Normalize the vector by dividing each component with the magnitude
    new_x = x / mag
    new_y = y / mag
    new_z = z / mag

    unit_vector = [new_x, new_y, new_z]

    return unit_vector

# Main program
vector = [2,3,-4]
m = magnitude_vector(vector)

print(m)