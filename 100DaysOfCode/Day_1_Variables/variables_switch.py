'''
This program takes two inputs. The first input is stored in a variable called a. The second input is stored in a variable called b.

Write a program that switches the values stored in the variables a and b.
'''
# There are two variables, a and b from input
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

c=a
a=b
b=c

print('Numbers switched')
print("a: " , a)
print("b: " , b)
