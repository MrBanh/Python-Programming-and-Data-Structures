'''
(Science: day of the week)

Zeller’s congruence is an algorithm developed by Christian Zeller to calculate the day of the week. The formula is

h = (q + 26(m+1)//10 + k + k//4 +j//4 +5j) % 7

where

- h is the day of the week (0: Saturday, 1: Sunday, 2: Monday, 3: Tuesday, 4: Wednesday, 5: Thursday, 6: Friday).
- q is the day of the month.
- m is the month (3: March, 4: April, ..., 12: December). January and February are counted as months 13 and 14 of the previous year.
- j is year//100.
- k is the year of the century (i.e., year % 100).


Write a program that prompts the user to enter a year, month, and day of the month, and then it displays the name of the day of the week.
'''

year = int(input('Enter year: (e.g., 2008): '))
m_month = int(input('Enter month: 1-12: '))
q_day = int(input('Enter the day of the month: 1-31: '))

m_month %= 12

if m_month == 1 or m_month == 2:
    year -= 1
    m_month += 12

j_century = year // 100
k_year_of_century = year % 100

# 0: Saturday, 1: Sunday, 2: Monday ...
strday = {
    0: 'Saturday',
    1: 'Sunday',
    2: 'Monday',
    3: 'Tuesday',
    4: 'Wednesday',
    5: 'Thursday',
    6: 'Friday',
}

h_day_of_week = (q_day +
                 ((26 * (m_month + 1)) // 10) +
                 k_year_of_century +
                 (k_year_of_century // 4) +
                 (j_century // 4) +
                 (5 * j_century)) % 7

print('Day of the week is', strday[h_day_of_week])
