"""
String slicing 
str_object[start_pos:end_pos:step]

    start_pos: is the starting index of the slice (inclusive). If not specified, it takes the start of the variable.
    end_pos: is the ending index of the slice (exclusive). If not specified, it takes the end of the variable.
    step: is the step size. If specified as a negative value, the slice is returned in reverse order.

    a[start:stop]  # items start through stop-1
    a[start:]      # items start through the rest of the array
    a[:stop]       # items from the beginning through stop-1
    a[:]           # a copy of the whole array

+ info : https://stackoverflow.com/questions/509211/how-slicing-in-python-works

Index slicing
starting from front	  
             0    1    2    3    4    5    6
					+----+----+----+----+----+----+----+							
					| E  |  n |  g | l  |  i | s  |  h |
					+----+----+----+----+----+----+----+							
					  -7   -6   -5   -4   -3   -2   -1  starting from rear

"""

# Single line comment
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I am enjoying learning Python"
print(sentence)

# Multiline String
multiline_string = '''I am currently working as a DBA.
Enjoying learing how to program using Python.'''
print(multiline_string)

# String Concatenation
first_name = 'Rene'
last_name = 'Kerr'
space = ' '
full_name = first_name  +  space + last_name
print('This is my full name: ', full_name) 
# Checking length of a string using len() builtin function
print('Lenght of first_name = ',len(first_name))  # 8
print('Lenght of last_name = ',len(last_name))   # 7
print('Lenght of first_name > lenght of last_name = ',len(first_name) > len(last_name)) # True
print('Lenght of full_name = ',len(full_name)) # 15

#### Unpacking characters 
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n

# Accessing characters in strings by index
language = 'Javascript'
first_letter = language[0]
print(first_letter) # J
second_letter = language[1]
print(second_letter) # a
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # t


# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Javascript'
four_first = language[0:4]
print(four_first) # Java
last_letter = language[-1]
print(last_letter) # t
second_last = language[-2]
print(second_last) # p


# Slicing
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Skipping character while splitting Python strings
language = 'Python'
pto = language[0:6:2] # 
print(pto) # pto

# Escape sequence
print('I am studying German.\nDo you speak French?') # line break
print('Country\tLanguage\t')
print('Spain\tSpanish\t')
print('This is a back slash  symbol (\\)') # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')


## String Methods
# capitalize(): Converts the first character the string to Capital Letter

challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 2`

# endswith(): Checks if a string ends with a specified ending

challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

# find(): Returns the index of first occurrence of substring

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# format()	formats string into nicer output    
first_name = 'R'
last_name = 'K'
job = 'DBA'
country = 'Spain'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence) 

radius = 10
pi = 3.14
area = pi # radius ## 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result) # The area of circle with 10 is 314.0

# index(): Returns the index of substring
challenge = 'thirty days of python'
print(challenge.index('y'))  # 5
print(challenge.index('th')) # 0

# isalnum(): Checks alphanumeric character

challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

# isalpha(): Checks if all characters are alphabets

challenge = 'thirty days of python'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

# isdigit(): Checks Digit Characters

challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True

# isdecimal():Checks decimal characters

num = '10'
print(num.isdecimal()) # True
num = '10.5'
print(num.isdecimal()) # False


# isidentifier():Checks for valid identifier means it check if a string is a valid variable name

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True


# islower():Checks if all alphabets in a string are lowercase

challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

# isupper(): returns if all characters are uppercase characters

challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True


# isnumeric():Checks numeric characters

num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False

# join(): Returns a concatenated string

web_tech = ['SQL', 'Linux', 'Snowflake', 'Powershell']
result = '#, '.join(web_tech)
print(result)


original_list = ['CSS', 'HTML']
modified_list = ['#' + element for element in original_list]
print(modified_list)


original_list = ['CSS', 'HTML']
modified_list = []
for element in original_list:
    modified_list.append(element +'#')
print(modified_list)



# strip(): Removes both leading and trailing characters
challenge = ' thirty days of python '
print(challenge.strip())


# replace(): Replaces substring inside
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# split():Splits String
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']

# title(): Returns a Title Cased String
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

# swapcase(): Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False


# Strings 
var_string_00 = 'Javascript'
var_string_01 = 'German'

print(len(var_string_00))
print(len((var_string_01)))

print(var_string_00 + " & " + var_string_01, ", both are languages!")

# Line breaks
line_breaks_00 = "This is an example of\na line break"
print(line_breaks_00)

tab_string_00 = "\tThis is an example of a tabulated line"
print(tab_string_00)

scape_string_00 = "\\This is an example of string scaped\\"
print(scape_string_00)


## Testing.....
 # Formatting strings
"""
In Python there are many ways of formatting strings. In this section, we will cover some of them. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s", "%d", "%f", "%.number of digitsf".

%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision
"""
name, surname, age = 'Jon', 'Doe', 65
print('--- Info ---')
print('Name =', name)
print('Surname =', surname)
print('Age =', age)
print('My name is', name, surname, 'and I am', age , 'years old')
print('My name is {} {} and I am {} years old'.format(name, surname, age))
print('My name is %s %s and I am %d years old' %(name, surname, age))
print(f'My name is {name} {surname} and I am {age} years old') # inferencia de detos 

# Slicing strings
ones_language = "Python"
lang_slice = ones_language[1:3]
print(lang_slice) # yt

lang_slice = ones_language[1:]
print(lang_slice) # ython

lang_slice = ones_language[-2]
print(lang_slice) # o

lang_slice = ones_language[0:6:2]
print(lang_slice) # o

# String reversed
reversed_language = ones_language[::-1]
print(reversed_language) # nohtyP

# Some functions
print(ones_language.capitalize())
print(ones_language.upper())
print(ones_language.count('y'))
print(ones_language.lower())
print(ones_language.lower().isupper())
print(ones_language.startswith('Py'))
print(ones_language.startswith('py'))
print('Py' == 'py') # False


language = 'English'
print(language[::])
print(language[1::])
print(language[2::])  
print(language[3::])   
print(language[0:3:])   
print(language[0:4:])   
print(language[0:4:1])  
print(language[0:4:2])  
print(language[0:4:3]) 
print(language[2:5])
print(language[3]) 
print(language[-4])
print(language[3:5])
print(language[-4:-2])
print(language[-4:])
print(language[3:])

listOne  =  ['a', 'b', 'c', 'd']
listTwo =  ['e', 'f', 'g']

new_list = listOne + listTwo

print(new_list)


listOne  =  ['a', 'b', 'c', 'd']
listTwo =  ['e', 'f', 'g']

new_list = listOne + listTwo
print(new_list)     #['a', 'b', 'c', 'd', 'e', 'f', 'g']

sampleList = [10, 20, 30, 40]
del sampleList[0:6] #[]
print(sampleList)

l = [None] * 10
print(len(l))   #10

list_a = ['a', 'b', 'c', 'd']
new_list = list_a.copy()
print(new_list)

fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.insert(1, "lemon")
print(fruits)




