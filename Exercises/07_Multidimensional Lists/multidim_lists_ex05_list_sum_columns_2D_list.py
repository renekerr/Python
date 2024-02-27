'''
Multidimensional Lists Exercise 5 (List of Sum of Columns of a 2-D List)

Write a function that takes a two-dimensional list (list of lists) of numbers as argument and returns a list
which includes the sum of each column. Assume that the number of columns in each row is the same.
'''

# Define Function(s)
# Solution 1
def sum_columns_multidimensional_lists(list_sample):

    length_cols = len(list_sample[0])
    output_list = []

    for c in range(length_cols):
        cols_sum = 0

        for rows in list_sample:
            cols_sum += rows[c]

        output_list.append(cols_sum)

    return output_list

# Solution. Simplified way 1
def _sum_columns_multidimensional_lists(list_sample):

    # zip() in conjunction with the * operator can be used to unzip a list
    # should only be used with unequal length inputs when you don’t care about trailing,
    # unmatched values from the longer iterables
    output_list = []
    x = list(zip(*list_sample))
    #print(x)

    for k in x:
        s = 0
        s = s + sum(k)
        output_list.append(s)

    return output_list

# Solution. Simplified way 2
def _sum_columns_multidimensional_lists_(list_sample):

    return [sum(col) for col in zip(*list_sample)]


# Main Program
list_a = [[10, 20, 30],
          [40, 50, 60]]

fn1 = sum_columns_multidimensional_lists(list_a)
fn2 = _sum_columns_multidimensional_lists(list_a)
fn3 = _sum_columns_multidimensional_lists_(list_a)

print(fn1)
print(fn2)
print(fn3)



'''
################### Sample Solution ###################
def _sum_of_columns_sample_(sample_list):

    # Solution type 1:
    # return [max(col) for col in zip(*sample_list)]

    # Solution type 2:
    cols = len(sample_list[0])
    mylist = []
    for c in range(cols):
        column_sum = 0
        for row in sample_list:
            column_sum += row[c]
        mylist.append(column_sum)
    return mylist
'''














