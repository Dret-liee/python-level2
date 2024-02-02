from tkinter import *
from tkinter import messagebox
import random

win_game = Tk()
win_game.geometry("450x250+350+100")
win_game.title("بازی رنگ")

colors = ['red', 'blue', 'yellow', 'green', 'orange', 'pink']
random_color = random.choice(colors)

time = 30
score = 0

# ============================ Function ============================
# this func start the time and game
def start_game():
    global time
    
    if time > 0:
        btn_start_game.config(state= DISABLED)
        btn_run.config(state= NORMAL)
        lbl_time.config(text= time)
        time -= 1
        lbl_time.after(1000, start_game)
        
        if time == 0:
            result = messagebox.showinfo('your time is ended', f'you earned {score} point in 30 second \nGood luck')
            if result == 'ok':
                win_game.destroy()

# this func check your entry 
def run():
    global score
    global random_color
        
    player = ent_player.get()
    ent_player.delete(0, END)

    if random_color == player:
        score += 1
        lbl_score.config(text= score)
        colors = ['red', 'blue', 'yellow', 'green', 'orange', 'pink']
        random_color = random.choice(colors)
        lbl_color.config(bg= random_color)

# ============================ Widget ============================
# label section
lbl_info_game = Label(win_game, text= 'نام رنگ مورد نظر را در کادر مربوطه وارد کنید')
lbl_info_time = Label(win_game, text= ':زمان')
lbl_info_score = Label(win_game, text= ':امتیاز')
lbl_time = Label(win_game, bg= 'yellow', text= time )
lbl_score = Label(win_game, bg= 'red', text= score)
lbl_color = Label(win_game, bg= random_color, text= 'color', font= 'Bold', width= 10,)

lbl_info_btn_start_game = Label(win_game, text= 'برای شروع بازی دکمه را فشار دهید\n شما 30 ثانیه زمان داربد\n موفق باشید')


lbl_info_game.place(x=70, y= 20)
lbl_info_time.place(x=400, y= 20)
lbl_info_score.place(x=400, y= 50)
lbl_time.place(x=370, y= 20)
lbl_score.place(x=370, y= 50)  
lbl_color.place(x= 185, y= 110)

lbl_info_btn_start_game.place(x= 20, y= 60)


# entry section
ent_player = Entry(win_game, border= 5)
ent_player.place(x= 160, y= 150)

# button section
btn_run = Button(win_game, text= 'run', bg= 'yellow', font= 'Arial 10', border= 5, command= run, state= DISABLED)
btn_start_game = Button(win_game, text= 'start', width= 10, command= start_game)

btn_run.place(x= 200, y= 200)
btn_start_game.place(x=65, y= 120)


win_game.mainloop()