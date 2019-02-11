'''
(Find the number of years and days)
Write a program that prompts the user to enter the
minutes (e.g., 1 billion) and displays the number of years
and days for the minutes. For simplicity, assume a year has 365 days.
'''

YEARS_IN_MINUTES = 365 * 24 * 60        # Number of minutes in a year
DAYS_IN_MINUTES = 24 * 60       # Number of minutes in a day

minutes = int(input('Enter the number of minuets: '))
years = minutes // YEARS_IN_MINUTES
remaining_minutes = minutes % YEARS_IN_MINUTES
days = remaining_minutes // DAYS_IN_MINUTES

print(f'{minutes} minutes is approximately {years} years and {days} days')
