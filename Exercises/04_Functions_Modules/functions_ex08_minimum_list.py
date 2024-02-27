# Functions Exercise 8 (Minimum of a List)
# This program calculates the minimum of a given list

def minimun_list(my_list):
    min_value = my_list[0] # first element of the list is set to minimum

    for x in my_list:   # compare 1 by 1 each of the elements
        if x < min_value: # if any other element of the list is lower will be assigned to var min_value
            min_value = x
    result = min_value
    return result


# Main program
my_list = [-13, 4, -5, 1]
m = minimun_list(my_list)

print(my_list)

print("Minimun element of the list is: ",m)
