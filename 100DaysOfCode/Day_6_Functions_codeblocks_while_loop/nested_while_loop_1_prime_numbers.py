# Algorithm to determine if a number is prime
# Prime numbers are divisible only by themselves and 1

# 1- Select a number
# 2- Select a divisor and set it equal to 2
# 3- Assume the number is prime
# 4- If divisor is less than the number, go to step 5, otherwise go to step 8
# 5- If remainder of (number/divisor) is 0 then the number is not prime (exit/stop)
# 6- Add one to the divisor
# 7- Go to step 4
# 8- Number is prime


# This a program that determines if a number is prime

current_number = 23 # Change number here
current_divisor = 2

is_current_number_prime = True

while (current_divisor < current_number):
    if current_number % current_divisor == 0:
        is_current_number_prime = False
        break
    current_divisor = current_divisor + 1
if is_current_number_prime:
    print(current_number, " is prime")
else:
    print(current_number, " is NOT prime")
print("All done!")

