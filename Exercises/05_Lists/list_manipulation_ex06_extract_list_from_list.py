# List Manipulation Exercise 6 (Extracting a list from a list)
# Write a function that accepts a list and return a new list which contains all but the first and last elements of
# the original list.

# Defining function
def extract_list(list_sample):
    new_list = list_sample[1:-1]
    return new_list


# Main program
list_sample = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']
fn = extract_list(list_sample)

print(fn)