# Quiz 3, Part 5
# Write a function that receives a positive integer as function parameter and returns True
# if the integer is a perfect number, False otherwise. A perfect number is a number whose
# sum of the all the divisors (excluding itself) is equal to itself. For example: divisors of 6
# (excluding 6 are) : 1, 2, 3 and their sum is 1+2+3 = 6. Therefore, 6 is a perfect number.

def perfect_number(n):
    s = 0
    for x in range(1,n):
        if n % x == 0: # when remainder of n divided by x is equal to 0, then x is a divisor of n
            s = s + x

    # check if the sum of the divisors equals to n itself
    if s == n:
        return True
    else:
        return False

# Main program
n = 28
f = perfect_number(n)

print(f)

