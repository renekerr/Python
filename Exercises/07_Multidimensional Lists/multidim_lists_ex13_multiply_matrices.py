'''
Multidimensional Lists, Exercise 13 (Multiplication of two Matrices without numpy)

Write a function that accepts two (matrices) 2 dimensional lists a and b of unknown lengths and returns their product.
Hint: Two matrices a and b can be multiplied together only if the number of columns of the first matrix(a) is the same
as the number of rows of the second matrix(b).
Do NOT use numpy module for this exercise. The input for this function will be two 2 Dimensional lists.

For example if the input lists are:

a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]
Then your function should return their product such as:
[[15, 9, 47], [21, 10, 66]]


Ref: https://www.youtube.com/watch?v=kuixY2bCc_0
'''

# Define Function(s)
def multiply_two_matrices(m1, m2):

    if len(m1[0]) != len(m2):       # If number of cols of m1 is diff from number of rows of second matrix
        return None                 # then, matrices cannot be multiplied

    # Product matrix will be ab(2,3)
    r = len(m1)                          # Number of rows
    c = len(m2[0])                       # Number of cols

    output_list = []                     # Create an empty list
    temp_cols = c * [0]                  # How many cols will be in a row


    for i in range(r):                   # Creating a product list filled with zeros
        output_list.append(temp_cols[:])
    # If variable output_list is printed the result is [[0, 0, 0], [0, 0, 0]]
    # which is the product matrix of a*b



    for row_index in range(len(m1)):                            # Loop through rows in matrix 1 (a)
        for col_index in range(len(m2[0])):                     # Loop through columns in matrix 2 (b)

            s = 0                                               # Set adder to 0
            for k in range(len(m1[0])):                         # Loop through matrix one to get index of each element in a row
                s += m1[row_index][k] * m2[k][col_index]        # Multiply/add elements
            #print(s)
            output_list[row_index][col_index] = s

    return output_list


# Main Program
a = [[2, 3, 4],             # a (2,3)
     [3, 4, 5]]
b = [[4, -3, 12],           # b (3,3)
     [1, 1, 5],
     [1, 3, 2]]             # multiplication -> ab (2,3) size of new matrix

fn = multiply_two_matrices(a, b)
print(fn,'\n')




'''
################### Sample Solution ###################
def _product_of_two_vectors_sample_(a, b):
    if len(a[0]) != len(b):
        return None
    # Create the result matrix and fill it with zeros
    output_list=[]
    temp_row=len(b[0])*[0]
    for r in range(len(a)):
        output_list.append(temp_row[:])
    for row_index in range(len(a)):
        for col_index in range(len(b[0])):
            sum=0
            for k in range(len(a[0])):
                sum=sum+a[row_index][k]*b[k][col_index]
            output_list[row_index][col_index]=sum
    return output_list
'''







