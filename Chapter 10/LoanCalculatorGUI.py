from tkinter import *


class LoanCalculator:
    def __init__(self):
        window = Tk()       # Create a window
        window.title("Loan Calculator")     # Set title

        # Labels for GUI with Label()
        Label(window, text="Annual Interest Rate").grid(
            row=1, column=1, sticky=W)
        Label(window, text="Number of Years").grid(
            row=2, column=1, sticky=W)
        Label(window, text="Loan Amount").grid(
            row=3, column=1, sticky=W)
        Label(window, text="Monthly Payment").grid(
            row=4, column=1, sticky=W)
        Label(window, text="Total Payment").grid(
            row=5, column=1, sticky=W)

        # Get User Input with Entry()
        self.annual_interest_rate = StringVar()
        Entry(window, textvariable=self.annual_interest_rate,
              justify=RIGHT).grid(row=1, column=2)

        self.years = StringVar()
        Entry(window, textvariable=self.years,
              justify=RIGHT).grid(row=2, column=2)

        self.loan_amount = StringVar()
        Entry(window, textvariable=self.loan_amount,
              justify=RIGHT).grid(row=3, column=2)

        # Label to display results
        self.monthly_payment = StringVar()
        Label(window, textvariable=self.monthly_payment).grid(
            row=4, column=2, sticky=E)

        self.total_payment = StringVar()
        Label(window, textvariable=self.total_payment).grid(
            row=5, column=2, sticky=E)

        # Button, click to compute
        Button(window, text="Compute Payment", command=self.compute_payment).grid(
            row=6, column=2, sticky=E)

        window.mainloop()

    # Calculates the monthly payment and the total payment
    def compute_payment(self):
        calc_monthly_payment = self.get_monthly_payment(
            float(self.loan_amount.get()),        # Loan amount
            float(self.annual_interest_rate.get()) / 1200,      # monthly rate
            int(self.years.get())       # num of years
        )

        # Change the values in the monthly payment and total payment
        self.monthly_payment.set(format(calc_monthly_payment, "10,.2f"))
        self.total_payment.set(
            format(int(calc_monthly_payment * 100) / 100 * 12 * int(self.years.get()), "10,.2f"))

    # Calculates the monthly payment amount
    def get_monthly_payment(self, loan_amount, monthly_interest_rate, years):
        monthly_payment = (loan_amount * monthly_interest_rate) /\
            (1 - (1 / (1 + monthly_interest_rate)**(years * 12)))

        return monthly_payment


LoanCalculator()
