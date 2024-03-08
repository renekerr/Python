#Quiz 3, Part 2
# These pieces of code test the use of functions, loops, conditionals and expressions

#1
def say_hello():
    print('Hello World!')
say_hello()

#2
def func(x):
    x = 2
    print('x is', x)
func(50)

#3
def even(x):
    if x % 2 == 0:
        return x
    else:
        return x+1
print(even(3))

#4
def cube(x):
    return x * x * x
y = cube(3)
print(y)

#5
#ERROR
#def fun(x, y, z):
#   z = x * y
#   return x + y + z
#print(fun(2, 30))


#6
def find_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')
find_max(3, 4)

#7
def count_item(x):
    count = 0
    for str in x:
        if str == "cat":
            count = count + 1
        elif str == "dog":
            count = count - 1
    return count
z = ['cat', 2, 'cat', 'dog', 34, 'cat']
print(count_item(z))

#8
def test_function():
    count = 0
    for x in range (0,3):
        count = count + x
    return
print(test_function())

#9
def function_call(x,y):
   z = multiply(x,y)
   m = x + z
   return m

def multiply(a,b):
   n = a * b
   return n

x = 2
y = 4
z = function_call(x,y)
print (x,y,z)

#10
def function_check(x):
    for m in range(0,3):
        n = 2
        while n <= 4:
            if m == n:
                x = x + 1
            n = n + 1
    return x
print(function_check(5))


