'''
Dictionaries, Exercise 2

What will be printed after each of the following code segments? If error, then write Error
Pay attention to the spaces. Your answer should exactly match the correct Python output.
'''

print('Example_1')
numbers = {'one':'uno', 'two':'dos', 'three':'tres'}
print('uno' in numbers)
print('\n')

print('Example_2')
numbers = {"one": "uno", "two": "dos"}
pass
numbers["two"] = 2
print (numbers["dos"]) #KeyError: 'dos'
print("KeyError: 'dos'")
print('\n')

print('Example_3')
numbers = {"one": "uno", "two": "dos"}
pass
numbers["dos"]="two"
print (numbers["two"])
print('\n')

print('Example_4')
numbers = {'one':1, 'two':[4, 6, 3], 'three':3}
x = numbers['two']
x.sort()
print(x)
print('\n')


