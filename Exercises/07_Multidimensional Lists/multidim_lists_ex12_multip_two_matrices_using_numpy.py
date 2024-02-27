'''
Multidimensional Lists, Exercise 12 (Multiplication of two Matrices)
Write a function that accepts two (matrices) 2 dimensional lists a and b of unknown lengths and returns their product.
Hint: Two matrices a and b can be multiplied together only if the number of columns of the first matrix(a)
is the same as the number of rows of the second matrix(b). Hint: You may import and use the numpy module but your
return must be a python list not a numpy array. The input for this function will be two 2 Dimensional lists.

For example if the input lists are:

a = [[2, 3, 4],
    [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]

Then your function should return their product such as:
[[15, 9, 47], [21, 10, 66]]
'''

'''
NumPy

NumPy is the fundamental package for scientific computing with Python. It contains among other things:

a powerful N-dimensional array object
sophisticated (broadcasting) functions
tools for integrating C/C++ and Fortran code
useful linear algebra, Fourier transform, and random number capabilities

Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data.
Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide
variety of databases.
'''


# Define Function(s)
import numpy as np

def multiply_two_matrices(m1, m2):

    cols = len(m1[0])
    rows = len(m2)
    if cols == rows:
        product = np.mat(m1) * np.mat(m2)
        product_list = product.tolist()

        return product_list

    else:
        return None


# Main Program
a = [[2, 3, 4],             # a (2,3)
     [3, 4, 5]]
b = [[4, -3, 12],           # b (3,3)
     [1, 1, 5],
     [1, 3, 2]]             # multiplication -> ab (2,3)

fn = multiply_two_matrices(a, b)
print(fn)


'''
################### Sample Solution ###################
def _product_of_two_vectors_sample_(a, b):
    import numpy
    product = (numpy.mat(a) * numpy.mat(b))     # returns a numpy array
    product_to_list = product.tolist()          # convert the numpy array to a standard list
    return product_to_list
'''


