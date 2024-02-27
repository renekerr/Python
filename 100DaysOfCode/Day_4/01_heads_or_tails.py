'''
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out "Heads" or "Tails".

e.g. 1 means Heads 0 means Tails
'''
# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random
n = random.randint(0,1)
#print(n)
if n == 1: 
  print('Heads')
else: 
  print('Tails')