'''
(Turtle: display a clock)
Write a program that displays a clock to show the time 9:15:00
'''
from turtle import penup, pendown, goto, forward, left, right, circle, color, write, done

# Draw circle
penup()
goto(0, -200)
pendown()
circle(200)

# Show 3, 6, 9, 12 and 9:15:00
penup()
goto(0, -225)
write('9:15:00', align='center', font=('Arial', 16, 'normal'))
goto(0, -195)
write('6', align='center', font=('Arial', 16, 'normal'))
goto(180, 0)
write('3', align='center', font=('Arial', 16, 'normal'))
goto(0, 175)
write('12', align='center', font=('Arial', 16, 'normal'))
goto(-180, 0)
write('9', align='center', font=('Arial', 16, 'normal'))

# Show the clockhands
goto(-100, 0)
pendown()
color('green')
forward(100)
left(90)
color('red')
forward(100)
penup()
goto(0, 0)
right(90)
pendown()
color('blue')
forward(100)

done()
