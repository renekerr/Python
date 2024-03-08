# Write a program using while loop, which prints the sum of every third numbers
# from 1 to 1001 ( both 1 and 1001 are included)

m = 1
s = 0
while m <= 1001:
    s = s + m
    m = m + 3
print(s)

################### Sample Solution ###################
x = 1
count = 0
while x < 1001:
    count = count +x
    x = x + 3
print(count)


    




