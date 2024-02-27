'''
Multidimensional Lists Exercise 4 (List of Sum of Rows of a 2-D List)

Write a function that takes a two-dimensional list (list of lists) of numbers as argument and returns a list which
includes the sum of each row. You can assume that the number of columns in each row is the same.
'''


# Define Functions

# Solution 1
def _sum_rows_multidimensional_list(list_sample):
    output_list = []

    for i, elem in enumerate(list_sample):              # Loop through rows
        row_elem_sum = 0                                # Set adder to 0

        for k in range(len(elem)):                      # Loop through columns
            row_elem_sum += elem[k]                     # Add each element

        output_list.append(row_elem_sum)                # Append it to the output list

    return output_list                                  # Return output list


# Solution 2. (Shorter version)
def sum_rows_multidimensional_list(list_sample):
    output_list = []

    for elements in list_sample:
        s = sum(elements)
        output_list.append(s)
    return output_list



# Main Program
input_list = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
print(input_list, '\n')

fn1 = _sum_rows_multidimensional_list(input_list)
fn2 = sum_rows_multidimensional_list(input_list)

print(fn1)
print(fn2)


'''
################### Sample Solution ###################
def _sum_of_rows_sample_(sample_list):
    mylist = []
    for item in sample_list:
        mylist.append(sum(item))
    return mylist
'''