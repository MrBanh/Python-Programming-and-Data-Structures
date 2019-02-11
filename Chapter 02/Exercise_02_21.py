'''
Financial application: compound value)
Suppose you save an $x.xx amount each month into a savings account with an
annual interest rate of 5%. Therefore, the monthly interest rate is
0.05 / 12=0.00417. Write a program that prompts the user to enter a
monthly saving amount and displays the account value after the sixth month.
'''

ANNUAL_INTEREST_RATE = 5 / 100      # 5% Interest rate
month_interest_rate = ANNUAL_INTEREST_RATE / 12
Num_of_months = 6
balance = 0.00

monthly_saving = float(input('Enter monthly saving amount: '))
monthly_saving = (int(monthly_saving * 100)) / 100.00

for i in range(Num_of_months):
    balance = round((monthly_saving + balance) * (1 + month_interest_rate), 2)

print(f'After the {Num_of_months}th month, the account value is {balance}')
