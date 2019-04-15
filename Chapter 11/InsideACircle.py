'''
Name of the program: InsideACircle.py
Python Version (e.g. Python 3.6.0): Python 3.7.2
Your name: Tony Banh
Student id: 0740162
Date: 04/13/2019
Platform (PC, Mac, or Linux machine): Windows 10 PC

Exercise: 11.10 (Geometry: inside a circle?)

Description:
Write a program that draws a fixed circle centered at (100, 60) with radius 50.
Whenever the mouse is moved while the left button is pressed, display the
message indicating whether the mouse pointer is inside the circle.
'''

from tkinter import *


class InsideACircle:
    def __init__(self):
        window = Tk()       # Create window
        window.title("Inside the circle?")       # Title GUI window

        # Create the circle, centered as 100, 60 and with radius of 50
        self.center_x = 100
        self.center_y = 60
        self.radius = 50
        self.canvas = Canvas(window, width=250, height=120, bg="white")
        self.canvas.pack()
        self.canvas.create_oval(self.center_x - self.radius,
                                self.center_y - self.radius,
                                self.center_x + self.radius,
                                self.center_y + self.radius)

        # Bind <B1-Motion> (left click hold and drag) to canvas
        self.canvas.bind("<B1-Motion>", self.process_mouse_event)

        window.mainloop()

    def process_mouse_event(self, event):
        # If mouse is within circle
        if (self.center_x - self.radius) <= event.x <= (self.center_x + self.radius)\
        and (self.center_y - self.radius) <= event.y <= (self.center_y + self.radius):
            self.canvas.delete("text")
            self.canvas.create_text(event.x, event.y - 10, tags="text",
                                    text="Mouse pointer is in the circle")
        else:
            self.canvas.delete("text")
            self.canvas.create_text(event.x, event.y - 10, tags="text",
                                    text="Mouse pointer is not in the circle")


InsideACircle()
