'''
(Financial application: compare loans with various interest rates) 

Write a program that lets the user enter the loan amount and loan period in
number of years and displays the monthly and total payments for each interest
rate starting from 5% to 8%, with an increment of 1/8.
'''

interest_rate = .05     # Starting interest rate of 5% APR

loan = float(input("Loan Amount: "))
years = int(input("Number of Years: "))
n = years * 12       # number of payments

for i in range(25):
    monthly_rate = interest_rate / 12       # interest rate / 12
    monthly_payment = loan * ((monthly_rate * ((1 + monthly_rate) ** n)) /
                            (((1 + monthly_rate) ** n) - 1))
    total_payment = monthly_payment * n
    print(format(interest_rate, ".3%"),
          format(monthly_payment, ".2f"),
          format(total_payment, ".2f"))
        
    interest_rate += ((1/8) / 100)
