"""
Strings, Exercise 2

What will be printed after each of the following code segments? If error, then write Error
These examples show how to use/manipulate strings
"""

print('Example1')
x = "abcdefg"
print (x[-5:4])         # IT STARTS FROM INDEX -5 (C) TO INDEX 3 (D).
print('\n')

print('Example2')
x = "abcdefg"
print (x[5:1:-2])       # IT STARTS FROM INDEX 5 (F) TO INDEX 2(C), THE STEP IS -2
print('\n')             # WHICH MEANS YOU SHOULD SELECT BACKWARD EVERY OTHER TWO ELEMENTS.


print('Example3')
x = "abcdefg"
print (x[-6:len(x):2])  # LENGTH OF THE STRING IS 7 SO IT STARTS FROM INDEX -6 (B) TO INDEX 6 (G) IN SEP OF 2
print('\n')

print('Example4')
x = "abcdefg"
print (x[-4:-1:2])      # IT STARTS FROM INDEX -4 (D) TO INDEX -2 (F) IN STEP OF 2.
print('\n')