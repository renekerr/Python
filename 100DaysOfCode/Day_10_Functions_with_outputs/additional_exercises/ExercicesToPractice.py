# Question 1: Accept two integer numbers from a user and return their product and  if the product is greater than 1000, then return their sum
print('# Question 1\n')

def multip_sum(num1, num2):
    product = num1 * num2
    sum_numbers = num1 + num2

    if product > 1000:
        return sum_numbers
    else:
        return product

num1 = int(input('Enter first number : '))
num2 = int(input('Enter second number : '))

result = multip_sum(num1, num2)
print('Result = ', result)


#Question 2: Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current number and previous number
print('# Question 2\n')
def sum(num):
    previous_number = 0
    for i in range(num):
        s = previous_number + i
        print ('Current number = ', i, 'Previous number :', previous_number, 'Sum : ', s)
        previous_number = i

result = sum(10)

# Question 3: Accept string from a user and display only those characters which are present at an even index number.
print('# Question 3\n')
def even_ix_number(string):
    for i in range(0, len(string)-1, 2):
        print('index[', i,'] ', string[i], sep='')

string = input('Enter a string : ')
print('String entered by user : ', string)

print('Printing only even index chars: ')
even_ix_number(string)

# Question 4: Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string
# For example, removeChars("pynative", 4) so output must be tive. Note: n must be less than the length of the string.
print('# Question 4\n')
def remove_chars(text, n_chars):
    result = text[n_chars:]
    return result

text  = input('Enter text : ')
n_chars = int(input ('Enter number of chars: '))
print(remove_chars(text, n_chars))

#Question 5: Given a list of numbers, return True if first and last number of a list is same
print('# Question 5\n')
def first_last_numbers_inn_list(list):
    first_num = list[0]
    last_num = list[-1]
    fl = [first_num, last_num ]
    print('Given list : ', list)
    print('The first and last element of list are : ', fl)
    if first_num == last_num:
        print('First and last element are same!')
        return True
    else:
        print('First and last element are not the same!')
        return False

numbers = [10, 20, 30, 40, 80]
print(first_last_numbers_inn_list(numbers))

# Python3 code to demonstrate
# to get first and last element of list
# using List slicing

# initializing list
test_list = ['First', 20, 30, 40, 80, 'Last']

# printing original list
print ("The original list is : " +  str(test_list))

# using List slicing
# to get first and last element of list
res = test_list[0::len(test_list ) -1]

# printing result
print ("The first and last element of list are : " +  str(res))

# Question 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
def div_by_five(numbers):
    print("Given list is ", numbers)
    print("Divisible of 5 in the list")
    for n in numbers:
        if n % 5 == 0:
            print(n)

nums = [10, 20, 33, 46, 55]
div_by_five(nums)

#-------------------------
text = 'revolution'
slicing = text[0::2]
print(slicing)

#-------------------------

#Question 7: Return the total count of string “Emma” appears in the given string
# “Emma is good developer. Emma is a writer”
def find_text(text, searchfor):
    text = text.lower()
    c = text.count(searchfor)
    print("Word '", searchfor, "' appear(s) ", c, " time(s).", sep='')

text = 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. She was blind, very blind, really blind'
s = input('Search for : ')
find_text(text, s)








