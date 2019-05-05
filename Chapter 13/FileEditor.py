from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename


class FileEditor:
    def __init__(self):
        window = Tk()
        window.title("Simple Text Editor")

        # Create menu bar
        menubar = Menu(window)
        window.config(menu=menubar)     # Display menu bar

        # Create a pulldown menu, and add it to the menu bar
        operation_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=operation_menu)
        operation_menu.add_command(label="Open", command=self.open_file)
        operation_menu.add_command(label="Save", command=self.save_file)

        # Hold editor pane
        frame = Frame(window)
        frame.grid(row=1, column=1)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.text = Text(frame, width=40, height=20, wrap=WORD,
                            yscrollcommand=scrollbar.set)
        self.text.pack()
        scrollbar.config(command=self.text.yview)

        window.mainloop()

    def open_file(self):
        filenamefor_Reading = askopenfilename()
        input_file = open(filenamefor_Reading, 'r')
        self.text.insert(END, input_file.read())        # Read all from the file
        input_file.close()

    def save_file(self):
        filenamefor_Writing = asksaveasfilename()
        output_file = open(filenamefor_Writing, 'w')
        # Write the file
        output_file.write(self.text.get(1.0, END))
        output_file.close()


FileEditor()
