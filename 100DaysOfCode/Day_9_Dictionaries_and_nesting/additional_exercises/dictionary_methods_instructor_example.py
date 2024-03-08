# Examples of some dictionary methods in Python

print('Example 1')
person = {'Name':'John', 'Age':30, 'Weight':160}
print(person)

# dict.clear()
person.clear()
print(person)
print('\n')

# dict.get(key, default=None)
print('Example 2')
person = {'Name':'John', 'Age':30, 'Weight':160}
print(person)

x = person.get('Age')
print(x)

w = person.get('Job')
print(w)
# If the key does not exist Python will return None (default)

z = person.get('Job', 'Key Not Found!')
print(z)
# If the key does not exist Python will return value of second parameter

y = person['Age']
print(y)
# If the key does not exist Python will return an error
print('\n')

# dict.keys()
print('Example 3')
person = {'Name':'John', 'Age':30, 'Weight':160}
print(person)

x = person.keys()
x = list(x) # Or x = list(person.keys())
print(x)
print('\n')

# dict.pop()
print('Example 4')
person = {'Name':'John', 'Age':30, 'Weight':160}
print(person)

x = person.pop('Age')
print(x)
print(person)
print('\n')


# dict.update(dict2)
print('Example 5')
person = {'Name':'John', 'Age':30, 'Weight':160}
print(person)

pet = {'Type':'dog', 'Color':'White', 'Age':7} # 'Age':30 will be replaced by 'Age':7
print(pet)

person.update(pet)
print(person)
print('\n')


# dict.values()
print('Example 6')
person = {'Name':'John', 'Age':30, 'Weight':160}
print(person)

x = person.values()
print(list(x))




'''
Table of common methods for Dictionaries
=========================================

Description
dict.clear()
Removes all elements of dictionary.

dict.copy()
Returns a shallow copy of dictionary.

dict.fromkeys(seq[,value])
Create a new dictionary with keys from seq and values set to value.

dict.get(key, default=None)
For key key, returns value or default if key not in dictionary

dict.items()
Returns a view object of dict items.

dict.keys()
Returns a view object of dict keys.

dict.pop(key)
Remove key, Return value

dict.setdefault(key, default=None)
Similar to get(), but will set dict[key]=default if key is not already in dict

dict.update(dict2)
Adds dictionary dict2's key-values pairs to dict

dict.values()
Returns a view object of dict_values.

'''

















































