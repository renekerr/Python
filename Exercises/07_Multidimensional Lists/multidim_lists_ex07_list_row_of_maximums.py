'''
Multidimensional Lists Exercise 7 (List of Row Maximums)

Write a function that takes a two-dimensional list (list of lists) of numbers as argument and returns a
list which includes the maximum value of each row.
'''

# Define Function(s)
def list_of_row_maximums(sample_list):
    output_list = []
    for k, elements in enumerate(sample_list):
        output_list.append(max(elements))
    return output_list

def _list_of_row_maximums(sample_list):
    return [max(elements) for elements in sample_list]

# Main Program
input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
fn1 = list_of_row_maximums(input_list)
fn2 = _list_of_row_maximums(input_list)

print(fn1)
print(fn2)


'''
################### Sample Solution ###################
def _max_of_rows_sample_(sample_list):
    mylist = []
    for item in sample_list:
        mylist.append(max(item))
    return mylist
'''

