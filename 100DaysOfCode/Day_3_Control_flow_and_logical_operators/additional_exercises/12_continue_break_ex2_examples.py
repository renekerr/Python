# Continue and break, Exercise 2

#1
my_str = "university"
count = 0
for char in my_str:
    if char == "i":
        continue
    else:
        count = count + 1
print(count)


#2
my_str = "university"
count = 0
for char in my_str:
    count = count + 1
    if char == "e":
        break
print(count)


#3
my_list = [6, 5, 7, 2, 3, 5, 7, 8] 
count = 0
for number in my_list:
    if number == 5 or number == 7:
        continue
    else:
        count = count + number
print(count)
