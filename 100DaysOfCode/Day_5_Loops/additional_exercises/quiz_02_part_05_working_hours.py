# Quiz 2 Part 5
# Write a program which asks the user to enter an integer 'n' which would be the total numbers of hours the user worked
#  in a week and calculates and prints the total amount of money the user made during that week. If the user enters any
#  number less than 0 or greater than 168 (n < 0 or n > 168) then your program should print INVALID

user_response= input("Enter total number of hours: ")
n= int(user_response)
total= 0

if n < 0 or n > 168:
    print('INVALID')

elif n <=40:
    total= n*8
    print("YOU MADE", total, "DOLLARS THIS WEEK")

elif n <=50:
    total= (40*8)+((n-40)*9)
    print("YOU MADE", total, "DOLLARS THIS WEEK")
    
else:
    total= (40*8)+(10*9)+((n-50)*10)
    print("YOU MADE", total, "DOLLARS THIS WEEK")
