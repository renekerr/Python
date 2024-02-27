"""
Part 2: Find single insertion or deletion

Write a function named single_insert_or_delete that accepts two strings as input arguments and returns:

0 if the two strings match exactly.
1 if the first string can become the same as the second string by inserting or deleting a single character.
  Notice that inserting and deleting a character is not the same as replacing a character.
2 otherwise


Capital letters are considered the same as lower case letters. Here are some examples:

First string	Second String	Function return
¨¨¨¨¨¨¨¨¨¨¨¨    ¨¨¨¨¨¨¨¨¨¨¨¨¨   ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
dog	                Dog	                0

Python	            Java	            2

book	            boot	            2


sin	                sink	            1 (Inserting a single character at the end)
poke	            spoke	            1 (Inserting a single character at the start)
poker	            poke	            1 (Deleting a single character from the end)
programing	        programming	        1 (Inserting a single character)

"""

# Define Function
def single_insert_or_delete(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()

    if s1 == s2:
        return 0

    if abs(len(s1) - len(s2)) != 1:
        return 2

    if len(s1) > len(s2):
        # s1 is greater, only deletion is possible
        for k in range(len(s2)):
            if s1[k] != s2[k]:
                if s1[k + 1:] == s2[k:]:
                    return 1
                else:
                    return 2
        return 1

    else:
        # s1 is shorter, only insertion is possible
        for k in range(len(s1)):
            if s1[k] != s2[k]:
                if s1[k:] == s2[k + 1:]:
                    return 1
                else:
                    return 2
        return 1


# Main Program
string_1 = 'python'
string_2 = 'java'
fn = single_insert_or_delete(string_1, string_2)

print(fn)


"""
################### Instructor function ###################
def _instructor_function (s1,s2):
    s1=s1.lower()
    s2=s2.lower()

    if s1==s2:
        return 0

    if abs(len(s1)-len(s2))!=1:
        return 2

    if len(s1)>len(s2):
        # only deletion is possible
        for k in range(len(s2)):
            if s1[k]!=s2[k]:
                if s1[k+1:]==s2[k:]:
                    return 1
                else:
                    return 2
        return 1
    else: # s1 is shorter Only insertion is possible
        for k in range(len(s1)):
            if s1[k]!=s2[k]:
                if s1[k:]==s2[k+1:]:
                    return 1
                else:
                    return 2
        return 1
"""




