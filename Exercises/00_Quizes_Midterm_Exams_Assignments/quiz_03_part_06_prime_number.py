#Quiz 3, Part 6
# Write a function that accepts a positive integer n as function parameter and returns True
# if n is a prime number, False otherwise. Note that zero and one are not prime numbers and two
# is the only prime number that is even


# Se conoce como número primo a cada número natural que sólo puede dividirse por 1 y por sí mismo.
# Por citar un ejemplo: 3 es un número primo, mientras que 6 no lo es ya que 6 / 2 = 3 y 6 / 3 = 2.


def prime_number(n):

    if n < 2:       # 0 and 1 are not prime numbers
        return False

    # Iterate from 2 to the number
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = 27
f = prime_number(n)

print(f)