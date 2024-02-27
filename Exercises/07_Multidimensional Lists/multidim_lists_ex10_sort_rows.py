'''
Multidimensional Lists Exercise 10 (Sort Rows)

Write a function that accepts a 2-dimensional list of integers, and sorts
(descending order) all the elements inside each row and returns the sorted 2-dimensional
list.
'''

# Define Function(s)
def sort_rows_1(list_sample):                           # Solution I
    output_list = []

    for i, elem in enumerate(list_sample):
        output_list.append(sorted(elem, reverse=True))
    return output_list

def sort_rows_2(list_sample):                           # Solution II
    for rows in list_sample:
        rows.sort(reverse=True)
    return list_sample


# Main Program
input_list = [[1,2,3], [10, 20, 30]]
#print(input_list)
fn1 = sort_rows_1(input_list)
fn2 = sort_rows_2(input_list)
print(fn1)
print(fn2)

'''
################### Sample Solution ###################
def _2d_rows_sorted_sample_(_2d_list):
    for rows in _2d_list:
        rows.sort(reverse=True)
    return _2d_list
'''