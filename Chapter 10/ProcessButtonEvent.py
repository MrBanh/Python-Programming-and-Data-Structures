from tkinter import *


def processOK():
    print("OK button is click")


def processCancel():
    print("Cancel button is clicked")


root = Tk()     # Create a root window

btnOK = Button(root, text="OK", fg="red", command=processOK)
btnCancel = Button(root, text="Cancel", bg="yellow", command=processCancel)

btnOK.pack()        # Place the button in the window
btnCancel.pack()        # Place the button in the window

root.mainloop()
