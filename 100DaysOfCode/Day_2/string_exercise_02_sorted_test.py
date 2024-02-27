"""
Strings Exercise 2 (Sorted Test)

Write a function that takes a list of words as an input argument and returns True
if the list is sorted and returns False otherwise.
"""

# Define Function
def sort_list(list_a):
    list_b = list_a[:]
    list_b.sort()

    if list_a == list_b:
        return True
    else:
        return False


# Main Program
list_a = ['a', 'b', 'c', 'd', 'e']

x = sort_list(list_a)
print(x)


"""
################### Sample Solution ###################
def _is_sorted_sample_(sample_list):
    # Create a copy of the sample_list using list slicing
    copy_original = sample_list[:]
    # Sort the sample list using python's built in sort() method
    sample_list.sort()
    # Compare the original list with the now sorted list to see if they are equal
    if copy_original == sample_list:
        return True     # Sample list was already sorted
    else:
        return False    # Sample list was not sorted
"""













