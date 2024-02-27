"""
List Manipulation Exercise 9 (Unique Elements)

Write a function that accepts an input list and returns a new list which contains only the unique elements
(Elements should only appear one time in the list and the order of the elements
must be preserved as the original list. )
"""

# Define function
def unique_list_elements(list_sample):
    new_list = []

    for element in list_sample:
        # if element is not in the list add it
        if element not in new_list:
            new_list.append(element)
        # otherwise skip it
        else:
            continue
    return new_list


# Main program
list_sample = ['hello', 1, 22, 'cat', 'hello', 'cat', 33, 22, 'last']
fn = unique_list_elements(list_sample)

print(fn)

"""
################### Sample Solution ###################
def _unique_list_sample_(sample_list):
    output_list = []
    for items in sample_list:
        if items not in output_list:
            output_list.append(items)
    return output_list

"""



