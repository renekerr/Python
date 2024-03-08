"""
CHARACTER ENCODING
Each character is given a unique number (code) so it can be stored
in a computer memory

There are many character encoding standards such as:

ASCII (American Standard Code for Information Interchange)
UTF-8   (8-bit Unicode Transformation Format)
UTF-16  (16-bit Unicode Transformation Format)
UTF-32  (32-bit Unicode Transformation Format)

UTF-8
UTF-8 is the main character encoding for the web and simple English text but it can also contain
any unicode character (1.112.064 characters can be represented)

UTF-8 is using 1 to 4 bytes to encode each character. The first 128 characters of UTF-8 are encoded
using 1 byte with the same binary value as ASCII.

UTF-8  is recommended as the default encoding for web pages (in HTML and XML)

There are two functions which are useful to convert from a character to a number and from a
number to a character

ord() takes a character and returns its UTF-8 integer value
chr() takes an integer and returns the UTF-8 character
"""

# Example1
print(ord('a'))
print(ord('S'))

# Example2
print(chr(97))
print(ord("2"))

# Example3
s = ''
for k in range(20000, 20201):
    s = s + chr(k)
print(s, '\n')

# Example4
# Escape sequences
print('Hello \nHow are you doing?')
print('He said \"Hi\"')


