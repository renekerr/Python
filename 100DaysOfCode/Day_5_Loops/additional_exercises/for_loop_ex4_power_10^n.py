# Write a program that asks the user for an input 'n'
# (assume that the user enters a positive integer) and prints a sequence
# of powers of 10 from 10^0 to 10^n in separate lines.
# For example if 'n' is equal to 4 then the output should look like
# the following:

# 1
# 10
# 100
# 1000
# 10000

user_response = input("Type a number: ")
n = int(user_response)

y = 0

for x in range(0,n+1):
    y = 10**x
    print(y)
    
    

