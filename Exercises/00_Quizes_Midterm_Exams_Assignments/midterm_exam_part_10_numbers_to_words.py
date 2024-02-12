"""
Define Functions
¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

These functions decompose entered number into thousands, hundreds, tens and ones.
"""


# decompose_thousands()
def decompose_thousand(n):
    a = int(n/1000)*1000
    return a

# decompose_hundreds()
def decompose_hundreds(n, a):
    b = n - a
    b = int(b/100)*100
    return b

# decompose_tens()
def decompose_tens(n, a, b):
    c = n - a - b
    c = int(c/10)*10
    return c

# decompose_ones()
def decompose_ones(n, a, b, c):
    d = n - a - b - c
    return d



"""
These functions convert/return string value from integer number entered###
"""
def output_ones(n, list_01_09):                 # Ones[01-09]
    ones_string = list_01_09[n-1]
    return ones_string


def output_teens_numbers(fn4, list_10_19):      # Teens [10-19]
    teens_numbers_string = list_10_19[fn4]
    return teens_numbers_string


def output_tens(fn3, list_20_99):
    z = int(fn3/10)
    tens_string = list_20_99[z-2] + ' '
    return tens_string

def output_hundreds(fn2, list_01_09):
    y = int(fn2/100)
    hundreds_string = list_01_09[y-1] + ' hundred '
    return hundreds_string

def output_thousands(fn1, list_01_09):
    x = int(fn1/1000)
    thousands_string = list_01_09[x-1] + ' thousand '
    return thousands_string



"""
Main Program
¨¨¨¨¨¨¨¨¨¨¨¨
"""
n = int(input('Enter integer number [1-9999]: '))


fn1 = decompose_thousand(n)                 # Thousands
fn2 = decompose_hundreds(n, fn1)            # Hundreds
fn3 = decompose_tens(n, fn1, fn2)           # Tens
fn4 = decompose_ones(n, fn1, fn2 , fn3)     # Ones

list_01_09 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
list_10_19 = ['ten', 'eleven','twelve', 'thirteen','fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
list_20_90 = [ 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


# x for thousands
# y for hundreds
# z for tens
# w for ones

# Numbers in range 01 - 09
if 1 <= n <= 9:
    ones = output_ones(n, list_01_09)
    print(ones)

# Numbers in range 10 - 19
if 10 <= n <=19:
    ones_teens = output_teens_numbers(fn4, list_10_19)
    print(ones_teens)

# Numbers in range 20 and 99
if 20 <= n < 100:

    # If 'ones' is equal to 0 (tens are equal to 20, 30, 40, ....)
    if fn4 == 0:
        tens = output_tens(fn3, list_20_90)
        print(tens)

    # If 'ones' is NOT equal to 0, i.e.: 78, 23, 98,....)
    else:
        tens = output_tens(fn3, list_20_90) + ' ' + output_ones(fn4, list_01_09)
        print(tens)



# Numbers in range 100 - 999
if 100 <= n <= 999:

    # If n is equal to 100, 200, 300,...
    if fn3 == 0 and fn4 == 0:
        hundreds = output_hundreds(fn2, list_01_09)
        print(hundreds)

    # If n is equal to 101, 203, 408, 907,...
    elif fn3 == 0 and 1 <= fn4 <=9 :
        hundreds = output_hundreds(fn2, list_01_09) + output_ones(fn4, list_01_09)
        print(hundreds)

    # If n is equal to 910, 811, 716,....
    elif fn3 == 10:
        hundreds = output_hundreds(fn2, list_01_09) + output_teens_numbers(fn4, list_10_19)
        print(hundreds)

    # If n is equal to 340, 280, 870,...
    elif fn4 == 0:
        hundreds = output_hundreds(fn2, list_01_09) + output_tens(fn3, list_20_90)
        print(hundreds)

    # If 'ones' is NOT equal to 0, i.e.: 178, 523, 798,....)
    else:
        hundreds = output_hundreds(fn2, list_01_09) + output_tens(fn3, list_20_90) + output_ones(fn4, list_01_09)
        print(hundreds)




# Numbers in range 1000-9999
if 1000 <= n <= 9999:

    # If n is equal to 1000, 2000, 3000,....
    if fn2 == 0 and fn3 == 0 and fn4 == 0:
        thousands = output_thousands(fn1, list_01_09)
        print(thousands)

    # If n is equal to 1001, 2007, 7009,....
    elif fn2 == 0 and fn3 == 0:
        thousands = output_thousands(fn1, list_01_09) + output_ones(fn4, list_01_09)
        print(thousands)

    # If n is equal to 2016, 3018, 1011,....
    elif fn2 == 0 and fn3 == 10:
        thousands = output_thousands(fn1, list_01_09) + output_teens_numbers(fn4, list_10_19)
        print(thousands)

    # If n is equal to 9020, 7080,1050,....
    elif fn2 == 0 and fn4 == 0 and fn3 != 0:
        thousands = output_thousands(fn1, list_01_09) + output_tens(fn3, list_20_90)
        print(thousands)

    # If n is equal to 6051, 4076, 9099,....
    elif fn2 == 0:
        thousands = output_thousands(fn1, list_01_09) + output_tens(fn3, list_20_90) + output_ones(fn4, list_01_09)
        print(thousands)

    else:
        thousands = output_thousands(fn1, list_01_09) + output_hundreds(fn2, list_01_09) + output_tens(fn3, list_20_90) + output_ones(fn4, list_01_09)
        print(thousands)


