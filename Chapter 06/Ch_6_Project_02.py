'''
(Financial application: compute the future investment value)

Write a function that computes a future investment value at a given interest
rate for a specified number of years. The future investment is determined
using the formula in Programming Exercise 2.19 in Chapter 2 Programming
Exercise from the Book.

Use the following function header:

def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):

For example, futureInvestmentValue(10000, 0.05/12, 5) returns 12833.59.

Write a test program that prompts the user to enter the investment amount and
the annual interest rate in percent and prints a table that displays the
future value for the years from 1 to 30.
'''


def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    future_value = investmentAmount

    for i in range(1, years + 1):
        future_value = (future_value * (1 + (monthlyInterestRate / 100)) ** 12)
        print(i, format(future_value, ".2f"))


def main():
    invested = float(input("The amount invested: "))
    annual_interest = float(input("Annual interest rate: "))

    print("Years Future Value")
    futureInvestmentValue(invested, annual_interest/12, 30)


main()
