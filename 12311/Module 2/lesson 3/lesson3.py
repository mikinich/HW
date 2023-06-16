from tkinter import *
import random


window = Tk()
window.geometry('600x600')
canvas = Canvas(window, width=600, height=600)
canvas.pack()


background = PhotoImage(file=r'C:\Users\user\PycharmProjects\pythonProject1\12311\lesson 3\доп материалы\Доп. материалы\Доп. материалы\bg_2.png')


class Knight:
    def __init__(self):
        self.x = 150
        self.y = 350
        self.v = 0
        self.vx = 0
        self.photo = PhotoImage(file=r'C:\Users\user\PycharmProjects\pythonProject1\12311\lesson 3\доп материалы\Доп. материалы\Доп. материалы\knight.png')

    def up(self, event):
        self.v = -6

    def down(self, event):
        self.v = 6

    def stop(self, event):
        self.v = 0
        self.vx = 0
    def left(self, event):
        self.vx = -4
    def right(self, event):
        self.vx = 4

knight = Knight()

class Dragon():
    def __init__(self):
        self.x = random.randint(550, 600)
        self.y = random.randint(50,550)
        self.v = random.randint(1,4)
        self.photo = PhotoImage(file=r'C:\Users\user\PycharmProjects\pythonProject1\12311\lesson 3\доп материалы\Доп. материалы\Доп. материалы\dragon.png')
dragon = Dragon()

dragons =[]
for i in range(5):
    dragons.append(Dragon())



def game():
    canvas.delete('all')
    canvas.create_image(300, 300, image=background)
    canvas.create_image(knight.x, knight.y,  image=knight.photo)
    knight.y += knight.v
    knight.x += knight.vx
    for dragon in dragons:
        canvas.create_image(dragon.x, dragon.y, image=dragon.photo)
        dragon.x -= dragon.v
        if ((knight.x - dragon.x) ** 2 + (knight.y - dragon.y) ** 2) ** 0.5 <50:
            dragons.remove(dragon)
    print(knight.y)
    if len(dragons) == 0:
        return win()
    if dragon.x < 50:
        return lose()
    if knight.x >550:
        knight.x =500
    elif knight.x < 50:
        knight.x = 100
    elif knight.y < 50:
        knight.y = 100
    elif knight.y > 550:
        knight.y = 500
    window.after(5, game)

def win():
    canvas.create_text(300, 300, text='Вы Выиграли', font='Verdana 42')

def lose():
    canvas.create_text(300, 300, text='Вы Проиграли', font='Verdana 42')


window.bind('<Key-Right>',knight.right)
window.bind('<Key-Left>',knight.left)
window.bind('<Key-Up>',knight.up)
window.bind('<Key-Down>',knight.down)
window.bind('<KeyRelease>',knight.stop)






game()
window.mainloop()