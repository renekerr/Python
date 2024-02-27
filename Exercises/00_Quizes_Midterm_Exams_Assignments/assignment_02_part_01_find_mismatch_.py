"""
Part 1: Find mismatch
Write a function named find_mismatch that accepts two strings as input arguments and returns:

0 if the two strings match exactly.
1 if the two strings have the same length and mismatch in only one character.
2 if the two strings do not have the same length or mismatch in two or more characters.

Capital letters are considered the same as lower case letters. Here are some examples:

First string	    Second String	    Function return
¨¨¨¨¨¨¨¨¨¨¨¨        ¨¨¨¨¨¨¨¨¨¨¨¨¨       ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
Python	                Java	            2
Hello There	        helloothere	            1
sin	                    sink	            2 (note not the same length)
dog	                    Dog	                0
"""

"""
This is the instructor solution

def find_mismatch(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    mismatch = 0                            # Set mismatch to 0
                                            # If two strings match exactly 0 will be displayed

    if len(s1) != len(s2):                  # If strings lengths are not the same
        return 2                            # Function will return 2

    for i, elem in enumerate(s1):           # Using function enumerate() and a for loop to iterate any string

        if s1[i] != s2[i]:                  # Check if there is any character mismatch

            mismatch = mismatch + 1         # If so, then count it

            if mismatch > 1:                # In case number of mismatch is greater than 1
                return 2                    # Function will return 2

    return mismatch
"""

# This is my approach
def find_mismatch(s1,s2):
    s1, s2 = s1.lower(), s2.lower()
    m = 0

    for k, elem in enumerate(s1):

        if s1[k] != s2[k]:
            m += 1

            if m == 1 and len(s1) == len(s2):
                return 1
            else:
                return 2

    if len(s1) != len(s2):
        return 2

    return m

# Main Program
input_str1 = 'sin'
input_str2 = 'sink'
#fn = find_mismatch(input_str1, input_str2)
fn = find_mismatch(input_str1, input_str2)

print(fn)