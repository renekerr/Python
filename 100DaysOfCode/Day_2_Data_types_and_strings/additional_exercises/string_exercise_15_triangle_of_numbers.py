"""
Strings, Exercise 3

Write a program using while loops that asks the user for a positive integer 'n' and prints a triangle using numbers from
1 to 'n'. For example if the user enters 6 then the output should be like this :

(There should be no spaces between the numbers)

1
22
333
4444
55555
666666

"""

# Main program
n = int(input('Enter a positive integer: '))

i = 1
while i <= n:
    print(i*str(i))
    i = i + 1

"""
################### Sample Solution ###################
x = int(input("Please enter an integer: "))
y = 1
while y < x+1:
    print (str(y) * y)
    y = y + 1
"""