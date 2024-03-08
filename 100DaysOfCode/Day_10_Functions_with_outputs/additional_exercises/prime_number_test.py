"""
Prime numbers are divisible only by themselves and 1

"""


# Main program
"""
Part 1
This first program determines if a user given number is prime or not
--------------------------------------------------------------------

n = int(input('Enter a integer number : '))
is_prime = True
start = 2


if n < 2:               # 0 and 1 are not prime numbers
    is_prime = False

while start < n:    # Iterate from 2 to the number
    if n % start == 0:
        is_prime = False
    start = start + 1

if is_prime:
    print(n, 'is prime')
else:
    print(n, 'is NOT prime')

"""



"""
Part 2
This second program determine if a number is prime and store the result in a list
----------------------------------------------------------------------------------

number = 20
i = 2
output_list = []

for i in range(2, number + 1):
    is_number_prime = True

    for k in range(2, i):
        if i % k == 0:
            is_number_prime = False

    if is_number_prime:
        output_list.append(i)

print(output_list)

"""



"""
Part 3
This function receives a value n and returns a list with all prime numbers between 2 and n
-------------------------------------------------------------------------------------------
"""


# Define function
def list_of_primes(n):
    output_list = []            # Empty list where prime numbers will be stored

    for i in range(2, n+1):
        is_prime = True

        for k in range(2, i):
            if i % k == 0:
                is_prime = False

        if is_prime:
            output_list.append(i)

    return output_list



# Main program
n = int(input('Enter and integer value : '))
my_function = list_of_primes(n)

print('\nPrime numbers between 2 and', n, '(both inclusive)')
print(my_function)




