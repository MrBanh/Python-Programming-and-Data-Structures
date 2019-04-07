from tkinter import *


class TextReverser:
    def __init__(self):
        # Create window
        window = Tk()
        window.title("Reverse")

        # Create widgens for the window
        self.visible_message = StringVar()      # Holds a string, default is ""
        self.visible_message.set("Hello... how are you?!?")
        text_label = Label(window,
                           textvariable=self.visible_message,
                           font=("Arial", 32))

        self.reverseState = IntVar()        # Holds an integer, default is 0
        reverse_button = Checkbutton(window,
                                     text="Reverse text",
                                     font=("Arial", 24),
                                     variable= self.reverseState,
                                     command=self.update_text)

        # Adds the controls to window
        text_label.pack()
        reverse_button.pack()

        # Create an "event loop"
        window.mainloop()

    def update_text(self):
        if(self.reverseState.get() == 1):
            self.visible_message.set("?!?uoy era woh ...olleH")
        else:
            self.visible_message.set("Hello... how are you?!?")

TextReverser()
