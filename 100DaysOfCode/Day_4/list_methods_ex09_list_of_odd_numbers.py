# List Methods Exercise 9 (List of Odd Numbers)
# Write a function that accepts two positive integers a and b (a is smaller than b)and returns a list that
# contains all the odd numbers between a and b (including a and including b if applicable) in descending order.

def odd_numbers(a,b):                           # Define function
    output_list = []                            # Assing variable as empty list

    for number in range(a,b+1):                 # Loop including a and b
        if number % 2 != 0:                     # # Even numbers : number % 2 == 0  // Odd numbers : number % 2 != 0
            output_list.append(number)          # Add elements to the list


    output_list.sort(reverse=True)              # Sort elements in descending order (reverse=False for ascending order)
    return output_list                          # Return value(s)


# Main program

a = int(input('Enter number a: '))
b = int(input('Enter number b: '))

if a < b :
    f = odd_numbers(a,b)
print('Odd numbers between a and b are (descending order): ')
print(f)
