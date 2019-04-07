from tkinter import *


class PackManagerDemo2:
    def __init__(self):
        window = Tk()
        window.title("Pack Manager Demo 2")

        Label(window, text="Blue", bg="blue").pack(side=LEFT)

        # expand option tells the pack manager to assign extra space to widgeth
        Label(window, text="Red", bg="red").pack(side=LEFT, fill=BOTH, expand=1)

        # fill uses X, Y, or BOTH to fill horizontally, vertically, or both ways
        Label(window, text="Green", bg="green").pack(side=LEFT, fill=BOTH)

        window.mainloop()


PackManagerDemo2()