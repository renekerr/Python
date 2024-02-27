'''
Dictionary Exercise 2 (Sorted Values)

Write a function that accepts a dictionary as input and returns a sorted list of all the values in the dictionary.
Assume that the values of this dictionary are just integers.
'''

# Define Function(s)
def dict_sorted_values(dict_sample):
    dict_values = dict_sample.values()
    dict_values = list(dict_values)
    dict_values.sort() # Sort ascending
                       # Sort descending sort(reversed=True)

    return dict_values

# Main Program
d = {'five':5, 'four':4, 'three':3, 'two':2, 'one':1, 'zero':0}
fn = dict_sorted_values(d)
print(fn)


'''
################### Sample Solution ###################
def _sorted_values_sample_(sample_dictionary):
    # Use the built in values() function
    # to generate a dictionary view
    values = sample_dictionary.values()
    # change dictionary view to list
    values = list(values)
    values.sort()
    return values
'''