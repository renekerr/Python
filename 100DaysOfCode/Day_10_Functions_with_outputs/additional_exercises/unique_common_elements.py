"""
Midterm Exam, Part 8 (Unique Common Elements)

Write a function named unique_common that accepts two lists both of which contain integers as
parameters and returns a sorted list (ascending order) which contains unique common elements
from both the lists. If there are no common elements between the two lists,
then your function should return the keyword None

For example, if two of the lists received by the function are:

([5, 6, -7, 8, 8, 9, 9, 10], [2, 4, 8, 8, 5, -7])
You can see that elements 5, -7, and 8 are common in both the first list and the
second list and that the element 8 occurs twice in both lists.
Now you should return a sorted list (ascending order) of unique common elements like this:
[-7, 5, 8]

if the two lists received by the function are:
([5, 6, 7, 0], [3, 2, 3, 2])
Since, there are no common elements between the two lists, your function should return the keyword
None
"""

# Define function
def unique_common(a, b):
    output_list = []

    for elem1 in a:
        for elem2 in b:

            if elem1 == elem2 and elem1 not in output_list:
                output_list.append(elem1)
                output_list.sort()

    if not output_list:
        return None
    else:
        return output_list


# Main program
list_a = [5, 6, -7, 8, 8, 9, 9, 10]
list_b = [2, 4, 8, 8, 5, -7]

#list_a = [5, 6, 7, 0]
#list_b = [3, 2, 3, 2]
print('Lists : ')
print(list_a)
print(list_b)

my_function = unique_common(list_a, list_b)

print(my_function)


"""
################### Instructor function ###################
def _unique_common_elements_sample_ed2_(a, b):
    common = []
    for items in a:
        if items in b:
            common.append(items)
    if not common:
        return None
    unique = []
    for items in common[:]:
        if items not in unique:
            unique.append(items)
    return sorted(unique)
"""





