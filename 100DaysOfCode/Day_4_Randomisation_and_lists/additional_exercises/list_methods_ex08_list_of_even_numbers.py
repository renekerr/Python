# List Methods Exercise 8 (List of Even Numbers)
# Write a function that accepts two positive integers a and b and returns a list of all the even numbers
# between a and b (including a and not including b).


def even_numbers(a,b):                  # Define function
    results_list = []                   # Assign a var as empty list
    for x in range(a,b):

        if x % 2 == 0:                  # Even numbers : number % 2 == 0  // Odd numbers : number % 2 != 0
            results_list.append(x)      # Add elements to the list using list.append() method
    return results_list                 # Return value(s)



# Main program

a = int(input('Enter a: '))
b = int(input('Enter b: '))

f = even_numbers(a,b)
print('Even numbers between a and b are: ')
print(f)



