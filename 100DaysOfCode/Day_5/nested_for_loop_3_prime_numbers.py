# This program prints all prime numbers between 2 and 8 ( change number )
# Prime numbers are divisible only by themselves and 1



start_number = 2 # Change number here
end_number = 5 # Change number here
current_number = start_number


# Using nested for loops
for current_number in range(start_number, end_number+1):
    is_current_number_prime = True

    for current_divisor in range(2, current_number):

        if current_number % current_divisor == 0:
            is_current_number_prime = False
            break
        print('current divisor', current_divisor)
    if is_current_number_prime:
        print(current_number, " is prime")
    else:
        print(current_number, " is NOT prime")

print("All done!")