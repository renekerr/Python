'''
Dictionaries, Exercise 1

What will be printed after each of the following code segments? If error, then write Error
Pay attention to the spaces. Your answer should exactly match the correct Python output.
'''

print('Example_1')
numbers = {'one':1, 'two':2, 'three':3}
print(numbers['two'])
print('\n')

print('Example_2')
numbers = {'one':'uno', 'two':'dos', 'three':'tres'}
print(numbers['three'])
print('\n')

print('Example_3')
numbers = {'one':1, 'two':2}
#print(numbers[2]) KeyError: 2
print('KeyError: 2')
print('\n')

print('Example_4')
numbers = {'one':'uno', 'two':'dos', 'three':'tres'}
print('two' in numbers) # Return True/False
print('\n')


