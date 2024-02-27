n = int(input('Enter integer number [1-9999]: '))

list_01_09 = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
list_10_19 = ['ten', 'eleven','twelve', 'thirteen','fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
list_20_90 = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

result = ""

if n == 0:
    print('zero')


first_digit  = n // 1000                # Thousands
second_digit = (n % 1000) // 100        # Hundreds
third_digit  = (n % 100) // 10          # Tens
fourth_digit   = (n % 10)               # Ones



#print(first_digit, second_digit, third_digit, fourth_digit)


if first_digit > 0:
    result = result + list_01_09[first_digit] + ' thousand '
    #print(result)

if second_digit > 0:
    result = result + list_01_09[second_digit] + ' hundred '
    #print(result)

if third_digit > 1:
    result = result + list_20_90[third_digit] + ' '
    #print(result)


if third_digit == 1:
    result =  result + list_10_19[fourth_digit] + ' '
    #print(result)

else:
    if fourth_digit:
        result = result + list_01_09[fourth_digit] + ' '
        #print(result)

# This conditional checks whether there is an empty space at the end of the string
# in order not to show it.
if result[-1] == " ":
    result = result[0:-1]


print(result)
