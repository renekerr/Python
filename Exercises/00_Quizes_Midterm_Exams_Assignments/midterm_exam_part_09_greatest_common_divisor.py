"""
Midterm Exam, Part 9 (GCD)

Write a function named find_gcd that accepts a list of positive integers and returns their greatest common divisor (GCD).
Your function should return 1 as the GCD if there are no common factors between the integers. Here are some examples:

if the list was

[12, 24, 6, 18]
then your function should return the GCD:
6
if the list was
[3, 5, 9, 11, 13]
then your function should return their GCD:
1
"""

# Define function
def gcd_list(list_sample):
    result = list_sample[0]

    for k in range(1, len(list_sample)):
        result = euclidean_gcd(result, list_sample[k])
    return result


def euclidean_gcd(x,y):

    """This function implements the Euclidean algorithm to find H.C.F. of two numbers"""
    while y:
        x, y = y, x % y  # See http://www.programiz.com/python-programming/examples/swap-variables
    return x


"""
    Here we loop until y becomes zero. The statement x, y = y, x % y does swapping of values in Python.
    In each iteration we place the value of y in x and the remainder (x % y) in y, simultaneously.
    When y becomes zero, we have H.C.F. in x.

    For more info, see video: https://www.youtube.com/watch?v=H8jbNa6lcB4

"""



# Main program
list_sample = [12, 24, 6, 18]
print('List')
print(list_sample,'\n')

my_function = gcd_list(list_sample)


print('GCD or Greatest Common Divisor is ',my_function)



"""
In mathematics GCD or Greatest Common Divisor of two or more integers is the largest positive integer that
divides both the number without leaving any remainder

Definition
¨¨¨¨¨¨¨¨¨¨
gcd(a,b) = a, if b = 0
         = gcd(b, a mod b), otherwise

Máximo Común Divisor
El máximo común divisor de dos o más números naturales (enteros positivos) es, como su nombre indica,
el mayor de los divisores comunes a dichos números.

El método más sencillo e intuitivo para saber cúal es el máximo común divisor de varios números,
consiste en calcular los divisores de cada número y, de los divisores comunes a dichos números,
el mayor de ellos será su Máximo Común Divisor.

Máximo Común Divisor de 6, 12 y 18

Los divisores de 6 son ⇒ 1, 2, 3, 6
Los divisores de 12 son ⇒ 1, 2, 3, 4, 6, 12
Los divisores de 18 son ⇒ 1, 2, 3, 6, 9, 18

Los divisores comunes de 6, 12 y 18 son ⇒ 1, 2, 3, 6

Como el mayor es 6, el M.C.D. (6 , 12 , 18) = 6

Si dos números sólo tienen como divisor común el 1 decimos que son Primos Entre Si, y entonces su Máximo Común Divisor
es igual a 1.

"""
