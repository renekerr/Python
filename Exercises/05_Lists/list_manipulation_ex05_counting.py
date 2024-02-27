# List Manipulation Exercise 5 (Counting an item in a list)
# Write a function that accepts a list and a value of an element and returns the count of how many times that element
# appears in the list. The behaviour of this function should be exactly like the list.count() method.
# You may NOT use any built in list methods for this problem.


# Defining function
def count_item(list_sample,value_x):
    k = 0

    for element in list_sample:
        if value_x == element:
            k = k + 1

    return k



# Main program
list_sample = ['hello', 23, 9.9, 'food' , 'cat', 'horse', 89, 'food']
value_x = 'food'
fn = count_item(list_sample,value_x)

print(fn)