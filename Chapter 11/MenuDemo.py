from tkinter import *


class MenuDemo:
    def __init__(self):
        window = Tk()
        window.title("Menu Demo")

        # Create a menu bar
        menubar = Menu(window)
        window.config(menu=menubar)     # Display menu bar

        # Create a pulldown menu and add it to the menu bar
        operation_menu = Menu(menubar)
        menubar.add_cascade(label="Operation", menu=operation_menu)

        operation_menu.add_command(label="Add", command=self.add)
        operation_menu.add_command(label="Subtract", command=self.subtract)
        operation_menu.add_separator()
        operation_menu.add_command(label="Multiply", command=self.multiply)
        operation_menu.add_command(label="Divide", command=self.divide)

        # Create GUI options pulldown
        exitmenu = Menu(menubar)
        menubar.add_cascade(label="Exit", menu=exitmenu)
        exitmenu.add_command(label="Quit", command=window.quit)

        # Add a tool bar frame
        frame0 = Frame(window)
        frame0.grid(row=1, column=1, sticky=W)

        # Create images to represent operations
        plusImg = PhotoImage(file="plus.gif")
        minusImg = PhotoImage(file="minus.gif")
        timesImg = PhotoImage(file="times.gif")
        divideImg = PhotoImage(file="divide.gif")

        # Create buttons to represent the images
        Button(frame0, image=plusImg, command=self.add).grid(
            row=1, column=1, sticky=W)
        Button(frame0, image=minusImg, command=self.subtract).grid(
            row=1, column=2, sticky=W)
        Button(frame0, image=timesImg, command=self.multiply).grid(
            row=1, column=3, sticky=W)
        Button(frame0, image=divideImg, command=self.divide).grid(
            row=1, column=4, sticky=W)

        # Create another frame for lables and entries for user input
        frame1 = Frame(window)
        frame1.grid(row=2, column=1, pady=10)

        # Add labels and entry box to frame1
        # First number input
        Label(frame1, text="Number 1:").pack(side=LEFT)
        self.num1 = StringVar()
        Entry(frame1, width=5, textvariable=self.num1,
              justify=RIGHT).pack(side=LEFT)

        # Second number input
        Label(frame1, text="Number 2:").pack(side=LEFT)
        self.num2 = StringVar()
        Entry(frame1, width=5, textvariable=self.num2,
              justify=RIGHT).pack(side=LEFT)

        # Result
        Label(frame1, text="Result:").pack(side=LEFT)
        self.result = StringVar()
        Entry(frame1, width=5, textvariable=self.result,
              justify=RIGHT).pack(side=LEFT)

        # Create another frame for operations buttons
        frame2 = Frame(window)
        frame2.grid(row=3, column=1, pady=10, sticky=E)

        # Add buttons to frame2 for each operations: add, subtract, multiply, divide
        Button(frame2, text="Add", command=self.add).pack(side=LEFT)
        Button(frame2, text="Subtract", command=self.subtract).pack(side=LEFT)
        Button(frame2, text="Multiply", command=self.multiply).pack(side=LEFT)
        Button(frame2, text="Divide", command=self.divide).pack(side=LEFT)

        # Create event loop
        window.mainloop()

    def add(self):
        self.result.set(float(self.num1.get()) + float(self.num2.get()))

    def subtract(self):
        self.result.set(float(self.num1.get()) - float(self.num2.get()))

    def multiply(self):
        self.result.set(float(self.num1.get()) * float(self.num2.get()))

    def divide(self):
        if float(self.num2.get()) == 0:
            self.result.set("ERROR")
        else:
            self.result.set(float(self.num1.get()) / float(self.num2.get()))


MenuDemo()
