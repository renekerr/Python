'''
Day 8 - Functions with inputs (parameters)
'''

'''
FUNCTIONS WITH PARAMETERS
'''
# Greeting I
def greet():
    print('Hi there!')

greet()

# Sum numbers
def suma():
    a = 3
    b = 2
    print(a+b)

suma()

# Greeting II
def greeting_name_location(name, location):
    print(f'Hi {name}')
    print(f'How is the weather like in {location}?')

greeting_name_location('René', 'Madrid')

# Greeting III
def greeting_position(name, location):
    print(f"Hi {name}")
    print(f"What's the weather like in {location}?")

greeting_position(name = 'Alex', location = 'London')
greeting_position(location = 'London', name = 'Alex')

# Greeting IV
def greeting_input(name, location):
    print(f"Hi {name}")
    print(f"What's the weather like in {location}?")

n = input('Name: ')
l = input('Location: ')

greeting_input(name = n, location = l)

# Auditorium LESSON 20 DAY 8 - PAINT AREA CALCULATOR
import math
def paint_calc(height, width, cover):
  number_of_cans = math.ceil((height * width)/cover)
  print(f"You'll need {number_of_cans} cans of paint.")

h = int(input('Height of the wall: '))
w = int(input('Width of the wall: '))
coverage = 5

paint_calc(height = h, width = w, cover=coverage)





