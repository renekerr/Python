# Python Modules Exercise 1 (Evaluate Trigonometric Expression)
# Write a function that accepts a number x and evaluates the following expression:
# y = sin(x) - cos(x) +  sin(x)cos(x)



from math import *
def my_math_fn(x):
    y = sin(x)-cos(x)+(sin(x)*cos(x))
    return y


# Main program
print("Exercise_1")
print("¨¨¨¨¨¨¨¨¨¨")
user_response = input("Enter a value for x: ")
x = int(user_response)
m = my_math_fn(x)

print("For x =",x,)
print("The expression y = sin(x) - cos(x) +  sin(x)cos(x) is equal to ", m)