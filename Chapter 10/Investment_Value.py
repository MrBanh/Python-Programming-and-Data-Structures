'''
Name of the program: Investment_Value.py
Python Version (e.g. Python 3.6.0): Python 3.7.2
Your name: Tony Banh
Student id: 0740162
Date: 04/05/2019
Platform (PC, Mac, or Linux machine): Windows 10 PC

Exercise: 10.2 (Create an investment-value calculator)

Description: Calculates the future value of an investment at a given interest
rate for a specified number of years.

    futureValue = investmentAmount * (1 + monthlyInterestRate) ** (years * 12)

'''
from tkinter import *


class Investment_Value:
    def __init__(self):
        window = Tk()       # Create a window
        window.title("Investment Calculator")       # Title the window

        # Create Labels with Label(), use .grid() to format where label goes
        Label(window, text="Investment Amount").grid(row=1, column=1, sticky=W)
        Label(window, text="Years").grid(row=2, column=1, sticky=W)
        Label(window, text="Annual Interest Rate").grid(
            row=3, column=1, sticky=W)
        Label(window, text="Future Value").grid(row=4, column=1, sticky=W)

        # Get user input with Entry()
        # Use StringVar() so the input field has empty for user
        self.investment_var = StringVar()        # Investment amount
        Entry(window, textvariable=self.investment_var,
              justify=RIGHT).grid(row=1, column=2)

        self.years_var = StringVar()        # Number of years
        Entry(window, textvariable=self.years_var,
              justify=RIGHT).grid(row=2, column=2)

        self.annual_rate_var = StringVar()        # Annual Interest Rate
        Entry(window, textvariable=self.annual_rate_var,
              justify=RIGHT).grid(row=3, column=2)

        # Label to show result
        self.future_val_var = StringVar()
        Label(window, textvariable=self.future_val_var).grid(
            row=4, column=2, sticky=E)

        # Button to invoke event and calculate result
        Button(window, text="Calculate", command=self.get_future_value).grid(
            row=5, column=2, sticky=E)

        # Start the main loop
        window.mainloop()

    # Calculates the future value of an investment
    def get_future_value(self):
        # Annual % to monthly rate as a decimal
        self.monthly_interest_rate = float(self.annual_rate_var.get()) / 1200

        # Calculate the future value and return it
        self.calc_future_val = float(self.investment_var.get(
        )) * (1 + self.monthly_interest_rate) ** (float(self.years_var.get()) * 12)

        # Show the future value in the label
        self.future_val_var.set(format(self.calc_future_val, ",.2f"))


Investment_Value()
