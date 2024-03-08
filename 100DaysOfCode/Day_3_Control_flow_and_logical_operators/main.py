'''
Day 3 - Beginner - Control Flow and Logical Operators
'''


'''
OPERATORS
                                   

https://github.com/Asabeneh/30-Days-Of-Python/blob/master/03_Day_Operators/03_operators.md#-exercises---day-3
'''
age = 45
height = 1.95
n = 2 + 1j  # variable that store a complex number

'''
Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
'''
print('Area of a triangle')
b = int(input('Enter the base : '))
h = int(input('Enter height: '))
area = 0.5 * b * h
print(f'The area of the triangle is {area}\n')


'''
Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
'''
print('Calculating the perimeter of a triangle')
side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('enter side c: '))
perimeter = side_a + side_b + side_c
print(f'The perimeter of the triangle is {perimeter}\n')

'''
Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width)
'''
print('Calculating the area and perimeter of a rectangle ')
l = float(input('Enter the length: '))
w = float(input('Enter the width: '))

a = l * w
p = 2 * (l + w)

print(f'The area of the rectangle is {a}')
print(f'The perimeter of the rectangle is {p}\n')

'''
Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
'''

print('Calculating the area and circumference orf a circle')
r = float(input('Enter the radius: '))
pi = 3.14

a = round(pi * r * r, 2)
c = round(2 * pi * r, 2) 

print(f'The area is {a} and the circumference is {c}\n')

'''
Calculate the slope, x-intercept and y-intercept of y = 2x -2
'''
print('Calculating the slope, x-intercept and y-intercept of y = 2x -2')
# Equation: y = 2x - 2
# Slope (m) is the coefficient of x
slope = 2

# The equation is in the form y = mx + b, where b is the y-intercept
y_intercept = -2

# To find the x-intercept, set y to 0 and solve for x
# 0 = 2x - 2  =>  2x = 2  =>  x = 1
y = 0
x = (y + 2)/2
x_intercept = x

print("slope:", slope)
print("y-intercept:", y_intercept)
print("x-intercept:", x_intercept)

'''
Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
'''
x1, y1 = 2, 2
x2, y2 = 6, 100

# Calculate slope using the formula (m = (y2 - y1) / (x2 - x1))
slope = (y2 - y1)/(x2 -x1)

# Calculate Euclidean distance between two points
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print('The slope between is equal to ', slope)
print('The Euclidean distance between two points is equal to ', round(distance, 2), '\n')   


'''
Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0
'''
print('Calculating y (y = x^2 + 6x + 9)') 
x = float(input('Enter the value of x : '))
y = x**2 + (6*x) + 9

print(f'When x = {x}, y = {y}\n')

'''
Find the length of 'python' and 'dragon' and make a falsy comparison statement.
Use and operator to check if 'on' is found in both 'python' and 'dragon'
I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
There is no 'on' in both dragon and python
Find the length of the text python and convert the value to float and convert it to string
'''
a = 'python'
b = 'dragon'
x = 'on'

d = 'I hope this course is not full of jargon.'
y = 'jargon'

len_a = len(a)
len_b = len(b)

flt = float(len_a)
t1 = type(flt)
str_flt = str(flt)
t2 = type(str_flt)

x_in_a = x in a
x_in_b = x in b
y_in_d = y in d

if  len_a == len_b: 
    print(f"Length of '{a}' and '{b}' are the same.")
else: 
    print(f"Length of '{a}' and '{b}' are different.")

print(f"Is '{x}' found in '{a}'? {x_in_a}")
print(f"Is '{x}' found in '{b}'? {x_in_b}")
print(f"Is '{y}' found in the sentence :'{d}'? {y_in_d}")

print(f"Length of '{a}' converted to 'float' is {flt}")
print(f"type() of variable '{flt}' is {t1}")
print(f"This is the value of '{flt}' converted to a string: {str_flt}")
print(f"type() of variable '{str_flt}' is {t2}")


'''
Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
Check if type of '10' is equal to type of 10
'''

# Which number do you want to check?
number = int(input('Which number do you want to check?'))
if (number % 2) == 0:
  print('This is an even number.')
else: 
  print('This is an odd number.')

a = '10'
b = 10

type_a = type(a)
type_b = type(b)

if type_a == type_b: 
  print(f"type() of variable 'a' and 'b' are the same.")  
else:
  print(f"type() of variable 'a' and 'b' are NOT the same.")

print(f'type(a) is {type_a}')
print(f'type(b) is {type_b}')

'''
Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
'''
hours = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hours: '))

weekly_earning = hours * rate_per_hour
print('Your weekly earing is ', weekly_earning)



'''
Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

1 hour      = 60 minutes 

1 minute    = 60 seconds
60 minutes  = 3600 seconds

1 hour      = 3600 seconds
24 hours    = 86400 seconds

then 
1 day       = 86400 seconds

'''
days_in_a_year = 365
seconds_in_a_day = 86400
years_lived = int(input('Enter number of years you have lived: '))
seconds_lived  = years_lived * days_in_a_year * seconds_in_a_day

print(f'You have lived for {seconds_lived} seconds.')



'''


  __ ___ _  ___       __  __ 
 (_   | |_)  |  |\ | /__ (_  
 __)  | | \ _|_ | \| \_| __) 
                             



https://github.com/Asabeneh/30-Days-Of-Python/blob/master/04_Day_Strings/04_strings.md#-exercises---day-4

'''

'''
Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
Declare a variable named company and assign it to an initial value "Coding For All".
Print the variable company using print().
Print the length of the company string using len() method and print().
Change all the characters to uppercase letters using upper() method.
Change all the characters to lowercase letters using lower() method.
Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
'''

a = '100 Days'
b = 'Of'
c = 'Coding in'
d = 'Python'
x = a + ' ' + b + ' ' + c + ' ' + d 
print(a, b, c, d)
print(x, '\n')

# Multiline string
multiline_string = '''I am new to Python.
Python is a very powerful programming language.
I am following #100DaysOfPython course.'''
print(multiline_string, '\n')

# Another way of doing the same thing
multiline_string = """I am new to Python.
Python is a very powerful programming language.
I am following #100DaysOfPython course"""
print(multiline_string,'\n')

# Escape Sequences in Strings
'''
In Python and other programming languages \ followed by a character is an escape sequence. Let us see the most common escape characters:

\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")
'''

# Examples
print('This is an example of scaping in Python.\nThis sentence will appear in a new line.')
print('My hobbies are: ')
print('\t-Reading')
print('\t-Photography')
print('\t-Travel')
print('This is a backslash  symbol (\\)') # To write a backslash


# String formatting
'''
OLD Style String Formatting (% Operator)

%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision

NEW Style String Formatting (str.format)

'''

# Old style

country = 'Spain'
city = 'Madrid'
job = 'DBA'
years_living_here = 20
avrg_temp_summer = 30.5
print('OLD Style String Formatting (% Operator)')
formatted_string = 'I live in %s, %s and I work as a %s.\nI have been living here for %d years.\nThe average temperature in summer is %f (more precisely %.1f). It is very hot.\n' %(city, country, job, years_living_here, avrg_temp_summer, avrg_temp_summer)

'''
Or use the print() function directly: 
print('I live in %s, %s and I work as a %s.\nI have been living here for %d years.\nThe average temperature in summer is %f (more precisely %.1f). It is very hot.\n' %(city, country, job, years_living_here, avrg_temp_summer, avrg_temp_summer))

'''
print(formatted_string)


# New style
print('NEW Style String Formatting (str.format, introduced in Python version 3.)')
new_format = 'I live in {}, {}.'.format(city, country)
print(new_format)
print('I live in {}, {}.'.format(city, country)) # Or use the print() function directly

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a+b))
print('{} - {} = {}'.format(a, b, a-b))
print('{} * {} = {}'.format(a, b, a*b))
print('{} / {} = {}'.format(a, b, a/b))
print('{} / {} = {:.2f}\n'.format(a, b, a/b)) # limits it to two digits after decimal

# String Interpolation / f-Strings (Python 3.6+)
# Another new string formatting is string interpolation, f-strings. Strings start with f and we can inject the data in their corresponding positions.

print('String Interpolation / F-STRINGS (Python 3.6+)')
c = 4
d = 3
print(f'{c} + {d} = {c+d}')
print(f'{c} - {d} = {c-d}')
print(f'{c} * {d} = {c*d}')
print(f'{c} / {d} = {c/d}')
print(f'{c} / {d} = {c/d:.2f}\n') # limits it to two digits after decimal


company = 'Coding for All'
len_company = len(company)
print(company)
print(f"Lenght of '{company}' is {len_company}.\n")

company = 'Coding for All'
company_uppercase = company.upper()
company_lowercase = company.lower()
company_capitalize = company.capitalize()
company_title = company.title()
company_swapcase = company.swapcase()
slicing_one = company[0:6]

print('Upppercased : ', company_uppercase)
print('Lowecased : ', company_lowercase)
print('Capitalized : ', company_capitalize)
print('Titled : ', company_title)
print('Swapped : ', company_swapcase)
print('Sliced one: ', slicing_one)


'''
Check if Coding For All string contains a word Coding using the method index, find or other methods.
Replace the word coding in the string 'Coding For All' to Python.
Change Python for Everyone to Python for All using the replace method or other methods.
'''

# Unpacking characters
city = 'Madrid'
a,b,c,d,e,f = city
print(f"Unpacking '{city}'")
print(a)
print(b)
print(c)
print(d)
print(e)
print(f, '\n')

x = 'Coding for all'

w = x[:6]
z = w in x

sub_str = 'Coding'
fnd_str = x.index(sub_str)

print(f"Is the word '{w}' in the sentence '{x}'? {z}\n")
print(fnd_str)

# Slicing
k = 'Madrid'
l = len(k)
print(f"City: '{k}'")
print(f'Length of {k} is {l}\n')
first_three = k[0:3]
print('First three characters in sentence: ', first_three)
last_three_one = k[3:6]
print('Last three characters in sentence: ', last_three_one)
last_three_two = k[-3:]
print('Last three characters in sentence: ', last_three_two)
last_three_three = k[3:]
print('Last three characters in sentence: ', last_three_three, '\n')

# Reversing a String
rev = k[::-1]
print(f"'{k}' reversed is '{rev}'") # dirdaM

# Skipping characters
skip_char = k[0:6:2]
print(f"Skipping two characters in '{k}' : {skip_char}\n")

# Replacing string
x = 'Coding for all'
j = x[0:6]
str_to_change = 'Learning'
new_string = x.replace(j, str_to_change)
another_string = x.replace('all', 'you')
print(f"Replacing '{j}' with '{str_to_change}' in '{x}': {new_string}")
print(another_string)

'''
Split the string 'Coding For All' using space as the separator (split()) .
"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
What is the character at index 0 in the string Coding For All.
What is the last index of the string Coding For All.
What character is at index 10 in "Coding For All" string.
'''

# split() 
x = 'Coding for all'
fav_serie = 'True Detective'
print(fav_serie.split())
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))

print(f"Character at index 0 in '{x}' is {x[0]}")
print(f"Last character in '{x}' is {x[-1]}")
print(f"Character 10 in '{x}' is {x[9]}")


'''
Create an acronym or an abbreviation for the name 'Python For Everyone'.
Create an acronym or an abbreviation for the name 'Coding For All'.
Use index to determine the position of the first occurrence of C in Coding For All.
Use index to determine the position of the first occurrence of F in Coding For All.
Use rfind to determine the position of the last occurrence of l in Coding For All People.
'''

text_one = 'Python For Everyone'
accronym_one =  text_one[0] + text_one[7] + text_one[11]
text_two = 'Coding For All People'
accronym_two = text_two[0] + text_two[7] + text_two[11]

print(accronym_one)
print(accronym_two)

print(f"First occurrence of C in '{text_two}' is {text_two.index('C')}")
      
print(f"First occurrence of F in '{text_two}' is {text_two.index('F')}")

print(f"Last occurrence of l in '{text_two}' is {text_two.rindex('l')}")

'''
Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
'''

sentence = 'You cannot end a sentence with because because because is a conjunction'
word = 'because'
print(f"The first ocurrence of '{word}' in '{sentence}' is {sentence.index(word)}.")
print(f"The last ocurrence of the word '{word}' in '{sentence}' is {sentence.rindex(word)}.'")

phrase_to_slice = 'because because because'
start_index = sentence.index(phrase_to_slice)

# Slice out the phrase from the sentence
result = sentence[start_index:start_index + len(phrase_to_slice)]

print(result)

'''
Does ''Coding For All' start with a substring Coding?
Does 'Coding For All' end with a substring coding?
'''

text_two = 'Coding For All People'
word = 'Coding'
yes_no = text_two.startswith(word)
print(f"Does '{text_two}' starts with '{word}'? {yes_no}")

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
text_three = '   ...Coding For All...      ' 
result = text_three.strip()

print(result)

'''
Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python
'''

a = '30DaysOfPython'
b = 'thirty_days_of_python'
print(f"Is '{a}' a valid identifier? {a.isidentifier()}")
print(f"Is '{b}' a valid identifier? {b.isidentifier()}")

'''
The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string
'''

libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(libs)

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

'''
Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next.
'''

print("I am enjoying this challenge.\nI just wonder what is next.")

'''
Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
'''
print('Name\tAge\tCountry\tCity')
print('Rene\t20\tSpain\tMadrid') 


'''
Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
'''

radius = 10
area = 3.14 * radius ** 2

print(f'Teh area of a circle with radio {radius} is {area:.0f} meters square.')

'''
Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
'''

x = 8
y = 6

print(f'{x} + {y} = {x+y}')
print(f'{x} - {y} = {x-y}')
print(f'{x} * {y} = {x*y}')
print(f'{x} / {y} = {x/y:.2f}')
print(f'{x} % {y} = {x%y}')
print(f'{x} // {y} = {x//y}')
print(f'{x} ** {y} = {x**y}')

































































