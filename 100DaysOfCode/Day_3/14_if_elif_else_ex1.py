# Set of exercises to learn the use of conditional if-elif-else

# 1
my_list=[ 2.3, 'car', 12, 46, 'cat']
if 12 in my_list:
    print('hello')
elif 6 > 4:
    print('bye')
else:
    print('nothing')
    

# 2
if 6/2:
    print('three')
elif 5:
    print('five')
else:
    print('zero')

    
# 3
if False:
    print('false')
elif 2**3 == 8:
    print('true')
else:
    print('none')
    
# 4
my_string = "hello"
if 10 % 5: # this expression would be False because the result is 0 (10%5)
    print('true')
elif "le" not in my_string:
    print('false')
else:
    print('none')


# 5
if 6<5:
    print('one')
elif 7==9:
    print('two')
print("three")
