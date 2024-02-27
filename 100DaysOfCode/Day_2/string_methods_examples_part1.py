"""
String Methods With Examples

Like many of Python's built-in types, strings have a number of powerful and useful methods.
In this page, we will provide examples of how some of them can be used.

***Remember: square brackets indicate optional arguments.***
"""

# For a more elaborate list of String Methods
# https://docs.python.org/3/library/stdtypes.html#string-methods

# str.capitalize( )     This method returns a copy of the first character capitalized and the rest lower-cased.
print('Example_1')
my_string = "sTrInG mEtHoDs"                # Create a string
new_string = my_string.capitalize()         # Capitalize 1st, lower rest & return
print(new_string,'\n')


# str.casefold( )
# This method returns a casefolded copy of the string. Casefolded strings may be used for caseless matching.
# Casefolding is similar to lowercasing but more aggressive because it is intended to remove all case
# distinctions in a string.
print('Example_2')
my_string = "sTrInG mEtHoDs"               # Create a String
new_string = my_string.casefold()          # Return a casefolded copy
print(new_string, '\n')


# str.center(width[, fillchar])      This method returns a centered in a string of length width.
# Padding is done using the specified fillchar (default is an ASCII space).
# The original string is returned if width is less than or equal to len(s).
print('Example_3')
my_string = "sTrInG mEtHoDs"               # Create a String
new_string = my_string.center(20, 'x')     # Center in 20 spaces, fill spaces with 'x' & return
print(new_string, '\n')


# str.count(sub[, start[, end]])     This method returns the number of non-overlapping occurrences of substring sub
# in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.
print('Example_4')
my_string = "this is python. It is awesome!"     # Create a String
my_count = my_string.count('is', 0, -1)          # count occurrences of'is' and return
print(my_count, '\n')


# str.endswith(suffix[, start[, end]])        This method returns True if the string ends with the specified suffix,
# otherwise returns False. suffix can also be a tuple of suffixes to look for.
# With optional start, test beginning at that position.
# With optional end, stop comparing at that position.
print('Example_5')
my_string = "we love python"              # Create a String
my_value = my_string.endswith('python')   # Return a boolean
print(my_value, '\n')


# str.find(sub[, start[, end]])        This method returns the lowest index in the string where substring sub
# is found such that sub is contained in the slice s[start:end].
# Optional arguments start and end are interpreted as in slice notation.
# This method returns -1 if sub is not found.
print('Example_6')
my_string = "we love python"        # Create a String
my_index = my_string.find('o')      # Return the lowest index where substring was found
print(my_index, '\n')


# str.format(*args, **kwargs)       This method performs a string formatting operation.
# The string on which this method is called can contain literal text or replacement
# fields delimited by braces {}. Each replacement field contains either the numeric index of a
# positional argument, or the name of a keyword argument. It returns a copy of the string where each
# replacement field is replaced with the string value of the corresponding argument.
print('Example_7')
a = 10
b = 30
my_sum = a + b
my_product = a * b
print("The sum of a and b is {0} and their product is {1}".format(my_sum, a*b), '\n')

# str.index(sub[, start[, end]])        This method returns the lowest index in the string where substring sub
# is found such that sub is contained in the slice s[start:end].
# Optional arguments start and end are interpreted as in slice notation.
# This method is very similar to str.find except it raises a ValueError if the substring is not found.
print('Example_8')
my_string = "we love python"        # Create a String
my_index = my_string.index('py')     # Return lowest index at which the substring was found
print(my_index, '\n')                     # Check to see what was returned


# str.isalnum()     This method returns True if all the characters in the string are alphanumeric
# and there is at least one character, False otherwise.
print('Example_9')
my_string_1 = "StarWars2016"              # Notice there is no space
my_string_2 = "I love star wars 2016"     # This string contains spaces
check_1 = my_string_1.isalnum()           # Returns a Boolean value
check_2 = my_string_2.isalnum()           # Returns a Boolean value
print("check_1 is: {0} and check_2 is: {1}".format(check_1, check_2))   # Check to see what was returned

"""
*** Several other methods that are similar to str.isalnum() which return some Boolean value are as following:***

str.isalpha()
Return True if all characters in the string are alphabetic and there is at least one character, False otherwise.
Alphabetic characters are those characters defined in the Unicode character database as “Letter”


str.isdecimal()
Return True if all characters in the string are decimal characters and there is at least one character,
False otherwise. Decimal characters are those from general category “Nd”. This category includes digit characters,
and all characters that can be used to form decimal-radix numbers, e.g. U+0660, ARABIC-INDIC DIGIT ZERO.

str.isdigit()
Return True if all characters in the string are digits and there is at least one character,
False otherwise. Digits include decimal characters and digits that need special handling, such as
the compatibility superscript digits. Formally, a digit is a character that has the property value
Numeric_Type=Digit or Numeric_Type=Decimal.

str.isidentifier()
Return True if the string is a valid identifier according to the language definition, section
Identifiers and Keywords.

str.islower()
Return True if all cased characters in the string are lowercase and there is at least one cased character,
False otherwise.

str.isnumeric()
Return True if all characters in the string are numeric characters, and there is at least one character,
False otherwise. Numeric characters include digit characters,
and all characters that have the Unicode numeric value property

str.isprintable()
Return True if all characters in the string are printable or the string is empty,
False otherwise. Nonprintable characters are those characters defined in the Unicode character database as
“Other” or “Separator”, excepting the ASCII space (0x20) which is considered printable.

str.isspace()
Return True if there are only whitespace characters in the string and there is at least one character,
False otherwise. Whitespace characters are those characters defined in the Unicode character database as
“Other” or “Separator” and those with bidirectional property being one of “WS”, “B”, or “S”.

str.istitle()
Return True if the string is a titlecased string and there is at least one character, for example
uppercase characters may only follow uncased characters and lowercase characters only cased ones.
Return False otherwise.

str.isupper()
Return True if all cased characters in the string are uppercase and there is at least one cased character,
False otherwise
"""