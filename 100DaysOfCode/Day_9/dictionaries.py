'''
Dictionary: 
A collection of {key:value} pairs ordered and changeable. No duplicates.
'''

# Access keys and values in a dictionary
people = {
    "Alice": 25,
    "John": 30,
    "Mary": 22,
    "Peter": 40,
    "Laura": 18
}

# Attributes and methods related to a dictionary
print(dir(people))
print(help(people))

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

# Retrieve values from dictionary
print(student['courses']) # ['Math', 'CompSci']
print(student.get('name')) # John
print(student.get('phone', 'Key not found!')) # Key not found!

# Modify/update value in dictionary
print(student) # {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
student['name'] = 'Jamie'
print(student) # {'name': 'Jamie', 'age': 25, 'courses': ['Math', 'CompSci']}
student.update({'name':'Jane', 'age':26, 'phone': 666777888})
print(student) # {'name': 'Jane', 'age': 26, 'courses': ['Math', 'CompSci'], 'phone': 666777888}
del student['phone']
print(student) # {'name': 'Jane', 'age': 26, 'courses': ['Math', 'CompSci']}
student['age'] = 34
print(student) # {'name': 'Jane', 'age': 34, 'courses': ['Math', 'CompSci']}
age = student.pop('age')
print(f'Age is {age}') # Age is 34
print(student) # {'name': 'Jane', 'courses': ['Math', 'CompSci']}

# Dictionary lenght
dict_len = len(student)
print(f'Lenght of dictionary is {dict_len}') # Lenght of dictionary is 2

# Keys and values of a dictionary
k = student.keys()
v = student.values()
i = student.items()
print(f'Keys are: {k}') # Keys are: dict_keys(['name', 'courses'])
print(f'Values are: {v}') # Values are: dict_values(['Jane', ['Math', 'CompSci']])
print(f'Key:value pairs: {i}') # Key:value pairs: dict_items([('name', 'Jane'), ('courses', ['Math', 'CompSci'])])

# Looping through a dictionary 
for key, value in student.items():
    print(key, value)

# Clear/empty a dictionary
people.clear()
student.clear()



# Fill an empty dictionary
from mod_clear_screen import clear_screen
user_info = {}

stop_add = False

while not stop_add:
    user_name = input('User name: ')
    user_age = int(input('Age: '))

    user_info[user_name] = user_age

    continue_adding = input("Add more users, 'yes' or 'no'. ")
    if continue_adding == 'no':
        stop_add = True
        print(user_info) # {'Alex': 50, 'Jim': 56, 'Pet': 40, 'Kim': 60}
    else:
        clear_screen()






