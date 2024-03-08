"""
Practice With Strings. Part 2
Write a function that takes a string and an integer number, n, as input arguments and returns the number of n
letter word in that string
"""

# Define Function
def find_n_letter_word(s,n):

    words = s.split()               # Function split() converts a string into a list
    n_letter_words = 0
    for w in words:
        if len(w) == n:
            n_letter_words = n_letter_words + 1

    return n_letter_words


# Main Program
input_string = 'He who would learn to fly one day'
total_words = 0
#k = 5     # Number of characters in a word
for k in range(1,11):

    x = find_n_letter_word(input_string, k)
    total_words = total_words + x
    print('There are', x, 'words with', k,'characters')
print('¨¨¨¨¨\nThere are a total of', total_words, 'words in the string')

