# Assignment 1. Part 1
# Part 1: Calculate monthly payments for a loan

def monthly_payments_loan(principal, annual_interest_rate, duration):

    if annual_interest_rate == 0:
        return principal / (duration*12)

    r = (annual_interest_rate/100)/12  # monthly interest rate
    n = duration * 12
    monthly_payment = principal * ((r*(1+r)**n)/(float((1+r)**n)-1))

    return monthly_payment


# Main program
principal = 1000.0
annual_interest_rate = 4.5
duration = 5

s = monthly_payments_loan(principal, annual_interest_rate, duration)

print(s)
