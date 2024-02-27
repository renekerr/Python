# List Manipulation Exercise 4 (Extending and Sorting)
# Write a function that accepts two lists both of which contain integers and returns a new list which contains all the
# elements from both lists sorted in descending order. Your new list should include duplicate elements if they exist.
# Do NOT use the built in sort() or sorted() methods.

################### Sample Solution ###################
def merge_and_sort(list_a, list_b):
    list_a.extend(list_b)

    # Create a new list
    new_list = []

    # Loop until a becomes empty
    while list_a:

        # set an arbitrary element as the minimum
        # in this case we chose the first index
        maximum = list_a[0]

        # loop through the list and
        # find the element that is smallest
        for element in list_a:
            if element > maximum:
                maximum = element
        # append the smallest element to the new list
        new_list.append(maximum)

        # now remove that smallest element from the original list
        list_a.remove(maximum)
    # Ultimately a will become empty
    # and the loop will end
    # now return the new list
    return new_list




# Main program
list_a = [44, 32, 1, 8, 10, 2]
list_b = [78, 3, 1, 4]

fn = merge_and_sort(list_a, list_b)

print(fn)








