'''
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
The last line of your program should print the result.
'''
two_digit_number = input('Please enter a two-digit number: ')
# Write your code below this line 👇
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
sum_two_digits = first_digit + second_digit
print(sum_two_digits)
