'''
Dictionary Exercise 1 (Sorted Keys)

Write a function that accepts a dictionary as input and returns a sorted list of all the keys in the dictionary.
'''
# Define Function(s)
def dict_sorted_keys(d1):
    sorted_list = list(d1.keys())
    sorted_list.sort() # From A to Z

    # Or sort(reverse=True) if sorted from Z to A

    return sorted_list

# Main Program
dict_sample = {'Name':'Alex', 'Age':42, 'Job':'Python Programmer', 'City':'Auckland'}
fn = dict_sorted_keys(dict_sample)

print(fn)

'''
################### Sample Solution ###################
def _sorted_keys_sample_(sample_dictionary):
    # Use the built in keys() function to generate a dictionary view
    keys = sample_dictionary.keys()
    # change dictionary view to list
    keys = list(keys)
    keys.sort()
    return keys
'''

