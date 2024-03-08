# Conditional if elif, Ex4
# Write a program which asks the user to type a string and then: 
# Print "Dog" if "dog" is in the input string.
# Print "Cat" if "cat" is in the input string. (if both "dog" and "cat" are in the input string then you should only print "Dog") 
# Otherwise prints "None". (Pay attention to capitalization).



x= input("Enter a string: ")
if "dog" in x:
    print("Dog")
elif "cat" in x:
    print("Cat")
elif "dog" in x and "cat" in x:
    print("Dog")
else:
    print("None")
    
    
    
# Conditional if elif, Ex5
# Write a program which asks the user to type an integer.
# If the number is 2  then the program should print "two",
# If the number is 3  then the program should print "three",
# If the number is 5  then the program should print "five", 
# Otherwise it should print "other".



user_response= input("Enter an integer: ")
value= int(user_response)

if value == 2:
    print("two")
elif value == 3:
    print("three")
elif value == 5:
    print("five")
else:
    print("other")
    

