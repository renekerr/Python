'''
Multidimensional Lists Exercise 9 (2D To 1D)

Write a function that accepts a 2-dimensional list of integers, and returns a sorted (ascending order)
1-Dimensional list containing all the integers from the original 2-dimensional list.
'''

# Define Function(s)
def convert_2D_to_1D(sample_list):
    output_list =[]
    for k, row in enumerate(sample_list):
        for elem in row:
            output_list.append(elem)

    output_list.sort()
    return output_list

# Main Program
input_list = [[1, 2, 3, 4], [0, 5, 3, 2]]
fn = convert_2D_to_1D(input_list)

print(fn)

'''
################### Sample Solution ###################
def _2d_to_1d_list_sample_(_2d_list):
    output_list = []
    for rows in _2d_list:
        for items in rows:
            output_list.append(items)
    output_list.sort()
    return output_list
'''