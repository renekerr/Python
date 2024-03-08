# List Manipulation Exercise 1 (Updating a List)
# Write a function that accepts a list (which gas a length of 4 or more) and a string and returns the list
# such that the second through the fourth element (index 1 through 3 both inclusive) in the input list are replaced
# by the input string.

def slice_function_1(input_list, input_string):                 # Define function passing list as parameter

    for i in range(1,4):                                        # Loop from index 1 to 3
        input_list[i] = input_string                            # Assign input_string to input_list on index selected
                                                                # in this case, 1 to 3


    return input_list                                           # Return values

# Main program
input_list = ['Isha','Chand', 'Sri Vasya', 'Mandukya', 'Sri']
input_string = input('Enter a string: ')

print('List')
print(input_list, '\n')

f = slice_function_1(input_list, input_string)
print('List modified: ')
print(f)

















