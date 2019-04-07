from tkinter import *


class CanvasDemo:
    def __init__(self):
        window = Tk()
        window.title("Canvas Demo")

        # Place self.canvas in window
        self.canvas = Canvas(window, width=200, height=100, bg="white")
        self.canvas.pack()

        # Place buttons in the frame
        frame = Frame(window)
        frame.pack()

        # Insert buttons for shapes in the frame
        btnRectangle = Button(frame, text="Rectangle",
                              command=self.displayRectangle)
        btnOval = Button(frame, text="Oval", command=self.displayOval)
        btnArc = Button(frame, text="Arc", command=self.displayArc)
        btnPolygon = Button(frame, text="Polygon", command=self.displayPolygon)
        btnLine = Button(frame, text="Line", command=self.displayLine)
        btnString = Button(frame, text="String", command=self.displayString)
        btnClear = Button(frame, text="Clear", command=self.clearCanvas)

        # Format placement of buttons
        btnRectangle.grid(row=1, column=1)
        btnOval.grid(row=1, column=2)
        btnArc.grid(row=1, column=3)
        btnPolygon.grid(row=1, column=4)
        btnLine.grid(row=1, column=5)
        btnString.grid(row=1, column=6)
        btnClear.grid(row=1, column=7)

        # Event loop
        window.mainloop()

    # Display a rectangle
    def displayRectangle(self):
        self.canvas.create_rectangle(10, 10, 190, 90, tags="rectangle")

    # Display oval
    def displayOval(self):
        self.canvas.create_oval(10, 10, 190, 90, fill="red", tags="oval")

    # Display Arc
    def displayArc(self):
        self.canvas.create_arc(10, 10, 190, 90, start=0,
                               extent=90, width=8, fill="red", tags="arc")

    # Display polygon
    def displayPolygon(self):
        self.canvas.create_polygon(10, 10, 190, 90, 30, 50, tags="polygon")

    # Display line
    def displayLine(self):
        self.canvas.create_line(10, 10, 190, 90, fill="red", tags="line")
        self.canvas.create_line(10, 90, 190, 10, width=9,
                                arrow="last", activefill="blue", tags="line")

    # Display a string
    def displayString(self):
        self.canvas.create_text(60, 40, text="Hi, I am a string",
                                font="Times 10 bold underline", tags="string")

    # Clear drawings
    def clearCanvas(self):
        self.canvas.delete("rectangle", "oval", "arc",
                           "polygon", "line", "string")


CanvasDemo()
