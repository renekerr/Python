# Nested Loops, Exercise 1
# These are examples of nested loops

#1
print("Ex_1")
m = 0
for x in range(1,4):
    for y in range(1,3):
        m = m + 1
        print("x=",x, "", "y=", y, "", "m=", m)
print("m =", m,"\n")

#2
print("Ex_2")
m = 0
for x in range(1,3):
    for y in range(4,6):
        m = m + x + y
        print("x=",x, "", "y=", y, "", "m=", m)
print("m =", m,"\n")


#3
print("Ex_3")
m = 0
for x in range(1,3):
    k = 0
    for y in range(-2,0):
        k = k + y
        m = m + k
print("m =", m,"\n")

#4
print("Ex_4")
m = 0
for x in [3,5,3]:
    for y in range(10,11):
        m = m + x + y
print("m =", m,"\n")
