# Functions Exercise 6 (Average of a List)
# This program calculates the average of numbers in a list
def sum_list(my_list):

    result = 0
    count = 0

    average_result = 0

    for x in my_list:
        result = result + x
        count = count + 1

    average_result = result / count
    return average_result

# Main program
my_list = [-1, -1, -3, 4, 55, 12]
s = sum_list(my_list)

print(s)

