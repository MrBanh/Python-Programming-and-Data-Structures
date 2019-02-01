"""
(Turtle: display a rectanguloid)
Write a program that displays a rectanguloid
"""
from turtle import penup, pendown, goto, forward, right, left, position, done
import math


def draw_rectangle(x: float, y: float,
                   short_side: float, long_side: float,
                   inner_angle: float) \
                   -> None:

    outer_angle = 180 - inner_angle
    penup()
    goto(x, y)
    pendown()
    forward(long_side)
    left(inner_angle)
    forward(short_side)
    left(outer_angle)
    forward(long_side)
    left(inner_angle)
    forward(short_side)
    left(outer_angle)


if __name__ == "__main__":
    try:
        short_side = 100
        long_side = 200
        acute_angle = 30      # Change the inner angle here, should be <90
        right_angle = 90

        if acute_angle >= 90:
            raise Exception

        # Draw the top and bottom
        top_x = - (long_side / 2)
        top_y = short_side / 2
        bot_x = - (long_side / 2)
        bot_y = - short_side / 2
        draw_rectangle(top_x, top_y, short_side, long_side, acute_angle)
        draw_rectangle(bot_x, bot_y, short_side, long_side, acute_angle)

        # Draw the front and back
        draw_rectangle(bot_x, bot_y, short_side, long_side, right_angle)
        left(acute_angle)
        forward(short_side)
        right(acute_angle)
        back_x = position()[0]
        back_y = position()[1]
        draw_rectangle(back_x, back_y, short_side, long_side, right_angle)

        done()
    except:
        print('Angle needs to be acute (< 90 degrees).')
        exit()
