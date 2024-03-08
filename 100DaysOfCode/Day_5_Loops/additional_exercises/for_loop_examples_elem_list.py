# For loop examples


#### If you want to go over a sequence of objects such as the elements
# of a list

#1
my_books = ["python", "java", "c++", "ruby","html"]
for x in my_books:
    print(x)
print("No more books on the shelf.")
print("") # Line jump


#2
my_books = ["python", "java", "c++", "ruby","html"]
number_of_books = 0

for current_book in my_books:
    number_of_books = number_of_books + 1
    print("Title", number_of_books, "/", current_book)
print("No more books on the shelf.")
print("") # Line jump



#### If you want to repeat a piece of code n times

#1
my_numbers = [1,2,3,4,5,6,7,8,9,10]
for current_number in my_numbers:
    print("Hello")
print("") # Line jump
    

#2
# if you want to repeat something n times
# use range fn 
for current_number in range(1,11): # from 1 to 10
    print(current_number, " Hello")
print("") # Line jump


#3
# start value can 
# use range fn. range(start_value, end_value)
# if you want to go from 1 to 10 -> range(1,10)
for current_number in range(90,101): # from 90 to 100
    print(current_number, " Hello")
