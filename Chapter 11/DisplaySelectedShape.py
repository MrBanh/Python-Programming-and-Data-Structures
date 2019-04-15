'''
Name of the program: DisplaySelectedShape.py
Python Version (e.g. Python 3.6.0): Python 3.7.2
Your name: Tony Banh
Student id: 0740162
Date: 04/13/2019
Platform (PC, Mac, or Linux machine): Windows 10 PC

Exercise: 11.1 (Display a selected shape)

Description:
Write a program that contains a combo box and a canvas. The combo box shows
five strings: rectangle, oval, arc, polygon, and line. The canvas displays
a shape according to the selection in the combo box
'''

from tkinter import *


class DisplaySelectedShape:
    def __init__(self):
        window = Tk()       # Create window
        window.title("Select Shapes")       # Title GUI window

        # Crate a combo box to select a shape
        self.shape = StringVar()
        self.shape.set("rectangle")     # Default shape is rectangle
        self.combo_box = OptionMenu(window, self.shape,
                                    "rectangle", "oval", "arc",
                                    command=self.process_shape)
        self.combo_box.pack(fill=BOTH)      # Display the combo box

        # Create a canvas to display shape, display rectangle by default
        self.canvas = Canvas(window, width=200, height=100)
        self.canvas.pack()
        self.process_shape(self.shape.get())

        window.mainloop()

    def process_shape(self, selected_shape):
        # Erase current shape
        self.canvas.delete("shape")

        # Determine which shape to display
        if selected_shape == "rectangle":
            self.canvas.create_rectangle(10, 10, 190, 90, tags="shape")
        elif selected_shape == "oval":
            self.canvas.create_oval(10, 10, 190, 90, fill="red", tags="shape")
        elif selected_shape == "arc":
            self.canvas.create_arc(10, 10, 190, 90, start=0, extent=90,
                                   fill="red", width=8, tags="shape")


DisplaySelectedShape()
