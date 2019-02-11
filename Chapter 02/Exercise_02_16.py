'''
(Physics: acceleration)
Average acceleration is defined as the change of velocity
divided by the time taken to make the change

average_acceleration = (v1 - v0) / t

v1 = ending velocity in meters/second
v0 = starting velocity in meters/second
t = time in seconds
'''

initial_velocity = float(input('Enter initial velocity: '))
ending_velocity = float(input('Enter ending velocity: '))
time = float(input('Enter time: '))

average_acceleration = (ending_velocity - initial_velocity) / time

print(f'The average acceleration is {average_acceleration}')
