# Functions Exercise 5 (Sum of a List)
# This program sums up all values of a given list

def sum_list(my_list):
    result = 0
    for x in my_list:
        result = result + x
    return result

# Main program
my_list = [1,2,3,-5,6,7,-9]
s = sum_list(my_list)

print(s)