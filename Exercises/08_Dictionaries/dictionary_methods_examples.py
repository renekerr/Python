'''
Dictionary Methods, Exercise 1

What will be printed after each of the following code segments? If error, then write Error
Pay attention to the spaces. Your answer should exactly match the correct Python output
'''

print('Example_1 | pop()')
numbers = {1:2, 3:4}
print('numbers =',numbers)
numbers.pop(3)
print(numbers)
print('\n')

print('Example_2 | pop()')
d = {'uno':['one', 1], 'dos':['two', 2], 3: ['tres', 'three']}
print('d =',d)
print(d.pop('dos'))
print('d = ',d)
print('\n')

print('Example_3 | get()')
d = {'uno':['one', 1], 'dos':['two', 2], 3: ['tres', 'three']}
print('d =',d)
print(d.get(3,'cat'))
print('d =',d)
print('\n')

print('Example_4 | get()')
numbers = {'one':'uno', 'two':'dos', 'three':'tres'}
print('numbers =',numbers)
print(numbers.get('one', 'test'))
print('numbers =',numbers)
print('\n')

print('Example_5')
d = {"uno":["one",1],"dos":["two",2],3:["tres","three"]}
print('d =', d)
#print (d.has_key(3))   'dict' object has no attribute 'has_key' Error
print("Error...'dict' object has no attribute 'has_key'")
print('\n')

print('Example_6 | setdefault()')
d = {"uno":"one","dos":"two"}
print('d =',d)
d.setdefault('one', 'dog')
print(d['one'])
print('d =',d)
print('\n')

'''
dict.setdefault(key, default=None)	Similar to get(), but will set dict[key]=default if key is not already in dict
'''


