'''
 Day 1 - Beginner - Working with Variables in Python to Manage Data

 
VARIABLES

 '''

print('Hi ' + input('What is your name? ') + '!')
print(len(input('What is your name? ')))

# Variables
print('Day 1 of 100DaysofCode')
first_name = 'René'
last_name = 'Kerr'
full_name = first_name + ' ' + last_name
country = 'Cuba'
age = 49
is_married = True
books_read = [
    'Trilogía sucia de La Habana', 'El insaciable hombre araña',
    'El rey de La habana'
]

# Declaring multiple variables in one line
job, language, city = 'Database Administrator', 'Spanish', 'Madrid'

# Printing variables
print('First name:', first_name)
print('Last name:', last_name)
print('Full name:', full_name)
print('Country:', country)
print('Age:', age)
print('Is married:', is_married)
print('Books read:', books_read)
print('Job:', job)
print('Language:', language)
print('City:', city)