'''
Name of the program: AlternateTwoMessages.py
Python Version (e.g. Python 3.6.0): Python 3.7.2
Your name: Tony Banh
Student id: 0740162
Date: 04/13/2019
Platform (PC, Mac, or Linux machine): Windows 10 PC

Exercise: 11.3 (Alternate two messages)

Description:
Write a program to change, with a left mouse click, between two messages
displayed on a canvas, “Programming is fun” and “It is fun to program”
'''

from tkinter import *


class AlternateTwoMessages:
    def __init__(self):
        window = Tk()       # Create window
        window.title("Rotating Message")       # Title GUI window
        self.canvas = Canvas(window, bg="white", width=200, height=100)
        self.canvas.pack()

        # Bind the Button-1 (left mouse click) event to canvas
        self.canvas.bind("<Button-1>", self.process_mouse_event)

        # Set the default message to display "Programming is fun"
        self.message = StringVar()
        self.message.set("Programming is fun")
        self.text_obj = self.canvas.create_text(100, 50, text=self.message.get())

        window.mainloop()

    def process_mouse_event(self, event):
        # Control the text alternating
        if self.message.get() == "Programming is fun":
            self.message.set("It is fun to program")        # Change the message
            self.canvas.itemconfig(self.text_obj, text=self.message.get())
        else:
            self.message.set("Programming is fun")      # Change the message
            self.canvas.itemconfig(self.text_obj, text=self.message.get())


AlternateTwoMessages()
