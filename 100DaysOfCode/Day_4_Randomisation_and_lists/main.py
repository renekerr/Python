'''
Day 4 - Randomisation and Python Lists
'''

'''

RANDOMISATION & LISTS
                                                         

'''

# Import & use a module
import random

rint = random.randint(1,10)
print(rint)

rfloat = random.random()
print(rfloat)

'''
by multiplying rfloat by 5, we will get a random number between [0 - 5)
0.000000....4.9999999
'''

nrfloat = rfloat * 5
print(nrfloat)


'''
LISTS
Lists:

Ordered collection of items
Accessed by position (index)
Allow duplicate items
Can store any data type  

Example: 
    Shopping list with items in a specific order
'''

# Lists
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Caucasia", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)
# List indexing
print(states_of_america[0])
print(states_of_america[1])
print(states_of_america[2])

# Nested lists

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1])

print(dirty_dozen[1][1]) # this will print the second item of the second list which is Kale




