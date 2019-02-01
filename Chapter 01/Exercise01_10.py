"""
(Average speed in miles)
Assume a runner runs 14 kilometers in 45 minutes and 30 seconds.
Write a program that displays the average speed in miles per hour.
(Note that 1 mile is 1.6 kilometers.)
"""

kilometers_ran = 14
miles_ran = kilometers_ran / 1.6
minutes = 45
time_in_seconds = minutes * 60 + 30
one_hour_in_seconds = 60 * 60

average_speed = miles_ran / (time_in_seconds / one_hour_in_seconds)
print(f'Average Speed: {round(average_speed, 4)} miles per hour')
