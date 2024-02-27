# Write a program using while loop, which asks the user to type a positive integer, n,
# and then prints the factorial of n.
# A factorial is defined as the product of all the numbers from 1 to n (1 and n inclusive)


user_response = input ("Please enter an integer:")
n = int(user_response)

x = 1
factorial = 1

while x <= n:       

    factorial = factorial * x
    x = x + 1
print(factorial)


################### Sample Solution ###################
y = input("Type a number:")
x = int(y)
count = 1
z = 1
while z <= x:
    count = count * z
    z = z + 1
print(count)
