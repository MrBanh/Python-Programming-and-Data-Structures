'''
(Financial application: investment amount)
Suppose you want to deposit a certain amount of money into a savings account
with a fixed annual interest rate. Write a program that prompts the user to
enter the final account value, the annual interest rate in percent, and the
number of years, and then displays the initial deposit amount.

initial_deposit =  future_value / ((1.00 + i) ** n)

future_value = final account value
i = monthly interest rate
n = number of months
'''

future_value = float(input('Enter final account value: '))
future_value = (int(future_value * 100)) / 100.00

annual_interest_rate = float(input('Enter annual interest rate, e.g. 8.25: '))
monthly_interest_rate = annual_interest_rate / 1200

number_of_years = int(input('Enter number of years: '))
number_of_months = number_of_years * 12

initial_deposit = future_value / \
                  ((1 + monthly_interest_rate) ** number_of_months)

initial_deposit = round(initial_deposit, 2)

print(f'Initial deposit value is {initial_deposit}')
