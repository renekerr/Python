# List Manipulation Exercise 4 (Extending and Sorting)
# Write a function that accepts two lists both of which contain integers and returns a new list which contains all the
# elements from both lists sorted in descending order. Your new list should include duplicate elements if they exist.
# Do NOT use the built in sort() or sorted() methods.

# Defining function
def merge_and_sort(list_a, list_b):
    new_list = list_a + list_b      # Or using list.extend() method. [list_a.extend(list_b)]
    length = len(new_list)

    exchange_elements = True
    while exchange_elements:
        exchange_elements = False

        for i in range(0,length-1):


            if new_list[i] < new_list[i+1]:
                temporary_var = new_list[i]
                new_list[i] = new_list[i+1]
                new_list[i+1] = temporary_var

                exchange_elements = True
    return new_list




# Main program
list_a = [44, 32, 1, 8, 10, 2]
list_b = [78, 3, 1, 4]

fn = merge_and_sort(list_a, list_b)

print(fn)








