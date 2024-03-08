# List Methods Exercise 10 (List of Cube Roots))
# Write a function that accepts a positive integer k and returns the ascending sorted list of cube root values of all
# the numbers from 1 to k (including 1 and not including k). [if k is 1, your program should return an empty list]

def cube_root_numbers(k):                       # Define function
    output_list = []                            # Assign variable as empty list
    for number in range(1,k):                   # Loop from 1 to k(not included)

        cube_root = number ** (1/3)             # Cube root calculation
        output_list.append(cube_root)           # Add values to the list

    output_list.sort(reverse=False)             # Sort list (ascending order)
    return output_list                          # Return value(s)


# Main program
k = int(input('Enter a number (k): '))
f = cube_root_numbers(k)

print('Cube root of values between 1 and k (k not included) are: ')
print(f)

