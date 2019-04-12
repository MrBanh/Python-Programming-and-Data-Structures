from tkinter import *


class AnimationDemo:
    def __init__(self):
        window = Tk()
        window.title("Animation Demo")

        self.width = 250     # width of the canvas
        self.canvas = Canvas(window, bg="white", width=self.width, height=50)
        self.canvas.pack()

        # Frame for adding buttons to control animation
        frame = Frame(window)
        frame.pack()
        # Stop button
        btStop = Button(frame, text="Stop", command=self.stop)
        btStop.pack(side=LEFT)
        # Resume button
        btResume = Button(frame, text="Resume", command=self.resume)
        btResume.pack(side=LEFT)
        # Faster button
        btFaster = Button(frame, text="Faster", command=self.faster)
        btFaster.pack(side=LEFT)
        # Slower button
        btSlower = Button(frame, text="Slower", command=self.slower)
        btSlower.pack(side=LEFT)

        self.x = 0       # Starting x position
        self.sleepTime = 100        # Set a sleep time
        self.canvas.create_text(self.x, 30, text="Message moving?", tags="text")

        self.dx = 3
        self.isStopped = False
        self.animate()

        window.mainloop()

    def stop(self):
        # Stop the animation
        self.isStopped = True

    def resume(self):
        # Resume animation
        self.isStopped = False
        self.animate()

    def faster(self):
        # Speed up animation
        if self.sleepTime > 5:
            self.sleepTime -= 20

    def slower(self):
        # slow down animation
        self.sleepTime += 20

    def animate(self):
        # Move the message
        while not self.isStopped:
            self.canvas.move("text", self.dx, 0)      # Move text dx unit on x-axis
            self.canvas.after(self.sleepTime)       # Sleep
            self.canvas.update()     # Update the canvas
            if self.x < self.width:
                self.x += self.dx     # Current position for string
            else:
                self.x = 0       # Reset the string position to the beginning
                self.canvas.delete("text")
                # Redraw the text at the beginning
                self.canvas.create_text(self.x, 30, text="Message moving?", tags="text")


AnimationDemo()
