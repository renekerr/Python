# Functions Exercise 1 (Adding Two Numbers)
# This program receives a number from a user and adds 5 to it

def adding_numbers(k):
    r = k + 5
    return r

# Main program
user_response = input("Enter an integer: ")
k = int(user_response)

s = adding_numbers(k)
print(k, "+ 5 = ",s)

