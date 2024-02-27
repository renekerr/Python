# List Methods Exercise 7 (List of Multiples)
# Write a function that accepts a positive integer k and returns a list that contains the first five multiples of k.
# The multiples should be calculated starting from 1 to 5 (including both 1 and 5).
# For example the first five multiples of 3 are 3, 6, 9, 12, and 15


def k_multiples(k):             # Define function
    results = []                # Assign a var as empty list

    for x in range(1,6):        # Loop

        m = x * k               # Statement
        results.append(m)       # Append elements to the list using list.append(9 method
    return results              # Return value(s)

# Main program
k = int(input('Enter a number : '))
f = k_multiples(k)
print('First five multiples of', k, 'are:')
print(f)
