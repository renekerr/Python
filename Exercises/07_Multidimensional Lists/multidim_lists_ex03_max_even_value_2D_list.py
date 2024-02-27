'''
Multidimensional Lists Exercise 3 (Maximum Even Value of a 2-D List)

Write a function that accepts a 2D list of integers and returns the maximum EVEN value for the entire list.
You can assume that the number of columns in each row is the same. Your function should return None if the list is
empty or all the numbers in the 2D list are odd. Do NOT use python's built in max() function.
'''

# Define Function
def max_even_value_2D_list(sample_list):
    max_even = 0

    for i, number in enumerate(sample_list):            # Loop through rows
        for k in range(len(number)):                    # Loop through columns
            # Ways to display date in 2D list : print(number[k]) or print(list_sample[i][k])

            if number[k] % 2 == 0:                      # Check if a number is EVEN

                if number[k] > max_even:                # Check maximum value
                    max_even = number[k]

    if not sample_list or max_even == 0:                # If list is empty or all numbers are ODD
        return None

    return max_even



# Main Program
list_sample = [[121, -18, 20, 13, -44], [199, -12, -6, 13, -44]]
#list_sample = []
#list_sample = [[1, 3, 5], [7, 9, 11]]

fn = max_even_value_2D_list(list_sample)
print(fn)



'''
################### Sample Solution ###################
def _maximum_even_value_sample_(sample_2d_list):
    if not sample_2d_list: # list is empty
        return None
    result=None
    for row in sample_2d_list:
        row_max=_max_even_of_1d_list(row)
        if row_max:
            if result==None or row_max>result:
                result=row_max
    return result

def _max_even_of_1d_list(input_list):
    result=None
    for element in input_list:
        if element%2 ==0: # if element is even
            if result==None or element>result:
                result=element
    return result
'''