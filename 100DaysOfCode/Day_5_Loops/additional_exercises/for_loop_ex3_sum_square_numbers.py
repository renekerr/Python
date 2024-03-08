# Using a for loop, write a program which asks the user to type an integer, n,
# and then prints the sum of the square of all numbers from
# 1 to n (including both 1 and n).

# For example if the user type 3, the answer should be
# ((3**2) + (2**2) + (1**2)) = 14

user_response = input("Type an integer: ")
n = int(user_response)

y = 0

for x in range(1, n+1):
    y = x ** 2
print(y)