# List Manipulation Exercise 3 (Sorting a List)
# Write a function that accepts a list of integers and returns a new list which is the sorted version (ascending order)
# of the original list (Original list should not be modified). You may NOT use the built in sort() or sorted() functions.
# Notice that the original list should not be modified

# Defining function
def bubble_sort(original_list):

    new_list = original_list[:] # Make a copy of original list
    length = len(original_list) # Determine the length of the list
    elem_change = True        # Set to True elem_change (while loop)

    while elem_change:        # As elem_change is True while loop will go on
        elem_change = False   # In order to check list's elements until no more changes are needed

        for index in range(0,length-1):     # For loop to go through list's elements

            if new_list[index] > new_list[index + 1]:   # Comparison

                temporary = new_list[index]             # Exchange values
                new_list[index] = new_list[index + 1]
                new_list[index + 1] = temporary

                elem_change = True                      # Since list's elements were exchange it is set to True

    return new_list                                     # Return value(s)


# Main program
original_list = [32, 1, 67, 23, 99, 4]
fn = bubble_sort(original_list)

print('Original list')
print(original_list,'\n')

print('Sorted list (ascending)')
print(fn)



























