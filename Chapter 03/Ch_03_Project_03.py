'''
(Find the number of days in a month)

Write a program that prompts the user to enter the month and year and displays the number of days in the month.
For example, if the user entered month 2 and year 2000, the program should display that February 2000 has 29 days.
If the user entered month 3 and year 2005, the program should display that March 2005 has 31 days.
'''
import datetime

month = int(input('Enter a month in the year (e.g. 1 for Jan): '))
year = int(input('Enter a year: '))

isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if month == 1:
    days = 31
    print('January', year, 'has', days, 'days')
elif month == 2:
    days = 28
    if isLeapYear:
        days = 29
    print('February', year, 'has', days, 'days')
elif month == 3:
    days = 31
    print('March', year, 'has', days, 'days')
elif month == 4:
    days = 30
    print('April', year, 'has', days, 'days')
elif month == 5:
    days = 31
    print('May', year, 'has', days, 'days')
elif month == 6:
    days = 30
    print('June', year, 'has', days, 'days')
elif month == 7:
    days = 31
    print('July', year, 'has', days, 'days')
elif month == 8:
    days = 31
    print('August', year, 'has', days, 'days')
elif month == 9:
    days = 30
    print('September', year, 'has', days, 'days')
elif month == 10:
    days = 31
    print('October', year, 'has', days, 'days')
elif month == 11:
    days = 30
    print('November', year, 'has', days, 'days')
elif month == 12:
    days = 31
    print('December', year, 'has', days, 'days')
else:
    print('Invalid month number.')


# Cleaner solution using datetime module
date = datetime.datetime(year, month, 1)
num_of_days = (datetime.datetime(year, month + 1, 1) - date).days

print(date.strftime('%B'), year, 'has', num_of_days, 'days')
