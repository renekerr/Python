# Write a program which asks the user to type a string
# and then prints "Yes" if "dog" is in that string,
# otherwise prints "No"

s= input("Please enter an string: ")
if 'dog' in s:
    print('Yes')
else:
    print('No')
    


# Write a program which asks the user to type an integer
# and then prints "Yes" if that integer is divisible by 3, otherwise prints "No"

i= input("Please enter an integer: ")
result= (int(i)%3)
if result == 0:
    print('Yes')
else:
    print('No')
    
