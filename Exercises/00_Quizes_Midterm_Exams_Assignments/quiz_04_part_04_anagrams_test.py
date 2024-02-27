'''
Quiz 4, Part 4 (Anagrams Test)
Write a function named test_for_anagrams that receives two strings as parameters, both of which consist of alphabetic
characters and returns True if the two strings are anagrams, False otherwise. Two strings are anagrams if one string
can be constructed by rearranging the characters in the other string using all the characters in the original string
exactly once. For example, the strings "Orchestra" and "Carthorse" are anagrams because each one can be constructed
by rearranging the characters in the other one using all the characters in one of them exactly once. Note that
capitalization does not matter here i.e. a lower case character can be considered the same as an upper case character
'''
# Define Function
def test_for_anagrams(s1, s2):

    s1, s2 = sorted(s1.lower()), sorted(s2.lower())

    if s1 == s2:
        return True
    else:
        return False


# Main Program
str_1 = 'Orchestra'
str_2 = 'Carthorse'

fn = test_for_anagrams(str_1, str_2)
print(fn)



'''
################### Instructor function ###################
def _are_anagrams_sample_(sample_string1, sample_string2):
    if sorted(sample_string1.lower()) == sorted(sample_string2.lower()):
        return True
    else:
        return False
'''




























