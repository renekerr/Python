"""
Midterm Exam, Part 6 (ListsiL)

Write a function named crazy_list that accepts a list as parameter and returns a boolean (either True or False) based on
whether or not the list is the same forward and backwards. You may NOT use list.reverse() method.

For example, if the list received by the function is:

[5, 6, 8, 9, 'PYTHON', 9, 8, 6, 5]
(Notice how the list is exactly the same whether you read it from left to right, or from right to left)
Then your function should return the Boolean
True
however, if the list received by the function is something like this:
[4, 5, 6, 7, 8, 4, 5, 2]
(Notice how the list is NOT the same when reading from left to right vs right to left) In this case, your function
should return the Boolean
False
"""


"""
Example 1
This program determines if a list can be read the same from left to right, or from right to left
In this first example the original list is read from right, a new list is created and compared with the original list
"""

# Define function
def list_palindrome(list1):
    length = len(list1)
    compare_list = []

    # Create a new list from original list (reversed)

    for i in range(length - 1, -1, -1):         # Go through list from end to start
        compare_list.append(list1[i])           # Keep elements in a new list

    if list1 == compare_list:                   # Compare original list with new list (compare_list)
        return True
    else:
        return False

# Main program
list_sample_1 = [5, 6, 8, 9, 'PYTHON', 9, 8, 6, 5]
my_function_1 = list_palindrome(list_sample_1)

print('Example 1')
print('List :')
print(list_sample_1)

print('Is the list palindrome ?', my_function_1, '\n')



"""
Example 2
This program determines if a list can be read the same from left to right, or from right to left
In this second example the list is divided in 2. First and second half (reversed), they are compared.
"""

# Define function
def list_palindrome_sample(list2):
    length = len(list2)

    if length % 2 == 0:
        mid = int(length / 2)

        first_half = list2[0:mid]
        second_half = list2[-1:mid - 1:-1]  # Another way to write this code. second_half = list2[mid::][::-1]
    else:
        mid = int(length / 2)

        first_half = list2[0:mid]
        second_half = list2[-1:mid:-1]  # Another way to write this code. second_half = list2[mid + 1::][::-1]

    if first_half == second_half:
        return True
    else:
        return False


# Main program
list_sample_2 = [4, 5, 6, 7, 6, 5, 4, 'cat']
my_function = list_palindrome_sample(list_sample_2)
print('Example 2')
print('List')
print(list_sample_2)

print('Is the list palindrome ? ', my_function)




"""
Example 3
This is the solution from the tutor
################### Instructor function ###################
def _test_list_palindrome_sample_ed2(some_list):
    size = len(some_list)
    if size % 2 == 0:
        # if the length is even
        mid = int(size / 2)
        first_half = some_list[0:mid]
        # get the second half and reverse it
        second_half = some_list[mid::][::-1]
    else:
        mid = int((size) / 2)
        # get the first half
        first_half = some_list[0:mid]
        # get the second half and reverse it
        second_half = some_list[mid + 1::][::-1]
    if first_half == second_half:
        return True
    else:
        return False

"""