'''
Multidimensional Lists Exercise 1 (Sum of a 2-D List)
Write a function which accepts a 2D list of numbers and returns the sum of all the number in the list
You can assume that the number of columns in each row is the same. (Do not use python's built-in sum() function).
'''

# Define Function
def sum_2D_list(sample_list):
    
    total_sum = 0
    for i, number in enumerate(sample_list):
        for k in range(len(number)):
            total_sum += int(number[k])
    
    return total_sum

################### Sample Solution ###################
def _sum_of_a_2d_list_sample_(sample_list):
    total_sum = 0                                   # Initialize total sum to be 0
    n_rows = len(sample_list)                       # Get the length of rows and columns
    n_cols = len(sample_list[0])

    rows = 0                                        # Initialize row index to 0
    while rows < n_rows:                            # Loop through rows

        cols = 0
        while cols < n_cols:
            total_sum += sample_list[rows][cols]

            cols += 1
        rows += 1

    return total_sum




# Main Program
list_sample = [[-18, 20, 13, 44], [-12, -6, 13, -44]]
fn1 = sum_2D_list(list_sample)
fn2 = _sum_of_a_2d_list_sample_(list_sample)


print(fn1)
print(fn2)

'''
################### Sample Solution ###################
def _sum_of_a_2d_list_sample_(sample_2d_list):

    total_SUM = 0                               # Initialize total sum to be 0
    number_of_rows = len(sample_2d_list)        # Get the length of rows and columns
    number_of_columns = len(sample_2d_list[0])
    rows = 0                                    # Initialize row index to 0



    # Produce row indices 0, 1, 2, ...number_of_rows
    while rows < number_of_rows:
        # for each row, initialize the column index to 0
        columns = 0
        # Produce column indices 0, 1, 2, ... number_of_columns
        while columns < number_of_columns:
            # Added the element i.e. list[row][column] to total sum
            total_SUM = total_SUM + sample_2d_list[rows][columns]
            # Increment to the next column index
            columns = columns + 1
        # increment to the next row index
        rows = rows + 1
    # Finally return the total sum
    return total_SUM
'''

