# Assignment 1. Part 2
# Part 2: Calculate the remaining balance of a loan

def monthly_payments_loan(principal, annual_interest_rate, duration, number_of_payments):

    if annual_interest_rate == 0:
        return principal * (1-(number_of_payments/(duration*12)))


    r = (annual_interest_rate/100)/12  # monthly interest rate
    n = duration * 12
    p = number_of_payments

    remaining_loan_balance = principal * ((1.0+r)**n - (1.0+r)**p)/(((1.0+r)**n) - 1)

    return remaining_loan_balance



# Main program
principal = 1000.0
annual_interest_rate = 4.5
duration = 5
number_of_payments = 12

s = monthly_payments_loan(principal, annual_interest_rate, duration, number_of_payments)

print(s)

