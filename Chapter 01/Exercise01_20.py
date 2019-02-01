"""
(Turtle: display a rectanguloid)
Write a program that displays a rectanguloid
"""
from turtle import penup, pendown, goto, forward, right, left, position, done
import math

def draw_rectangle(x: float, y: float, \
               short_side: float, long_side: float, \
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
    short_side = 100
    long_side = 200
    top_bot_angle = 45
    front_back_angle = 90

    # Draw the top and bottom
    top_x = - (long_side / 2)
    top_y = short_side / 2
    bot_x = - (long_side / 2)
    bot_y = - short_side / 2
    draw_rectangle(top_x, top_y, short_side, long_side, top_bot_angle)
    draw_rectangle(bot_x, bot_y, short_side, long_side, top_bot_angle)

    # Draw the front and back
    draw_rectangle(bot_x, bot_y, short_side, long_side, front_back_angle)
    # TODO: FIX
    right(top_bot_angle)
    forward(short_side)
    back_x = position()[0]
    back_y = position()[1]
    draw_rectangle(back_x, back_y, short_side, long_side, front_back_angle)

    done()
