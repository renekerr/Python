"""
Strings Exercise 4

Write a program that asks the user for an input 'n' and prints a square of n by n asterisks "*".
For example if the user enters 5 then the output should look like the following:

Note that there should be no spaces between the asterisks

*****
*****
*****
*****
*****

"""

# Main program
n = int(input('Enter a positive integer: '))

i = 1
character = '*'
while i < n + 1:
    print(n*character)
    i = i + 1

"""
################### Sample Solution ###################
n = int(input("Please enter a positive integer: "))
for x in range(1, n+1):
    print("*" * n)
"""

