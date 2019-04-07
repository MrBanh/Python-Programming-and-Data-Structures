'''
Name of the program: Compare_Interest_Rates.py
Python Version (e.g. Python 3.6.0): Python 3.7.2
Your name: Tony Banh
Student id: 0740162
Date: 04/05/2019
Platform (PC, Mac, or Linux machine): Windows 10 PC

Exercise: 10.17 (Compare loans with various interest rates)

Description: program should let the user enter the loan amount and loan period
in the number of years from a text field, and should display the monthly and
total payments for each interest rate starting from 5 percent to 8 percent,
with increments of one-eighth, in a text area.

'''
from tkinter import *


class Compare_Interest:
    def __init__(self):
        window = Tk()       # Create a window
        window.title("Compare Interest Rates")      # Title the window

        # Create a frame
        frame = Frame(window)
        frame.pack(anchor=CENTER)

        # Loan amount label and entry
        self.loan_amount_var = StringVar()
        Label(frame, text="Loan Amount").grid(row=1, column=1)
        Entry(frame, textvariable=self.loan_amount_var,
              justify=RIGHT).grid(row=1, column=2)

        # Year Label and Entry
        self.years_var = StringVar()
        Label(frame, text="Years").grid(row=1, column=3)
        Entry(frame, textvariable=self.years_var,
              justify=RIGHT).grid(row=1, column=4)

        # Calculate button
        Button(frame, text="Calculate",
               command=self.compare_interest_rates).grid(row=1, column=5)

        # Listbox to display results
        self.listbox = Listbox(window)
        self.listbox.pack(fill=BOTH, expand=1)
        self.listbox.insert(END, f"{'Interest Rate':<40s}" +
                            f"{'Monthly Payment':<40s}" +
                            f"{'Total Payment':<40s}")

        # Start the event loop
        window.mainloop()

    def compare_interest_rates(self):
        interest_rate = 5     # Starting interest rate of 5% APR
        loan = float(self.loan_amount_var.get())
        years = int(self.years_var.get())
        n = years * 12      # Number of payments

        for _ in range(25):
            # Convert to monthly rate in decimal
            monthly_rate = interest_rate / 1200

            # Calculate monthly payment
            monthly_payment = loan * \
                ((monthly_rate * (1 + monthly_rate) ** n) /
                 (((1 + monthly_rate) ** n) - 1))

            # Calculate total payment
            total_payment = monthly_payment * n

            # Append results to listbox
            self.listbox.insert(END, f"{interest_rate:<45.2f}" +
                                f"{monthly_payment:<53.2f}" +
                                f"{total_payment:<45.2f}")

            # Increment interest rate
            interest_rate += (1/8)


Compare_Interest()
