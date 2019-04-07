from tkinter import *


class PackManagerDemo:
    def __init__(self):
        window = Tk()
        window.title("Pack Manager Demo 1")

        Label(window, text="Blue", bg="blue").pack()

        # expand option tells the pack manager to assign extra space to widgeth
        Label(window, text="Red", bg="red").pack(fill=BOTH, expand=1)

        # fill uses X, Y, or BOTH to fill horizontally, vertically, or both ways
        Label(window, text="Green", bg="green").pack(fill=BOTH)

        window.mainloop()


PackManagerDemo()
