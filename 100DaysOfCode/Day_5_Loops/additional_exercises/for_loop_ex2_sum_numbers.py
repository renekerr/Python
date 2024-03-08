# Using a for loop, write a program which asks the user to type an integer, n,
# and then prints the sum of all numbers from 1 to n (including both 1 and n).

user_response = input("Type a number: ")
n = int(user_response)

y = 0

for x in range(1, n+1):
    y = y + x
print("Sum of all numbers from 1 to", n, "is = ", y)
    
