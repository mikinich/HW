from tkinter import *
import time
window = Tk()
window.geometry('500x400')
window.resizable(width=False, height=False)
canvas = Canvas(window, width=500, height=400)
canvas.pack()
class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.oval = canvas.create_oval(200, 200, 230, 230, fill=color)
        self.line = canvas.create_line(200,200,230,230, fill=color)
        self.x = 1
        self.y = 1


    def draw(self):
        self.canvas.move(self.oval, self.x, self.y)
        coords = self.canvas.coords(self.oval)
        x1,y1,x2,y2 = coords

        if x1 <=0 or x2>=500:
            self.x = -self.x

        if y1 <= 0 or y2 >= 400:
            self.y = -self.y
        while True:
            self.line = canvas.create_line(x1, y1, x2, y2, fill='blue')
ball = Ball(canvas, 'red')







while True:
    ball.draw()
    window.update()
    time.sleep(0.01)