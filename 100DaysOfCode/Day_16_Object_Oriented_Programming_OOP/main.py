# Day 16- Object-Oriented Programming (OOP)
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)  # this will print an object <turtle.Turtle object at 0x10e943b60>
timmy.shape('turtle')
timmy.shapesize(2.5, 2.5, 6)
timmy.color('aquamarine4')
timmy.forward(100)


"""
https://docs.python.org/3/library/turtle.html
https://cs111.wellesley.edu/reference/colors
"""
# Attributes (what it 'has', variables)
my_screen = Screen()
print(my_screen.canvheight)   # this line will print 300, the value of the attribute

# Methods (what it 'does', functions)
my_screen.exitonclick()
