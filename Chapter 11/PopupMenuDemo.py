from tkinter import *


class PopupMenuDemo:
    def __init__(self):
        window = Tk()
        window.title("Popup Menu Demo")

        # Create a pop up menu
        self.menu = Menu(window, tearoff=0)
        self.menu.add_command(label="Draw a line", command=self.display_line)
        self.menu.add_command(label="Draw an oval", command=self.display_oval)
        self.menu.add_command(label="Draw a rectangle",
                              command=self.display_rect)
        self.menu.add_command(label="Clear", command=self.clear)

        # Place canvas in window
        self.canvas = Canvas(window, width=200, height=100, bg="white")
        self.canvas.pack()

        # Bind popup to canvas
        self.canvas.bind("<Button-3>", self.popup)

        window.mainloop()

    def display_line(self):
        self.canvas.create_line(10, 10, 190, 90, tags="line")
        self.canvas.create_line(10, 90, 190, 10, tags="line")

    def display_oval(self):
        self.canvas.create_oval(10, 10, 190, 90, tags="oval")

    def display_rect(self):
        self.canvas.create_rectangle(10, 10, 190, 90, tags="rect")

    def clear(self):
        self.canvas.delete("line", "oval", "rect")

    def popup(self, event):
        self.menu.post(event.x_root, event.y_root)

PopupMenuDemo()
