'''
Dictionary Exercise 4 (Value Containing Key)

Write a function which accepts a dictionary and an integer as input and returns an ascending sorted list
of all the keys whose values contain the input value.
Note that the keys of this dictionary are strings while the values of this dictionary are
1 Dimensional lists of integers. For example if the input dictionary is:

sample = {"rabbit" : [1, 2, 3],
          "kitten" : [2, 2, 6],
          "lioness": [6, 8, 9]}

and the input integer is 2 then your function should return:

[ "kitten", "rabbit",]

If the input integer is not found then your function should return an empty list.
'''

# Define Function(s)
def value_containing_key(d,n):

    output_list =[]                     # Create an empty list to display results
    keys = d.keys()                     # Create a variable with keys from dictionary

    for k in keys:
        #print(k, d[k])
        i_values = d[k]
        #print(i_values)

        if n in i_values:
            output_list.append(k)
        output_list.sort()
    return  output_list


# Main Program
sample_dict = {'rabbit': [1,2,3],
               'lioness': [6,8,9],
               'kitten': [2,2,6]
               }
n = 6

fn = value_containing_key(sample_dict, n)

print(fn)


'''
################### Sample Solution ###################
def _return_keys_list_sample_(sample_dictionary, sample_value):
    keys_list = []
    for each_key in sample_dictionary.keys():
        if sample_value in sample_dictionary[each_key]:
             keys_list.append(each_key)
    keys_list.sort()
    return keys_list
'''
