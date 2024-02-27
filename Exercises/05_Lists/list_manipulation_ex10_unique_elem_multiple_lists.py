"""
List Manipulation Exercise 10 (Unique Elements From Multiple Lists)

Write a function that accepts two input lists and returns a new list which contains only the unique elements
from both lists.
"""

# Define function
def unique_elements(list_a, list_b):

    list_a.extend(list_b)
    new_list = []

    for element in list_a:
        if element not in new_list:
            new_list.append(element)

    return new_list


# Main program
list_a = ['first', 2, 'third', 'random', 5, 'sixth']
list_b = [1, 2, 'third', 4, 7]

fn = unique_elements(list_a, list_b) # Unique elements from 2 lists

print(fn)


"""
################### Sample Solution ###################
def _join_two_lists_unique_sample_(sample_list1, sample_list2):
    output_list = []
    for items1 in sample_list1:
        if items1 not in output_list:
            output_list.append(items1)

    for items2 in sample_list2:
        if items2 not in output_list:
            output_list.append(items2)
    return output_list
"""
