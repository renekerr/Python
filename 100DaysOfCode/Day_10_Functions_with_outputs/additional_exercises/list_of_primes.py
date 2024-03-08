"""
Midterm Exam, Part 4 (List of Primes)

Write a function named list_of_primes that accepts a positive integer n and returns a sorted list
(ascending order) of all the prime numbers between 2 and n (including 2 but not including n)

Prime numbers are divisible only by themselves and 1

"""



# Define function
def list_of_primes(n):
    output_list = []            # Empty list where prime numbers will be stored

    for i in range(2, n):       # Including 2 but not including n
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




"""
################### Instructor function ###################
def _list_of_primes_sample_(n):
    my_list = []
    integer = 2
    while integer < n:
        prime = True
        start = 2
        while start < integer:
            if integer % start == 0:
                prime = False
            start = start + 1
        if prime == True:
            my_list.append(integer)
        integer = integer + 1
    return my_list

    [2, 3, 5, 7, 11, 13, 17, 19] Correct answer

"""









