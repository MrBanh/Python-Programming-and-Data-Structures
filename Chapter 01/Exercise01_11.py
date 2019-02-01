"""
(Population projection)
The US Census Bureau projects population based on the following assumptions:

One birth every 7 seconds

One death every 13 seconds

One new immigrant every 45 seconds

Write a program to display the population for each of the next five years. 
Assume that the current population is 312032486 and one year has 365 days.
"""

current_population = 312032486
year_in_seconds = 365 * 24 * 60 * 60
num_of_years = 5

for i in range(num_of_years):
    birth_rate = int(year_in_seconds / 7)
    death_rate = int(year_in_seconds / 13)
    immigrant_rate = int(year_in_seconds / 45)
    current_population += (birth_rate - death_rate + immigrant_rate)
    print(f'Year {i + 1} Population:', current_population)
