from tkinter import *
from tkinter import messagebox


win = Tk()
win.geometry("400x200+350+100")
win.title("time")

time = 0

# ============================ Function ============================

# this func set time 
def set_time():
    global time
    time = int(ent_time.get())

    return time

# this func reset time 
def reset():
    global time 
    time = 0
    lbl_time.config(text= '')   
    btn_start.config(state= NORMAL)
    btn_settime.config(state= NORMAL)
    btn_reset.config(state= DISABLED)
    ent_time.delete(0, END)

# this func start countdown the time 
def start():
    global time 
    if time > 0:
        btn_reset.config(state= NORMAL)
        btn_start.config(state= DISABLED)
        btn_settime.config(state= DISABLED)
        lbl_time.config(text= time)
        time -= 1
        lbl_time.after(1000, start)

        if time == 0:
            messagebox.showinfo('time', 'time is ended')
            btn_reset.config(state= DISABLED)
            btn_start.config(state= NORMAL)
            btn_settime.config(state= NORMAL)
    
# ============================ Widget ============================

# label section
lbl_info = Label(win, text= 'please enter your time in second -->', font= 'Arial 10')
lbl_time = Label(win, fg= 'black', bg= 'yellow', font= '14')

lbl_info.place(x= 15, y= 75)
lbl_time.place(x= 190, y=25)

# entry section 
ent_time = Entry(win, border= 5)
ent_time.place(x= 250, y= 75)

# button section
btn_settime = Button(win, text= 'set time', width= 10, command= set_time)
btn_start = Button(win, text= 'start', width= 10, command= start )
btn_reset = Button(win, text= 'reset', width= 10, state= DISABLED, command= reset)

btn_settime.place(x= 50, y= 160)
btn_start.place(x= 150, y= 160)
btn_reset.place(x= 250, y= 160)


win.mainloop()
