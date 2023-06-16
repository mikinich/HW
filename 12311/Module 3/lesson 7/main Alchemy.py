import random
from tkinter import *
import random as rn


window = Tk()
window.geometry('600x600')
window.title('Алхимия')


class Steam:
    image = PhotoImage(file=r'C:\Users\user\PycharmProjects\pythonProject1\12311\Module 3\lesson 7\Доп. материалы\aroma.png').subsample(4,4)

class Water:
    image = PhotoImage(file=r'C:\Users\user\PycharmProjects\pythonProject1\12311\Module 3\lesson 7\Доп. материалы\water.png').subsample(4,4)
    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam

class Fire:
    image = PhotoImage(file=r'C:\Users\user\PycharmProjects\pythonProject1\12311\Module 3\lesson 7\Доп. материалы\fire.png').subsample(4,4)
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam
        if isinstance(other, Ground):
            return Pottery

class Wind:
    image = PhotoImage(file=r'C:\Users\user\PycharmProjects\pythonProject1\12311\Module 3\lesson 7\Доп. материалы\wind.png').subsample(4,4)
    def __add__(self, other):
        if isinstance(other, Pottery):
            return Dust
class Pottery:
    image = PhotoImage(file=r'C:\Users\user\PycharmProjects\pythonProject1\12311\Module 3\lesson 7\Доп. материалы\pottery.png').subsample(4,4)
    def __add__(self, other):
        if isinstance(other, Wind):
            return Dust
class Ground:
    image = PhotoImage(file=r'C:\Users\user\PycharmProjects\pythonProject1\12311\Module 3\lesson 7\Доп. материалы\ground.png').subsample(4,4)
    def __add__(self, other):
        if isinstance(other, Fire):
            return Pottery
class Dust:
    image = PhotoImage(file=r'C:\Users\user\PycharmProjects\pythonProject1\12311\Module 3\lesson 7\Доп. материалы\dust.png').subsample(4,4)

canvas = Canvas(width=600, height=600)
canvas.pack()

def move(event):
    images_ids = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    canvas.coords(images_ids, event.x, event.y)
    if len(images_ids) == 2:
        elem_id_1, elem_id_2 = images_ids[0], images_ids[1]
        elem1 = elems[elem_id_1 -1]
        elem2 = elems[elem_id_2 -1]

        new_elem = elem1 + elem2
        if new_elem not in elems:
            elems.append(new_elem)
            canvas.create_image(event.x, event.y, image=new_elem.image)
    print(images_ids)

elems = [Wind(), Fire(), Water(), Ground()]
for elem in elems:
    canvas.create_image(rn.randint(50, 550), rn.randint(50, 550), image=elem.image)
window.bind('<B1-Motion>', move)


window.mainloop()