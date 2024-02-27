"""
String Methods With Examples Continued

In this page we will continue to provide examples of how some more of the string methods can be used.

***Remember: square brackets indicate optional arguments.***
"""
# For a more elaborate list of String Methods
# https://docs.python.org/3/library/stdtypes.html#string-methods


# str.join(iterable )
# This method returns a string which is the concatenation of the strings in the iterable.
# A TypeError will be raised if there are any non-strings values in iterable, including bytes objects.
# The separator between elements is the string providing this method.
print('Example_1')
sign = "@"
my_list = ["One", "Two", "Three", "Four"]
new_string = sign.join(my_list)
print(new_string, '\n')

# str.ljust(width[, fillchar])
# This method returns the string left justified in a string of length width.
# Padding is done using the specified fillchar (default  is an ASCII space).
# The original string is returned if width is less than or equal to len(s).
print('Example_2')
my_string = "unjustified text"  # Create a String
new_string = my_string.ljust(2 * len(my_string), "X")  # left justify, fit within 2*len of string, fill with X
print(new_string, '\n')

# str.lower()       This method returns a copy of the string with all the cased characters converted to lowercase.
print('Example_3')
my_string = "sTrInG mEtHoDs"  # Create a String
new_string = my_string.lower()  # Return the lowercased string
print(new_string, '\n')  # Check to see what was returned

# str.lstrip([chars])
# This method returns a copy of the string with leading characters removed.
# The chars argument is a string specifying the set of characters to be removed.
# If omitted or None, the Chars argument defaults to removing whitespace. The chars argument is not a prefix;
# rather all combinations of its values are stripped.
print('Example_4')
my_string = "   python is fun"  # Notices the whitespaces
new_string = my_string.lstrip()  # strip leading characters & return
print(new_string, '\n')  # Check to see what was returned

# str.replace(old, new[, count])
# This method returns a copy of the string with all occurrences of substring old replaced by new.
# If the optional argument count is given, only the first count occurrences are replaced.
print('Example_5')
my_string = "we love python very very much"  # Notice there are five spaces in the string
new_string = my_string.replace(" ", "X", 3)  # Replace first 3 white spaces with 'Z' & return
print(new_string, '\n')  # Check to see what was returned

# str.rfind(sub[, start[, end]])
# This method returns the highest index in the string where substring sub is found such that sub is
# contained in the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation.
# This method returns -1 if sub is not found.
print('Example_6')
my_string = "we love python"  # Create a String
my_index = my_string.rfind('o')  # Return the highest index at which the substring was found
print(my_index, '\n')  # Check to see what was returned


# str.rindex(sub[, start[, end]])
# This method performs like rfind() but raises ValueError when the substring sub is not found.

# str.split(sep=None, maxsplit=-1)
# This method returns a list of the words in the string, using sep as the delimiter string.
# If maxsplit is given, at most maxsplit splits are done.
# If maxsplit is not specified or -1, then there is no limit on the number of splits.
print('Example_7')
my_string = "1,3,5,7,9,11"         # Notice that the numbers here are separated by commas
my_list = my_string.split(',')     # Return a list, split using comma as delimiter
print(my_list, '\n')


# str.strip([chars])
# This method returns a copy of the string with the leading and trailing characters removed.
# The chars argument is a string specifying the set of characters to be removed.
# If omitted or None, the chars argument defaults to removing whitespace.
# The char argument is not a prefix or a suffix; rather, all combinations of its values are stripped.
print('Example_8')
my_string = "    https://docs.python.org/3/     "    # Notice the white spaces in the string
new_string = my_string.strip()                       # Remove all leading & trailing characters & return
print(new_string, '\n')

# For a more elaborate list of String Methods
# https://docs.python.org/3/library/stdtypes.html#string-methods