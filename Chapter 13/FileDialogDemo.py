from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

filenameforReading = askopenfilename()
print(f"You can read from {filenameforReading}")

filenameforWriting = asksaveasfilename()
print(f"You can write data to {filenameforWriting}")