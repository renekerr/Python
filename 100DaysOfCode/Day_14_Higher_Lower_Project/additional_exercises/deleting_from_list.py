'''
Deleting item from list containing dictionaries as items
'''

from game_data import data_testing
from random import choice

print(data_testing)
print(len(data_testing))

a = choice(data_testing)
idx = data_testing.index(a)


print(f'\nEntity: {a}')
print(f'Index : {idx}\n')

data_testing.pop(idx)

print(data_testing)
print(len(data_testing))


