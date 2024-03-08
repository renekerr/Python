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

print(my_list)
print(my_list[: :2])
print('\n')


#3
print('#3')
def append_sublists(x):
    for k in range (len(x)):
        x.append(x[:k+1])         
m = [1,5,3]
append_sublists(m)
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



#6
print('#6')
def delete_items(my_list, s, e):
    del(my_list[s:e])

values = [2, 9, 16, 3, 24, 13, 15]
delete_items(values, -6, -4)
print(values)
delete_items(values, 2,4)
print(values)
print('\n')

#7
print('#7')
def add_items(i):
    values = []
    values.append(i)
    return values

print(add_items(5))
print('\n')


#8
'''
This code extracts elements from the input list that are divisible by 3 but not by 2, and inserts them into a new list
'''
print('#8')
def insert_item(m):
    x = []
    for k in range(len(m)):
        if m[k] % 3 == 0 and m[k] % 2:
            x.insert(k, m[k])
    return x

values = [2, 9, 16, 3, 24, 13, 15]
print(insert_item(values))
print('\n')


#9
'''
This code increments each element of the input list values by the specified increment value and prints the modified list
'''
print('#9')
def increment_value(m, increment):
    x = 0
    while x < len(m):
        m[x] = m[x] + increment
        x = x + 1
    return m

values = [4, 3, 7]
print(increment_value(values, 2))
print('\n')


#10
print('#10')
def remove_integer(m):
    x = m[:]
    for k in x:
        if type(k) == int:
            m.remove(k)

values = [3, [3,4], 2.9, 3, 6, 'dog', 5]
remove_integer(values)
print(values)















