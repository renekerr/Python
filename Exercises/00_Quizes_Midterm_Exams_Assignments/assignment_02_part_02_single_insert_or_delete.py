"""
Part 2: Find single insertion or deletion

Write a function named single_insert_or_delete that accepts two strings as input arguments and returns:

0 if the two strings match exactly.
1 if the first string can become the same as the second string by inserting or deleting a single character.
  Notice that inserting and deleting a character is not the same as replacing a character.
2 otherwise


Capital letters are considered the same as lower case letters. Here are some examples:
First string	Second String	Function return
Python	            Java	            2
book	            boot	            2
dog	                Dog	                0

sin	                sink	            1 (Inserting a single character at the end)
poke	            spoke	            1 (Inserting a single character at the start)
poker	            poke	            1 (Deleting a single character from the end)
programing	        programming	        1 (Inserting a single character)

"""

# This is my approach
# Define Function

def single_insert_or_delete(s1,s2):

    s1, s2 = s1.lower(), s2.lower()

    if s1 == s2:
        return 0

    if s1 == s2[0:-1:] or s1 == s2[1::] or s1[0:-1:] == s2 or len(s1) == len(s2)-1:
        return 1

    if len(s1) != len(s2):
        return 2

    if len(s1) == len(s2):

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return 2

# Main Program
string_1 = 'programing'
string_2 = 'programming'
#print(string_1, string_2)

fn = single_insert_or_delete(string_1, string_2)

print('result = ',fn)

