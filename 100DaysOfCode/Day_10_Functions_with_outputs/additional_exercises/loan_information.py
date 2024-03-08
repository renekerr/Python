# Assignment 1. Part 3
# Part 3: Display Loan Information


# Part 1: Calculate monthly payments for a loan
def monthly_payments_loan(principal, annual_interest_rate, duration):

    if annual_interest_rate == 0:
        return principal / (duration*12)

    r = (annual_interest_rate/100)/12  # monthly interest rate
    n = duration * 12
    monthly_payment = principal * ((r*(1+r)**n)/(float((1+r)**n)-1))

    return monthly_payment



# Part 2: Calculate the remaining balance of a loan
def balance_payments_loan(principal, annual_interest_rate, duration, number_of_payments):

    if annual_interest_rate == 0:
        return principal * (1-(number_of_payments/(duration*12)))


    r = (annual_interest_rate/100)/12  # monthly interest rate
    n = duration * 12
    p = number_of_payments

    remaining_loan_balance = principal * ((1.0+r)**n - (1.0+r)**p)/(((1.0+r)**n) - 1)

    return remaining_loan_balance



# Main program
principal = float(input("Enter loan amount: "))
annual_interest_rate = float(input("Enter annual interest rate (percent): "))
duration = int(input("Enter loan duration in years: "))

month_pay = int(monthly_payments_loan(principal, annual_interest_rate, duration))

print("")
print("LOAN AMOUNT:", principal, "INTEREST RATE (PERCENT):", annual_interest_rate)
print("DURATION (YEARS):", duration, "MONTHLY PAYMENT:", month_pay)

for year_number in range(1,duration+1):
    y = balance_payments_loan(principal, annual_interest_rate, duration, year_number*12)
    print("YEAR:", year_number, "BALANCE:", int(y), "TOTAL PAYMENT:", int(month_pay*year_number*12))













