# Nested Loops, Exercise 3
# This are examples of nested for loops


#1
print("Ex_1")
m = 1
for x in [1,2,3]:
    for y in [3,1,4]:
        if x == y:
            m = m * x
print("m =", m,"\n")


#2
print("Ex_2")
m = 1
my_list_1 = [2,4,1]
for x in my_list_1:
    for y in range(1,3):
        if (x+y)%3:
            m = m * x
print("m =", m,"\n")


#3
print("Ex_3")
m = 0
my_str_1 = "university"
my_str_2 = "mississipy"
for char_1 in my_str_1:
    for char_2 in my_str_2:
        if char_1 == char_2:
            m = m + 1
print(m)

