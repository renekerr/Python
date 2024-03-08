'''
Dictionary Exercise 7 (Dictionary of Word Count)

Write a function that takes a string of words as input argument and returns a dictionary of word counts.
The keys of this dictionary should be the unique words and the values should be the total count of those words.
Assume that characters are not case sensitive. For example if the input string is :

"I am tall when I am young and I am short when I am old"
Then the output should be:
{'short': 1, 'young': 1, 'am': 4, 'when': 2, 'tall': 1, 'i': 4, 'and': 1, 'old': 1}
'''

# Define Function(s)
def dict_word_count(sample_str):

    s = sample_str.lower().split()   # split() to convert a string into a list
    output_dict = {}

    for words in s:
        output_dict[words] = s.count(words)

    return output_dict

# Main Program
sample_string = 'I am tall when I am young and I am short when I am old'
fn = dict_word_count(sample_string)

print(fn)

'''
################### Sample Solution ###################
def _dictionary_of_word_counts_sample_(sample_string):
    lowered_splitted_string = sample_string.lower().split()
    sample_dictionary = {}
    for word in lowered_splitted_string:
        sample_dictionary[word] = lowered_splitted_string.count(word)
    return sample_dictionary
'''
