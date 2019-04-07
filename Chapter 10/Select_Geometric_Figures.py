'''
Name of the program: Select_Geometric_Figures.py
Python Version (e.g. Python 3.6.0): Python 3.7.2
Your name: Tony Banh
Student id: 0740162
Date: 04/05/2019
Platform (PC, Mac, or Linux machine): Windows 10 PC

Exercise: 10.3 (Select geometric figures)

Description: Write a program that draws a rectangle or an oval. The user
selects a figure from a radio button and specifies whether it is filled
in a check button.

'''
from tkinter import *


class Geometric_Figures:
    def __init__(self):
        window = Tk()       # Start the window
        window.title("Radiobuttons and Checkbuttons")       # Title the window

        # Place a white canvas on the window, using Canvas()
        self.canvas = Canvas(window, width=200, height=100, bg="white")
        self.canvas.pack()

        # Create a frame in the window to hold the buttons
        frame = Frame(window)
        frame.pack(anchor=CENTER)

        # Default when loading program
        self.shape = StringVar()
        self.is_filled = BooleanVar()        # Initialize to false (unchecked)
        self.shape.set("Rectangle")       # Select Rectangle by default
        self.display_rectangle()        # Displays a rectangle by default

        # Place radiobuttons in frame
        Radiobutton(frame, text="Rectangle", variable=self.shape,
                    value="Rectangle", command=self.display_rectangle).grid(row=1, column=1)
        Radiobutton(frame, text="Oval", variable=self.shape,
                    value="Oval", command=self.display_oval).grid(row=1, column=2)

        # Place checkbutton in frame
        Checkbutton(frame, text="Filled", variable=self.is_filled,
                    command=self.fill_unfill_shape).grid(row=1, column=3)

        window.mainloop()

    # Displays the rectangle
    def display_rectangle(self):
        # Clear Oval
        self.canvas.delete("oval")

        # Create the rectangle
        self.item = self.canvas.create_rectangle(
            10, 10, 190, 90, tags="rectangle")
        self.fill_unfill_shape()        # Keeps fill state when switching between shapes

    # Displays the oval
    def display_oval(self):
        # Clears Rectangle
        self.canvas.delete("rectangle")

        # Create the oval
        self.item = self.canvas.create_oval(10, 10, 190, 90, tags="oval")
        self.fill_unfill_shape()        # Keeps fill state when switching between shapes

    # Fills or unfills the shape, based on checkbutton
    def fill_unfill_shape(self):
        if self.is_filled.get():
            self.canvas.itemconfigure(self.item, fill="red")
        else:
            self.canvas.itemconfigure(self.item, fill="")


Geometric_Figures()
