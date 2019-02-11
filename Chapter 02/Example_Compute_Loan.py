# Example_Compute_Loan.py - computes and siplay the monthly payment and
# total payment amounts based on user input: interest rate, loan amount,
# and # of years

# Prompt user for yearly interest rate
annual_interest_rate = float(input('Enter annual interest rate, e.g. 8.25: '))
monthly_interest_rate = (annual_interest_rate / 100) / 12

# Prompt for number of years
number_of_years = int(input('Enter number of years as an integer, e.g., 5: '))

# Prompt for loan amount
loan_amount = float(input('Enter loan amount, e.g., 120000.95: '))

# Calculate payment
monthly_payment = (loan_amount * monthly_interest_rate) /\
                (1 - (1 / (1 + monthly_interest_rate)**(number_of_years * 12)))

total_payment = monthly_payment * 12 * number_of_years

# Display results
print(f'The monthly payment is {int(monthly_payment * 100) / 100}')
print(f'The total payment is {int(total_payment * 100) / 100}')
