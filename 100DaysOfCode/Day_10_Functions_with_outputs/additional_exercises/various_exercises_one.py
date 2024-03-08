"""
Midterm Exam, Part 1
What will be printed after each of the following code segments? If error, then write Error
"""

#1
print('#1')
x = ["dog", 2, "cat", 34, 5.8]
print('List')
print(x,'\n')

print('Lenght of list x is ',len(x))
m = 0
print('If we go from 1 to list length (for loop)' )
print('If  m = m + i')
for i in range(len(x)):
    m = m + i
    print('i =',i,'     m = ', m)
print('Final m is  ',m)
print('\n')

"""
Range examples:

>>>
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(range(0, 30, 5))
[0, 5, 10, 15, 20, 25]
>>> list(range(0, 10, 3))
[0, 3, 6, 9]
>>> list(range(0, -10, -1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> list(range(0))
[]
>>> list(range(1, 0))
[]

See more https://docs.python.org/3/library/stdtypes.html#range
"""


#2
print('#2')
def exponent_fn(x,y):
    exp = x ** y
    # Result is None, no 'return' any value(s)
    return exp

y = exponent_fn(2,3)
print(y)
print('\n')


#3
print('#3')
i = 1

while False:
    # This is a while loop with a condition that is always False. Therefore, the code inside the loop will never execute.
    if i % 5 == 0:
        break
    i = i + 2

print(i)
print('\n')

#4
print('#4')
count = 0
list_1 = []
for i in range(1,4):
    list_1.append(i**2)
for x in list_1:
    count = count + x
print(count)
print('\n')

#5
print('#5')
def modfiy_values(a):
    a[0] = 'new value:'
    a[1] = a[1] + 1

x = ['old value:', 99]
modfiy_values(x)
print (x[0], x[1])
print('\n')

#6
print('#6')
x = [ 2, "dog", 6, 4, "pet", 3, 9, "cat"]
count = 0

for item in x:
    m=0
    if item == "pet" or item == 3:
        m = x.index(item)
        count = count + m
print(count)
print('\n')

#7
print('#7')
count = 0
my_list = [2, 4, 1, 5, 7, 3, 9, 4]
new_list = my_list[1:7:2]   # List sliced new_list = [4, 5, 3]
for item in new_list:
    count = count + 1
print(count)
print('\n')

#8
print('#8')
x=0
my_list = []
while x < 10:
    if x % 2 == 0:
        my_list.append("dog")
    elif x % 3 == 0:
        my_list.remove("dog")
    x=x+1
print(my_list.count("dog"))
print('\n')


#9
print('#9')
list_1 = ["dog", 3, "cat" , 25, 2.4]
list_2 = ["car", 25, "dog" , 43]
count = 0
for item in list_1:
    if item in list_2:
        count = count + 1
print (count)
print('\n')

#10
print('#10')
def max_item_count(x):
    z=0
    for item in x:
        m = x.count(item)
        if m > z:
            z=m
    return z

y = ["cat", 4, "dog" , "cat" , 2, "cat", 2]
print (max_item_count(y))
print('\n')








