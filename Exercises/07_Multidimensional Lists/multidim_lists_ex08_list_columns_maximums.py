'''
Multidimensional Lists Exercise 8 (List of Column Maximums)

Write a function that takes a two-dimensional list (list of lists) of numbers as argument and returns a
list which includes the maximum value of each column. Assume that the length of columns is consistent in each row.
'''

# Define Function(s)
def list_cols_maximums_2(sample_list):          # Solution I

    cols = len(sample_list[0])
    output_list = []

    for k in range(cols):
        column_max = 0

        for row in sample_list:
            r = row[k]
            if r > column_max:
                column_max = r

        output_list.append(column_max)

    return output_list


def list_cols_maximums_1(sample_list):          # Solution II

    output_list = []
    z = list(zip(*sample_list))
    #print(z)

    for k, elements in enumerate(z):
        output_list.append(max(elements))
    return output_list



# Main Program
input_list = [[1, 1, 1, 12], [10, 2, 2, 2], [3, 3, 20, 3], [4, 40, 4, 4]]
fn1 = list_cols_maximums_1(input_list)
fn2 = list_cols_maximums_2(input_list)



print(fn1)
print(fn2)

'''
################### Sample Solution ###################
def _max_of_columns_sample_(sample_list):
    cols = len(sample_list[0])
    mylist = []

    for c in range(cols):
        column_max = 0
        for row in sample_list:
            if row[c] > column_max:
                column_max = row[c]
        mylist.append(column_max)
    return mylist
'''

