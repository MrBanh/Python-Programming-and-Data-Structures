'''
The place manager is not compatible with all computers.
If you run this program on Windows with a screen resolution of 1024 × 768,
the layout size is just right. When the program is run on Windows with a
monitor with a higher resolution, the components appear very small and
clump together. When it is run on Windows with a monitor with a lower
resolution, they cannot be shown in their entirety. Because of these
incompatibility issues, you should generally avoid using the place manager.
'''


from tkinter import *


class PlaceManagerDemo:
    def __init__(self):
        window = Tk()
        window.title("Place Manager Demo")

        Label(window, text="Blue", bg="blue").place(x=20, y=20)
        Label(window, text="Red", bg="red").place(x=50, y=50)
        Label(window, text="Green", bg="green").place(x=80, y=80)

        window.mainloop()


PlaceManagerDemo()
