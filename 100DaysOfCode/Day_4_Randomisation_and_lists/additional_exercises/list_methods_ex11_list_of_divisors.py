# List Methods Exercise 11 (List of Divisors)
# Write a function that accepts a positive integer k and returns the list of all the divisors of k.
# Your list should include both 1 and k.


def divisors_numbers(k):                    # Define fucntion
    output_list = []                        # Assign variable as empty list

    for number in range(1,k+1):             # Loop from 1 to k (k included)

        if k % number == 0:                 # Los divisores de un número natural son los números naturales que lo pueden dividir,
                                            # resultando de cociente otro número natural y de resto 0.
            output_list.append(number)      # Add elements to the list
    return output_list                      # Return value(s)



# Main program
k = int(input('Enter a value (k): '))
f = divisors_numbers(k)

print('Divisors of k are: ')
print(f)

