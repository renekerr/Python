# This program test the use of methods for lists
"""
append()
extend()
insert()
remove()
copy()
pop()
clear()
sort()
reverse()
count()
index()
"""



print('Main list')
x = ['cat', 'bird', 3, 41, 'mouse']
print(x , "\n")


# list.append(x)	Add an item to the end of the list
print('Example_1')
x.append('dog')
print(x)
print("\n")


# list.extend(L)	Extend the list by appending all the items in the given list
print('Example_2')
L = [100, 'madness', 99.9, 'last']
print('Another list')
print(L)

x.extend(L)
print(x)
print("\n")


# list.insert(i, x) Insert an item at a given position. The first argument is the index of the element to insert.
print('Example_3')
x.insert(1,'item inserted')
print(x)
print("\n")


# list.remove(x) Remove the first item from the list whose value is x. It is an error if there is no such item.
print('Example_4')
x.remove('madness')
print(x)
print("\n")

# list.copy() Return a shallow copy of the list.
print('Example_5')
x.copy()
print(x)
print("\n")


# list.pop([i])	Remove the item at the given position and return it. If no index is specified, removes the last item.
print("Example_6")
x.pop(8)
print(x)
print("\n")

# list.clear()	Remove all items from the list
print("Example_7")
x.clear()
print("Elements of list cleared ",x)
print("\n")


y = ['item1', 20, 'item2', 30]
print("New list created")
print(y)
print("\n")

# list.index(x)	Return the index in the list of the first item whose value is x. It is an error if there is no such item.
print("Example_8")
pos = y.index('item2')
print(pos)
print("\n")

# list.count(x)	Return the number of times x appears in the list.
y = y = ['item1', 20, 'item2', 30, 20]
print("Example_9")
c = y.count(20)
print(c)
print("\n")


# list.reverse()	Reverse the elements of the list in place.
print("Example_10")
y.reverse()
print(y)
print("\n")

# list.sort
print("Example_11")
z = [5,4,3,2,1]
print("Another list created")
print("z = ", z, "\n")
z.sort()
print("z sorted")
print(z)
print("\n")

# list.sort(key=None, reverse=False)
# This method sorts the items of the list in place. Note that this method does not return anything.
# (The arguments are optional and can be used for sort customization, see sorted() for their explanation.)
print("Example_12")
my_list = [5, 3, 6, 1, 2, 4, 7]
my_list.sort()                                   # Sort the items of the list in place
print("Sorted list looks like:", my_list)




















































