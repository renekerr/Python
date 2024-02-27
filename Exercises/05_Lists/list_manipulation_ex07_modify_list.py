# List Manipulation Exercise 7 (Modifying a List)
# Write a function that accepts a list that contains positive integers and returns a new list which contains all the
# elements from original list but adds 1 to those elements which are odd.

# Define function
def modify_list(list_sample):

    new_list = []

    for element in list_sample:

        if element % 2 != 0:
            new_list.append(element+1)
        else:
            new_list.append(element)

    return new_list

################### Sample Solution ###################
def _list_manipulation_sample5_(my_list):
    input_list = my_list[:]
    for x in range(0, len(input_list)):
        if input_list[x] % 2 != 0:
            input_list[x] = input_list[x] + 1
    return input_list



# Main program
list_sample = [13, 13, 16, 18, 19, 21]
fn = modify_list(list_sample)

print(fn)
