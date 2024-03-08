#Quiz 3, Part 3
# Write a program that asks the user for a positive number 'n' as input. Assume that the user enters a number
# greater than or equal to 3 and print a triangle as described below.

# *
# **
# ***
# ****
# *****
# ******
# *****
# ****
# ***
# **
# *

n = int(input("Enter a positive number n: "))

for x in range(1, n+1):
    print("*" * x)

for y in range(n-1, 0, -1):
    print("*" * y)

# El tipo range con tres argumentos se escribe range(m, n, p) y crea una lista que empieza en m
# y acaba antes de llegar a n, avanzando de p en p.


