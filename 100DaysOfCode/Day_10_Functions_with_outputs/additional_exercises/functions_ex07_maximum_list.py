# Functions Exercise 7 (Maximum of a List)
# This program calculates the maximum of a given list

def maximun_value(my_list):

    max_value_1 = my_list[0] # first element of the list is set to maximum
    for x in my_list:
        if x > max_value_1: # compare 1 by 1 each of the elements
            max_value_1 = x # if True assign value to max_value_1

    result = max_value_1
    return result


# Main program
my_list = [3, 4, -5, 1]
r = maximun_value(my_list)

print("Maximum value of the list is ",r)
