# Conditional if else examples II
# These are examples of the use of conditional if-else

# 1
my_list = [ "cat", 2, "dog", 4]
if 2 in my_list:
    print('yes')
else:
    print('no')


# 2
my_list = [ "cat", 2, "dog", 4]
x = 5 in my_list

if x:
    print('yes')
else:
    print('no')


# 3
my_list = [ 'dog', 'cat', 'worm', 'cow']
if 'dog' not in my_list:
    print('true')
else:
    print('false')
    

# 4
my_list = [ 'dog', 'cat', 'worm', 'cow']
if 'car' in my_list:
    print('true')
else:
    print('false')

# 5
my_list = [ 'dog', 'cat', 'worm', 'cow']
if 'w' in my_list:
    print('true')
else:
    print('false')
