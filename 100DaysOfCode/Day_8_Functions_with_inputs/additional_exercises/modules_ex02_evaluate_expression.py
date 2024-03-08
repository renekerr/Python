# Python Modules Exercise 2 (Evaluate Expression)
# Write a function that accepts a number x and evaluates the following expression:
# y = abs(x^3) + cos(sqrt(3x))

from math import *
def my_math_fn(x):
    y = abs(x**3)+ cos(sqrt(3*x))
    return y


# Main program
print("Exercise_2")
print("¨¨¨¨¨¨¨¨¨¨")
user_response = input("Enter a value for x: ")
x = int(user_response)
m = my_math_fn(3)

print("For x =",x,)
print("The expression y = abs(x^3) + cos(sqrt(3x)) is equal to ", m)