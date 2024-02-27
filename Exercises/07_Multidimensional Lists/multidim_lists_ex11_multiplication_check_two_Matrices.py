'''
Multidimensional Lists, Exercise 11 (Multiplication Check of two Matrices)

Write a function that accepts two (matrices) 2 dimensional lists a and b of unknown lengths and returns True
if they can be multiplied together False otherwise. Hint: Two matrices a and b can be multiplied together only if
the number of columns of the first matrix(a) is the same as the number of rows of the second matrix(b). The input
for this function will be two 2 Dimensional lists. For example if the input lists are:

a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]

Then your function should return a boolean value:
 True

'''


# Define Function(s)
def check_multip_matrices(a, b):

    cols1 = len(a[0])
    rows2 = len(b)

    if cols1 == rows2:
        return True
    else:
        return False


# Main Program
list_a = [[2, 3, 4],
     [3, 4, 5]]
list_b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]

fn = check_multip_matrices(list_a, list_b)
print(fn)

'''
################### Sample Solution ###################
def _multiplication_check_sample_(a, b):
    columns_of_a = len(a[0])
    rows_of_b = len(b)
    if columns_of_a == rows_of_b:
        return True
    else:
        return False
'''


