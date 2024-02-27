# Set of exercises to learn how conditional if-elif-else works

# 1
x = 0
if 5 in [1, 2, 3, 4]:
    x= x+1
elif 4==2:
    x= x+2
elif 7>4:
    x= x+3
else:
    x= x+4
print(x)


# 2
x = 5
if 8%4:
    x= x-1
elif 3<4/2:
    x= x-2
elif "t": # Any string will be True
    x= x-3
else:
    x= x-4
print(x)


# 3
x= 12
if "x" in "meow" and 4>2+1:
    x= x/2
elif 6%2 != 0:
    x= x/3
elif 2 in ["cat" , "dog" ]:
    x= x/4
else:
    x= x+1
print(x)



