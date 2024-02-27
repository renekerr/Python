# List Manipulation Exercise 2 (Extending a List Without List Functions)
# Write a function that accepts two lists A and B and returns a new list which contains all the elements of list A
# followed by elements of list B. Notice that the behaviour of this function is different from list.extend() method
# because the list.extend() method extends the list in place, but here you are asked to create a new list and return it.
# Your function should not return the original lists.

def extended_list(A,B):

    # In python we can simply implement our
    # version of list.extend using the '+' operator

    new_list = A + B        # Or new_list = A[:] + B[:], which is the same
    return new_list

# Main program
A = ['TEST','p', 'q', 6, 'k', 99]
B = [8, 10, 'cat', 'dog']

fn = extended_list(A,B)

print(fn)
