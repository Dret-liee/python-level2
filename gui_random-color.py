from tkinter import *
import random

win = Tk()
win.geometry('350x300+400+180')

# ============================ Function ============================
def change_color():
    lst = list('0123456789ABCDEF')
    color = '#'
    for _ in range(6):
        choice = random.choice(lst)
        color += choice

    win.configure(bg= color)
    lbl_color.config(text= color)
    print(color)

# ============================ Widget ============================
lbl_color = Label(win, width= 10)
lbl_color.place(x= 130, y= 120)

btn_change_color = Button(win, text= 'Change color', border= 5, width= 10, command= change_color)
btn_change_color.place(x= 130, y= 150)

win.mainloop()