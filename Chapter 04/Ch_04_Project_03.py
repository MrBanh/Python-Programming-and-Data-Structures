'''
(Days of a month)

Write a program that prompts the user to enter the year and the first three
letters of a month name (with the first letter in uppercase) and displays the
number of days in the month.
'''
import sys

year = int(input("Enter a year: "))
month = input("Enter a month: ")
isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

months_with_31_days = ["Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"]
months_with_30_days = ["Apr", "Jun", "Sep", "Nov"]

if month == "Feb":
    if isLeapYear:
        days = 29
    else:
        days = 28
elif month in months_with_31_days:
    days = 31
elif month in months_with_30_days:
    days = 30
else:
    print(month, "is not a correct month name")
    sys.exit()

print(month, year, "has", days, "days")
