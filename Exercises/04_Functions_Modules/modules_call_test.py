# This program tests how modules works
# File(module) containing functions to be used is
# /Python/modules_lesson_example.py

# from modules_lesson_example import add_numbers, multiply_numbers

# if using '*' all functions in the file will be imported
from modules_lesson_example import *
from math import * # import all functions included in 'math' module


a = 5
b = 8

c = add_numbers(a,b)
print(c)

d = multiply_numbers(a,b)
print(d)

x = 2
print(sqrt(x))
print(sin(x))

#### NOTES ####
# A module is a file with .py extension which contains Python statements
# A module can contain executable statements as well as function definitions
# To include a module in your program use:
# import module_name (module name only, not extension)
# To import all functions within a module use:
# from module_name import *



