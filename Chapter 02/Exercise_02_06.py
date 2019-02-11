'''
(Financial application: monetary units)
Rewrite Listing 2.5, ComputeChange.py, to fix the possible loss of
accuracy when converting a float value to an int value.
Enter the input as an integer whose last two digits represent the cents.
For example, the input 1156 represents 11 dollars and 56 cents.
'''


cents = int(input('Enter an amount as integer, e.g. 1156 for 11 dollars 56 cents: '))
dollars = cents // 100
remaining_cents = cents % 100
quarters = remaining_cents // 25
remaining_cents %= 25
dimes = remaining_cents // 10
remaining_cents %= 10
nickels = remaining_cents // 5
remaining_cents %= 5

print(f'''Your amount {cents} consists of
            {dollars} dollars
            {quarters} quarters
            {dimes} dimes
            {nickels} nickels
            {remaining_cents} pennies

            ''')
