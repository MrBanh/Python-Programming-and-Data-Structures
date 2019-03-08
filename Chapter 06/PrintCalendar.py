'''
PrintCalendar.py - prints the calendar based on year and month given by user

    Inputs:
        year: int -- User input the full year (e.g. 2001)
        day: int -- User input the month as a number between 1 and 12

    Outputs Example:
        December 2014
-----------------------------
 Sun Mon Tue Wed Thu Fri Sat
       1   2   3   4   5   6
   7   8   9  10  11  12  13
  14  15  16  17  18  19  20
  21  22  23  24  25  26  27
  28  29  30  31
'''
import datetime


# Print the calendar for the month in a year
def print_month(year: int, month: int) -> None:
    # Print the headings of the calendar
    print_month_title(year, month)

    # Print the body of the calendar
    print_month_body(year, month)


# Print the month title, e.g., December 2019
def print_month_title(year: int, month: int) -> None:
    month_title = get_month_name(month) + ' ' + str(year)
    print(f"{month_title:^29}")
    print("-----------------------------")
    print(" Sun Mon Tue Wed Thu Fri Sat")


# Get the month as a string
def get_month_name(month: int) -> str:
    return datetime.date(1900, month, 1).strftime('%B')


# Print month body
def print_month_body(year: int, month: int) -> None:
    # Get the start day of the week for the first date in the month
    start_day = get_start_day(year, month)

    # Get number of days in the month
    num_of_days_in_month = get_num_of_days_in_month(year, month)

    # Paid the space before first day of the month, depending on start day
    for i in range(start_day):
        print("    ", end="")

    # Print all the days of the calendar
    for i in range(1, num_of_days_in_month + 1):
        print(f"{i:>4}", end='')

        # Jump to the new line
        if (i + start_day) % 7 == 0:
            print()


# Get the start day of month/1/year
def get_start_day(year: int, month: int) -> int:
    # weekday() returns 0 for Monday and 6 for Sunday
    # Add 1 so 1 is Monday and 7 is Sunday
    start_day = datetime.datetime(year, month, 1).weekday() + 1

    # If 7 is assigned to start_day, return 0 so 0 is Sunday
    return 0 if start_day == 7 else start_day


def get_num_of_days_in_month(year: int, month: int) -> int:
    # January, March, May, July, August, October, and December have 31 days.
    months_31_days = [1, 3, 5, 7, 8, 10, 12]
    # April, June, September, and November have 30 days
    months_30_days = [4, 6, 9, 11]

    if month == 2:
        return 29 if is_Leap_Year(year) else 28
    elif month in months_31_days:
        return 31
    elif month in months_30_days:
        return 30
    else:
        return 0        # If month is incorrect


def is_Leap_Year(year: int) -> bool:
    # Determines if year is a leap year
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def main():
    # Prompt user for input
    year = int(input("Enter full year (e.g., 2001): "))
    month = int(input("Enter month as a number between 1 and 12: "))
    print_month(year, month)


if __name__ == "__main__":
    main()
