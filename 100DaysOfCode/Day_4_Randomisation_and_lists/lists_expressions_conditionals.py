# Quiz 2, Part 2
# These pieces of code shows the use of lists, expressions, conditional if-elif-else

#1
a = 14 // 3
b = 4 > 5
print( a and b)


#2
x = False
y = 0 > 10
print(y or x)


#3
x = ['cat', 2.5, 'dog']
y = 'cat' in x
print(y)


#4
x = "python course"
print("cours" not in x )


#5
my_list = [ 13, 'cat', 5.6, 'cow']
if 'dog' in my_list:
    print('bark')
else:
    print('meow')


#6
    my_list = [ 'dog', 'cat', 'worm', 2.3]
if 'doc' in my_list:
    my_list[1] = 4
else:
    my_list[2] = 6
print(my_list[1], my_list[2])

#7
x=10
if x>5:
    x= x+5
if x<12:
    x= x+5
if x == 15:
    x= x+5
print(x)

#8
x= 20
if True:
    x= x+10
if x == 20:
    x= x+30
else:
    x= x+40
print(x)


#9
x=4
if "z" in "computer science":
    x= x+10
elif 5%3 == 2:
    x= x+18
elif 5>4:
    x= x+30
else:
    x= x+5
print(x)
    

#10
x= "c"
y= 3
if "x" in "computer science":
    y= y+5
else:
    y= y+10

if x in "computer science":
    y= y+20
else:
    y= y+40
print(y)

















