from tkinter import *
from random import randint


# Get random color string in the form of #RRGGBB
def getRandomColor():
    color = "#"
    for j in range(6):
        color += toHexChar(randint(0, 15))       # Add a randon digit
    return color


def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:
        return chr(hexValue - 10 + ord('A'))


# Define Ball class
class Ball:
    def __init__(self):
        self.x = 0      # Starting center position
        self.y = 0
        self.dx = 2     # Move right by default
        self.dy = 2     # Move down by default
        self.radius = 3     # The radius is fixed
        self.color = getRandomColor()       # Get a random color


class BounceBalls:
    def __init__(self):
        self.ballList = []      # Create a list for balls
        self.window = Tk()      # Create a window
        self.window.title("Bouncing Balls")     # Set a title

        # Handle window closed event
        self.window.protocol("WM_DELETE_WINDOW", self.quit)

        self.width = 350        # Width of the self.canvas
        self.height = 150       # Height of the self.canvas
        self.canvas = Canvas(self.window, bg="white",
                             width=self.width, height=self.height)

        self.canvas.pack()

        frame = Frame(self.window)
        frame.pack()
        # Stop
        btStop = Button(frame, text="Stop", command=self.stop)
        btStop.pack(side=LEFT)
        # Resume
        btResume = Button(frame, text="Resume", command=self.resume)
        btResume.pack(side=LEFT)
        # Add
        btAdd = Button(frame, text="+", command=self.add)
        btAdd.pack(side=LEFT)
        # Remove
        btRemove = Button(frame, text="-", command=self.remove)
        btRemove.pack(side=LEFT)

        self.sleepTime = 100        # Set a sleep time
        self.isStopped = False
        self.animate()

        self.window.mainloop()

    def stop(self):
        self.isStopped = True       # Stop animation

    def resume(self):
        self.isStopped = False      # Resume animation
        self.animate()

    def add(self):
        self.ballList.append(Ball())

    def remove(self):
        self.ballList.pop()

    def animate(self):
        while not self.isStopped:
            self.canvas.delete("ball")

            for ball in self.ballList:
                self.redisplayBall(ball)

            self.canvas.after(self.sleepTime)       # Sleep
            self.canvas.update()        # Update self.canvas

    def redisplayBall(self, ball):
        if ball.x > self.width or ball.x < 0:
            ball.dx = -ball.dx      # When ball hits left or right boundary, make it bounce off

        if ball.y > self.height or ball.y < 0:
            ball.dy = -ball.dy      # When ball hits an upper or lower boundary

        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x - ball.radius, ball.y - ball.radius,
                                ball.x + ball.radius, ball.y + ball.radius,
                                fill=ball.color, tags="ball")

    def quit(self):
        self.stop()
        self.window.destroy()


BounceBalls()
