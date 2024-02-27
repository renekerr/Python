# List Methods, Exercise 6

#1
print('#1')
my_list = []
for x in range(2,11,3):
    my_list.append(x)
print(my_list)
print('\n')

# El tipo range con tres argumentos se escribe range(m, n, p) y crea una lista que empieza en m
# y acaba antes de llegar a n, avanzando de p en p

#2
print('#2')
my_list = []
# for x in range(4,30,3.0):
#       my_list.append(x)
print('TypeError: float object cannot be interpreted as an integer')
# print(my_list)
print('\n')


#3
print('#3')
a = range(3,20,4)
b = []
for k in a:
    if k % 2: #
        j= k % 2
        print(j)
        b.append(k)
print (b)
print('\n')

#4
print('#4')
my_list = []
for x in range(1,10):
    if not (x % 3):
        my_list.append(x)
print(my_list)







