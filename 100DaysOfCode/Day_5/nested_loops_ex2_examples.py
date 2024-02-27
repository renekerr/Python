# Nested Loops, Exercise 2
# This are examples of nested while loops

#1
print("Ex_1")
m = 0
x = 1
while x < 4:
    y = 1
    while y < 3:
        m = m + x + y
        y = y + 1
        #print("x=",x, "", "y=", y, "", "m=", m)
    x = x + 1
print("m =", m,"\n")

#2
print("Ex_2")
m = 0
x = 1
while x < 4:
    y = 1
    while y < 5:
        m = m + y
        y = y + 1
        if x+y == 5:
            break
    x = x + 1
print("m =", m,"\n")

#3
print("Ex_3")

m = 0
x = 10
while x > 8:
    for y in range(1,3):
        m = m + 1
    x = x - 1
print("m =", m,"\n")


