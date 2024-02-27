# Continue and Break, Exercise 1

#1
print('Ex: 1')
count = 20
for x in range(0,10):
    count = count - 1
    if x == 2:
        break
print(count)


#2
print('Ex: 2')
k=1
while k<5:
     if k%7 == 0:
         break
     k = k + 2
print(k)


#3
print('Ex: 3')
my_list = ["dog", 24, "cat", 12]
count = 0
for element in my_list:
    if element == "cat":
        continue
    count = count + 1
print(count)
