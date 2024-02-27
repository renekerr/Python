"""
Midterm Exam, Part 2
What will be printed after each of the following code segments? If error, then write Error

NOTE: In some cases I modified or add some code in order to understand/analyze it better
"""

#1
print('#1')
my_list = []
for k in range(1,101,20):
    my_list.append(k)
print(my_list[: :2])
print('\n')

#2
print('#2')
def my_fun(x):
    print('length = ',len(x))
    for k in range(len(x)):
        print('k = ',k)
        x.extend(x[:k])         # Using append()
        print(x[:k])
m = [1,5,3]
my_fun(m)
print(m)
print('\n')


#3
print('#3')
def my_fun(x):
    for k in range (len(x)):
        x.append(x[:k])         # Using append()
m = [1,5,3]
my_fun(m)
print(m)
print('\n')

#4
print('#4')
my_list = [9, 8, 7]
print('my_list = ',my_list)

for k in range (3):
    print('k =',k, '-k =',-k, 'k+1 =', k+1)
    my_list.insert(-k, k+1)
    print(my_list, '\n')
print(my_list)
print('\n')


#5
print('#5')
my_list = [12, "cat", 3.4, "dog", 62]
new_list = []
for k in range(5):
    print('k=', k)
    if k % 2:
        print('if k%2 =', k%2)  # if k%2 is equal to 1 (True) / if k%2 is equal to 0 (False)
        m = my_list.pop(k)
        print('m = my_list.pop(k) =>',m)
        new_list.append(m)
print(new_list)
print('\n')

"""
my_list = [12, "cat", 3.4, "dog", 62]
0%2=0 False
1%2=1 True  m = my_list.pop(k=1) =>'cat' // my_list = [12, 3.4, "dog", 62]
2%2=0 False
3%2=1 True  m = my_list.pop(k=3) => 62   // my_list = [12, 3.4, "dog"]
4%2=0 False
"""


#6
print('#6')
def my_fun(my_list, s, e):
    del(my_list[s:e])

values = [2, 9, 16, 3, 24, 13, 15]
my_fun(values, -6, -4)
my_fun(values, 2,4)
print(values)
print('\n')


#7
print('#7')
def my_fun(i):
    values = []
    values.append(i)
    return values

my_fun(5)
print(my_fun(3))
print('\n')


#8
print('#8')
def my_fun(m):
    x = []
    for k in range(len(m)):
        if m[k] % 3 == 0 and m[k] % 2:
            x.insert(k, m[k])
    return x

values = [2, 9, 16, 3, 24, 13, 15]
print(my_fun(values))
print('\n')


#9
print('#9')
def my_fun(m, increment):
    x = 0
    while x < len(m):
        m[x] = m[x] + increment
        x = x + 1
    return m

values = [4, 3, 7]
print(my_fun(values, 2))
print('\n')


#10
print('#10')
def my_fun(m):
    x = m[:]
    for k in x:
        if type(k) == int:
            m.remove(k)

values = [3, [3,4], 2.9, 3, 6, 'dog', 5]
my_fun(values)
print(values)















