# Using lists
empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0


# list of animal products
countries = ['Spain', 'Portugal', 'New Zealand', 'Croatia', 'Netherland']

# Print the lists and it length
print('Number of countries:', len(countries))


fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruits[0] = 'avocado' 
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']

# checking items
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# Append
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime]
print(fruits)

# insert
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'mango', 'lime','lemon',]
print(fruits)

# remove
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango']

# pop
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()     
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)     
print(fruits)       # ['orange', 'mango'] 

# delelete
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]     
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]     
print(fruits)       # ['orange', 'lemon']
del fruits
#print(fruits)       # This should give: NameError: name 'fruits' is not defined

# clear
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()     
print(fruits)       # []

# copying a list

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()     
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

# join
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )

# join with extend
num1 = [0, 1, 2, 3]
num2= [4, 5,6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits )

# count
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

# index
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24)) 

# Reverse
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)  
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) 

# sort
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits) 
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) 
ages.sort(reverse=True)
print(ages) 

### Some more examples... ###
list_01 = list()
list_02 = []

print(len(list_01))

list_01 = [35, 24, 62, 52, 30, 30, 17]

print(list_01)
print(len(list_01))

list_02 = [49 , 1.95, 'Rene', 'Kerr']
print(list_02)

print(type(list_01))
print(type(list_02))

print(list_02[0])
print(list_02[1])
print(list_02[2])
print(list_02[3])
## print(list_02[4]) ## IndexError: list index out of range

print(list_02[-1])
print(list_02[-2])
print(list_02[-3])
print(list_02[-4])
## print(list_02[-5]) ## IndexError: list index out of range

print('list_01', list_01)
print('list_02', list_02)
print('Joining previous lists... ', list_01 + list_02)

list_03 = list([43, 1.61, 'Joe', 'Doe'])
print('list_03', list_03)

list_04 = [50, 1.89, 'Jon', 'Doe']
print('list_04', list_04)

age, height, user_name, user_surname = list_04[0], list_04[1], list_04[2], list_04[3],
print(user_name, user_surname, 'is', age  , 'years old')


list_01_02 = list_01 + list_02
print(list_01_02) # [35, 24, 62, 52, 30, 30, 17, 49, 1.95, 'Rene', 'Kerr']


list_01_02.append('Cuba') # type: ignore
print(list_01_02)

list_01_02.insert(1, 'Spain') # type: ignore
print(list_01_02)

list_01_02[-2] = 'Denmark' # type: ignore
print(list_01_02)

list_01_02.reverse()
print(list_01_02)

list_01_02.remove(30)
print(list_01_02)

print('pop value', list_01_02.pop(-3))
print(list_01_02)

print('pop value', list_01_02.pop(5))
print(list_01_02)

del list_01_02[6]
print(list_01_02)

del list_01_02[-1]
print(list_01_02)

list_01_02.remove(62)
print(list_01_02)
list_01_02.remove(30)
print(list_01_02)

list_def = list_01_02.copy()

list_01_02.clear()
print(list_01_02)

print(list_def)
list_def[-1] = 'Japan' # type: ignore
print(list_def)

list_def.reverse()
print(list_def)

print(list_def[0:2])