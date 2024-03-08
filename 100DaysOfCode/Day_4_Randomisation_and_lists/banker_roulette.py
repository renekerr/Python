'''
You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
'''
names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']

import random
x = random.randint(0, len(names)-1)
w = names[x]

print(f'{w} is going to pay the meal today!')

