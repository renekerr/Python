# Quiz 2 Part 3. Program
# This program receives the user's age and returns a value using conditional if-elif-else

user_response= input("Please enter your age: ")
age= int(user_response)

if age <= 0:
    print('UNBORN')
elif age > 0 and age <= 150:
    print('ALIVE')
else:
    print('VAMPIRE')
