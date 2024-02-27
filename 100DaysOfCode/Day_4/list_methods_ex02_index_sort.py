# List Methods, Exercise 2
# list.index()
# list.sort()

#1
print('#1')
my_list = [4, 'two' , 'one' ,5,3,2,'bye']
print (my_list.index('one'))
print('\n')

#2
print('#2')
MyList = ['pet' , 'dog' ,5, 'cat', 'good','dog']
print (MyList.index(5))
print('\n')

#3
print('#3')
MyList = ['pet' , 'dog' ,5, 'cat', 'good','dog']
print (MyList.index('dog'))
print('\n')

#4
## ERROR ##
print('#4')
#MyList = ['pet' , 'dog' ,5, 'cat', 'good','dog']
#print (MyList.index('car')) # car is not on the list
print('ERROR / car is not on the list')
print('\n')

#5
# Sort is an inplace operation and it does not return anything.
print('#5')
MyList = [1, 5, 67, 3, 4]
x = MyList.sort()
print (x)
print('Sort is an inplace operation and it does not return anything \n')
print('List should be printed')
print(MyList)
print('\n')



