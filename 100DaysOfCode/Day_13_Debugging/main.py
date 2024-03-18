'''
Day 12 - Debugging: How to Find and Fix Errors in your Code

'''


############DEBUGGING#####################

# # Example 1
# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# Example 2
# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# Example 3
# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >1994:
#   print("You are a Gen Z.")

# Example 4
# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
# print(f"You can drive at age {age}.")

# Example 5
# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# Example 6
# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])


############DEBUGGING SOLUTION#####################
# Example 1
'''
To ensure that the program prints when the number reaches 20, the stop value in the range function should be 21 instead of 20. 
This adjustment allows the loop to iterate up to and including 20, thus triggering the print statement when the number equals 20.
'''


# Example 2
'''
There are two issues in this code. Firstly, since indexing in lists starts at 0, the current implementation does not display 'dice 1'. 
Secondly, when the random number generator produces a 6, it raises an IndexError due to the list index being out of range. 
To address these problems, we need to adjust the randint() function to generate random numbers between 0 and 5 (inclusive) instead of 1 to 6. 
This ensures that the indexing aligns with the available items in the list.
'''


# Example 3
'''
The code currently fails to correctly classify individuals born in 1994 as Generation Z.
To correct this, we need to adjust the condition in the elif statement to include individuals born in 1994 as part of Generation Z:
elif year >= 1994:
'''


# Example 4
'''
This code needs a couple of adjustments to function correctly. 

Firstly, we need to ensure that the user's input for age is converted to an integer since we cannot compare a string with an integer.

Secondly, we should improve the output formatting by using the f-string (format) with the print() statement.

The final corrected code should resemble this:
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
'''
# Example 5
'''
By using print statements, we identified that the value of word_per_page remained 0.
This was because the line word_per_page == int(input("Number of words per page: ")) mistakenly used the equality operator instead of the assignment operator.

The correct fix was to change it to word_per_page = int(input("Number of words per page: ")).

assignment (=)
equality (==)
'''

# Example 6
'''
Debugging Summary:
The issue with the code was that the list b_list was not properly populated.
Inside the loop, the new_item was calculated correctly, but it was not added to b_list during each iteration.
Therefore, only the last new_item was added to b_list.
To fix this, we moved the b_list.append(new_item) statement inside the loop, ensuring that each new_item is added to b_list.

Solution: 
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

'''
