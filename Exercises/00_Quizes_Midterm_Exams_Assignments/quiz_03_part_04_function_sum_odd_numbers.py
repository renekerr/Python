#Quiz 3, Part 4
# Write a function that accepts a list of integers as parameter.
# Your function should return the sum of all the odd numbers in the list.
# If there are no odd numbers in the list, your function should return 0 as the sum.

def fn(my_list):
    s = 0
    for items in my_list:
        if items % 2 != 0:
            s = s + items
    return print(s)

# Main program
my_list = [1,3,5,4,2,6,2]
f = fn(my_list)



