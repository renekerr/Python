# List Methods, Exercise 5
# list extend(), list.append(), list.pop(), list.remove(), list.insert()

#1
print('#1')
MyList = [3, "dog", 9, "cat"]
print(MyList.extend([7,8])) # Extends does not return anything.
print(MyList)
print('\n')

#2
print('#2')
MyList = ['pet', 'dog',5]
print (MyList.append('cat')) # Append does not return anything.
print(MyList)
print('\n')

#3
print('#3')
my_list=[1,"dog",2.3]
print(my_list.insert(2,"pet")) # Insert does not return anything.
print(my_list)
print('\n')

#4
print('#4')
my_list = ['two', 'one' ,5,3,2,'bye']
print (my_list.remove('one'))  # Remove does not return anything.
print(my_list)
print('\n')

#5
print('#5')
MyList = ['pet', 'dog' ,1]
print (MyList.pop(1))  # Pop deletes and returns the value of MyList[1] .
print(MyList)
print('\n')

#6
print('#6')
MyList = ['pet' , 'dog' ,5]
#print(MyList.pop('dog')) # pop only accepts integer as the index and not elements of the list.
## ERROR ##
print(MyList)
print('\n')


