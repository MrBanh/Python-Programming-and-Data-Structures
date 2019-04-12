from tkinter import *


class ComboBoxDemo:
    def __init__(self):
        window = Tk()       # Create a window
        window.title("Combo Box Demo")      # Set title

        # Create PhotoImage objects
        self.usImage = PhotoImage(file="us.gif")
        self.caImage = PhotoImage(file="ca.gif")

        # Create the combo box to select a country
        self.country = StringVar()
        self.country.set("Canada")
        self.cb_country = OptionMenu(window, self.country, "Canada",
                                     "US", command=self.process_selection)
        self.cb_country.pack(fill=BOTH)

        # Create a canvas to display image
        self.canvas = Canvas(window)
        self.canvas.create_image(100, 50, image=self.caImage, tag="image")
        self.canvas.pack()

        # Create event loop
        window.mainloop()

    def process_selection(self, selected_item):
        self.canvas.delete("image")     # Resets the canvas
        if selected_item == "Canada":
            self.canvas.create_image(100, 50, image=self.caImage, tag="image")
        elif selected_item == "US":
            self.canvas.create_image(100, 50, image=self.usImage, tag="image")

ComboBoxDemo()
