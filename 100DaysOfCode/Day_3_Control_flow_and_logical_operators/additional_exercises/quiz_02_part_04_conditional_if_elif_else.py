# Quiz 2 Part 4. Program
# Write a program which asks the user to enter a positive integer 'n' (Assume that the user always enters
# a positive integer) and based on the following conditions, prints the appropriate results exactly as shown
# in the following format (as highlighted in yellow).


user_response= input("Please enter an integer: ")
n= int(user_response)

if (n%2 == 0) and (n%3 ==0): #when 'n' is divisible by both 2 and 3 (for example 12)
    print('BOTH')

# when 'n' is divisible by only one of the numbers i.e divisible by 2 but not divisible by 3
# (for example 8), or divisible by 3 but not divisible by 2 (for example 9)

elif (n%2 == 0 and n%3 != 0) or (n%2 !=0 and n%3 == 0):
    print('ONE')
    
else:
    print('NEITHER')


