'''
(Science: wind-chill temperature)
How cold is it outside? The temperature alone is not enough to provide the
answer. Other factors including wind speed, relative humidity, and sunshine
play important roles in determining coldness outside. In 2001, the National
Weather Service (NWS) implemented the new wind-chill temperature to measure
the coldness using temperature and wind speed. The formula is given as follows:

twc = 35.74 + (0.6215 * ta) − (35.75 * (v**0.16)) + (0.4275 * ta * (v ** 0.16))

twc = wind-chill temperature
ta = outside temperature in Fahrenheight
v = speed in miles per hour

--> The formual cannot be used for wind speeds below 2 mph or for temperatures
--> below -58 F or above 41 F
'''

while True:    
    outside_temp = float(input('Enter the temperature in '
                               'Fahrenheight between -58 and 41: '))

    if -58 <= outside_temp <= 41:       # within range
        break
    else:
        print('Invalid input')

while True:
    wind_speed = float(input('Enter the wind speed in mph (must be > 2): '))

    if wind_speed >= 2:
        break
    else:
        print('Invalid input')

wind_chill = 35.74 + (0.6215 * outside_temp) - \
             (35.75 * (wind_speed ** 0.16)) + \
             (0.4275 * outside_temp * (wind_speed ** .16))

print(f'The wind chill index is {wind_chill}')
