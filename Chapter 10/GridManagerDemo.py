from tkinter import *


class GridManagerDemo:
    def __init__(self):
        window = Tk()
        window.title("Grid Manager Demo")

        message = Message(
            window, text="This Message widget occupies three rows and two columns")
        message.grid(row=1, column=1, rowspan=3, columnspan=2)

        Label(window, text="First Name: ").grid(row=1, column=3)
        Entry(window).grid(row=1, column=4, padx=5, pady=5)

        Label(window, text="Last Name: ").grid(row=2, column=3)
        Entry(window).grid(row=2, column=4)

        # sticky=E stick the button to the east in the cell
        # padx and pady pad the optional horizontal and vertical space in a cell
        Button(window, text="Get Name").grid(
            row=3, padx=5, pady=5, column=4, sticky=E)

        window.mainloop()


GridManagerDemo()
