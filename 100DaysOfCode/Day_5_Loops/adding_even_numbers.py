'''
You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:

i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.
'''

target = int(input('enter a number between 0 and 1000 '))
c = 0
if target > 0 and target < 1000:
  for number in range (0, target + 1):
    if number % 2 == 0:
         c+= number
print(c)

# another way to achieve same results
d = 0
if target > 0 and target < 1000:
    for number in range (2, target + 1, 2):
        d += number
print(d)



