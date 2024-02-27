# Write a program which prints the sum of numbers from 1 to 101
# ( 1 and 101 are included) that are divisible by 5 (Use while loop)

m = 0
s = 0
while m <= 100:
    
    m= m + 1
    d= m % 5

    if d == 0:
        s = s + m
    
print(s)

################### Sample Solution ###################

x=0
count=0
while x <= 101:
    if x%5==0:
        count = count+x
    x=x+1
print(count)



    
