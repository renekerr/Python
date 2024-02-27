'''
Multidimensional Lists Exercise 2 (Average of a 2-D List)
Write a function that accepts a 2 Dimensional list of integers and returns the average.
Remember that average = (sum_of_all_items) / (total_number_of_items).
'''

# Define Function
def average_2D_list(list_sample):
    total_sum = 0
    count_items = 0

    for k, number in enumerate(list_sample):
        for i in range(0, len(number)):
            total_sum += number[i]
            count_items += 1

    average_list = total_sum / count_items
    return total_sum, count_items, average_list

# Main Program
list_sample = [[10, 20, 30], [70, 60, 80]]
fn = average_2D_list(list_sample)

print(fn)


'''
################### Sample Solution ###################
def _average_of_a_2d_list_sample_(sample_2d_list):
    # Initialize total sum to be 0
    total_sum = 0
    number_of_items=0
    # Get the length of rows and columns
    for row_index in range(len(sample_2d_list)):
        for col_index in range(len(sample_2d_list[row_index])):
            total_sum=total_sum+sample_2d_list[row_index][col_index]
            number_of_items=number_of_items+1
    return total_sum/number_of_items
'''