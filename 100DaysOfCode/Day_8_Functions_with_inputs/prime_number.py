# Prime number
'''
Prime numbers are numbers that can only be cleanly divided by themselves and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

'''

def prime_checker(number):
    prime = True
    if number <= 1:
        prime = False
    for i in range(2, number):
        if number % i == 0:
            prime = False

    if prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number")

n = int(input('Enter a number: '))
prime_checker(number = n)