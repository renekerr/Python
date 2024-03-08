'''
 VARIABLES
'''


# Declaring variables in Python
first_name = 'Rene'
last_name = 'Kerr'
country = 'Spain'
city = 'Madrid'
age = 50
is_married = False
skills = ['SQL', 'Python']
person_info = {
    'firstname':'Alex', 
    'lastname':'Kerr', 
    'country':'Cuba',
    'city':'Havana'
    }

# Printing variables
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line
first_name, last_name, country, age, is_married = 'Rene', 'Alexis', 'Japan', 99, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)