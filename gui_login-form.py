from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("450x200+350+100")
win.title("Login")

# ============================ Function ============================

# this func is for login to the program 
def login():
    username = ent_username.get()
    password = ent_password.get()

    if username == 'ali' and password == '123ali':
        win.destroy()
        win2 = Tk()
        win2.mainloop()


# this func is for closing window
def cancle():
    result = messagebox.askquestion('Exit', 'are you sure you want to exit?')
    if result == "yes":
        win.destroy()
    
# ============================ Widget ============================

# label section
lbl_username = Label(win, text= 'User Name: ', font= 'Arial 12', padx= 20)
lbl_password = Label(win, text= 'Password: ', font= 'Arial 12')

lbl_password.grid(row= 1, column= 0)
lbl_username.grid(row= 0, column= 0)


# entry section
ent_username = Entry(win,)
ent_password = Entry(win,)

ent_password.grid(row= 1, column= 1)
ent_username.grid(row= 0, column= 1)


# button section
btn_login = Button(win, text= 'Login', width= 10, command= login)
btn_cancle = Button(win, text= 'Cancle', width= 10, command= cancle)

btn_cancle.place(x= 250, y= 130)
btn_login.place(x= 100, y= 130)


win.mainloop()
