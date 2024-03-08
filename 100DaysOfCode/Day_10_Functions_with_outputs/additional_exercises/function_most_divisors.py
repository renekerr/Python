"""
Midterm Exam, Part 3 (Most Divisors)

Write a function called find_integer_with_most_divisors that accepts a list of integers and returns the integer from
the list that has the most divisors. In case of a tie, return the first item that has the most divisors. For example:

if the list is:

 [8, 12, 18, 6]
In this list, 8 has four divisors which are: [1,2,4,8] ; 12 has six divisors which are: [1,2,3,4,6,12];
18 has six divisors which are: [1,2,3,6,9,18] ; and 6 has four divisors which are: [1,2,3,6].
Notice that both 12 and 18 are tied for maximum number of divisors (both have 6 divisors).
Your function should return the first item with maximum number of divisors; so it should return:
 12

"""



# Define function
def find_integer_with_most_divisors(input_list):
    max_divisors = 0
    max_divisor_element = None

    for elements in input_list:     # Loop to go through list's elements, 1 by 1
        output_list = []  # Empty list to hold divisors

        for divisors in range(1, elements + 1):
            if elements % divisors == 0:
                output_list.append(divisors)
        print(output_list)

        length = len(output_list)

        if length > max_divisors:
            max_divisors = length
            max_divisor_element = elements
    return max_divisor_element


# Main program
list_sample = [8, 12, 18, 6]
print('List')
print(list_sample, '\n')

print('Divisors of each list element')
fn = find_integer_with_most_divisors(list_sample)


print('\nFirst item with maximum number of divisors is : ', fn)




"""
################### Instructor function ###################
def _integer_with_most_divisors_(sample_list):

    # first set max_divisors to 0
    max_divisors = 0
    max_divisors_item = None

    for items in sample_list:
        # create a list to hold the divisors of all items in the list
        output_list = []

        for number in range(1, items):
            # Check for the remainder when k is divided by number
            # if the remainder is 0 that means number is a divisor of k

            if items % number == 0:

                # append number to the output list
                output_list.append(number)

        length = len(output_list)
        # if the length of divisors for a particular element
        # is greater than the current one i.e max_divisors
        # then set max_divisors as that length and max_divisor_item as
        # that particular item

        if length > max_divisors:
            max_divisors = length
            max_divisors_item = items
    return max_divisors_item
"""



#
# http://raymondtaught.me/the-python-way-10-tips/
#
