from course import get_course, today
from tkinter import *


window = Tk()
window.geometry('500x500')
window.title('Банк Святого Павла')
window.resizable(False,False)
window.configure(background='gray')
image = PhotoImage(file='logo.png')
label_img =  Label(window, image=image)
label_img.place(x=0, y=0)
label_title = Label(window, text='sBeer Bank', font="Arial 32")
label_title.place(x=200, y=50)
label_curency = Label(window, text=f'курсы на {today}:', font='Arial 22', fg='green', bg='gray' )
label_curency.place(x=5, y=200)
dollar_info = f"{get_course('R01235').get('name')} {get_course('R01235').get('value')} ₽"
dollar_Label = Label(window, text=dollar_info, font='arial 20', fg='red' , bg='gray')
dollar_Label.place(x=5, y=250)
euro_info = f"{get_course('R01239').get('name')} {get_course('R01239').get('value')} ₽"
euro_label = Label(window, text=euro_info, font='arial 20', fg='red' , bg='gray')
euro_label.place(x=5, y=300)
uan_info = f"{get_course('R01375').get('name')} {get_course('R01375').get('value')} ₽"
uan_label = Label(window, text=uan_info, font='arial 20', fg='red' , bg='gray')
uan_label.place(x=5, y=350)
entry = Entry(font='arial 22')
entry.place(x=5,y=400)
y = 40
def Search():
    global y
    currency_ID = entry.get()
    currency_info = get_course(currency_ID)
    currency_name = currency_info.get('name')
    currency_value = currency_info.get('value')
    currency_str = f"{currency_name} {currency_value}"
    currency_Label = Label(window, text=currency_str, font='arial 20', fg='red', bg='gray')
    currency_Label.place(x=5, y=450 + y)
    y += 40



button = Button(text='Найти', command=Search)
button.place(x=350, y=400)






window.mainloop()