# Examples of Built in Functions

# abs(x)
print("abs(x)")
print("¨¨¨¨¨")
my_value = -11.55                             # Notice that my_value is a negative floating point number
absolute = abs(my_value )                     # Return the absolute value
print("The absolute value is:", absolute)
print("\n")


# len(x)
print("len(x)")
print("¨¨¨¨¨¨")
my_list = ["abs", "len", 1, 2, "many", "more to come"]      # Create a list called "my_list"
my_size = len(my_list)                                      # Return length (the number of items) of my_list
print("The length of my_list is:", my_size)
print("\n")

# max(iterable, *[, key, default])
# max(arg1, arg2, *args[, key])
print("max(x)")
print("¨¨¨¨¨¨")
my_list = [-10, 12, 111, 32.3, 0, 4, 24]                        # Create a list called "my_list"
my_max1 = max(my_list)                                          # Return the largest item in my_list
my_max2 = max(my_list[0], my_list[-1])                          # Return the largest among first & last element
print("The largest item of my_list is:", my_max1)               # Print my_max1 to see what was returned
print("The larger among first and last item is:", my_max2)
print("\n")



#min(iterable, *[, key, default])
#min(arg1, arg2, *args[, key])
print("min(x)")
print("¨¨¨¨¨¨")
my_list = [10, -12, 11, 32.3, 1, 14, -5]                         # Create a list called "my_list"
my_min1 = min(my_list)                                           # Return the smallest item in my_list
my_min2 = min(my_list[0], my_list[-1])                           # Return the smallest among first & last element
print("The smallest item of my_list is:", my_min1)               # Print my_min1 to see what was returned
print("The smaller among first and last item is:", my_min2)
print("\n")

# pow(x, y[, z])
print("pow(x)")
print("¨¨¨¨¨¨")
x = 5                                                   # initialize a variable x
y = 3                                                   # initialize a variable y
result = pow(x, y)                                      # Return x to the power of y. Same as x**y
print("The result of the operation is", result)
print("\n")

# sorted(iterable[, key][, reverse])
print("sorted(x)")
print("¨¨¨¨¨¨¨¨¨")
# Lets sort the following list by the first item in each sub-list.
my_list = [[2, 4], [0, 13], [11, 14], [-14, 12], [100, 3]]
# First, we need to define a function that specifies what we would like our items sorted by
def my_key(item):
    return item[0]                                            # Make the first item in each sub-list our key
new_sorted_list = sorted(my_list, key=my_key)                 # Return a sorted list as specified by our key
print("The sorted list looks like:", new_sorted_list)
print("\n")


# sum(iterable[, start])
print("sum(x)")
print("¨¨¨¨¨¨")
my_list = [1, 2, 3, 4, 5]                        # Create a list
my_sum  = sum(my_list)                           # Return the sum of the list
print("The sum of my list is :", my_sum)         # Print my_sum
print("\n")


# zip(*iterables)
print("zip(x)")
print("¨¨¨¨¨¨")
x = [1, 2, 3, 4, 5]                                      # Create a list
y = ['a', 'b', 'c']                                      # Note that this list only has 3 elements
zipped = list(zip(x, y) )                                # Return the zipped object as a list of tuples
print("The result of the operation is:", zipped)





