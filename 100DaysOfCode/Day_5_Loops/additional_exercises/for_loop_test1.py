# Testing for loops

# Example_1
print("Example_1\n")
m = 0
for x in [3,5,3]:
    m = m + x
    print(x)
print(m,"\n")

# Example_2
print("Example_2\n")
for x in range(1,2):
    print(x)



# Example_3
print("Example_3\n")
my_list = [300,2,0,32,1100]
max_value = my_list[0] # assume that first element of the list is maximum

print("List of elements = ", my_list)


for x in my_list:
    if x > max_value:
        max_value = x
print("Maximun element of the list is", max_value)








