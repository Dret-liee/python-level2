from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("650x450+300+100")
win.title("test")

# ============================ Function ============================

# this func insert our data into the listbox
def insert():
    if ent_fname.get() != '' and ent_lname.get() != '':
        
        if len(ent_score.get()) == 0:
            data = f'{ent_fname.get()}-{ent_lname.get()}-{ent_score.get()}'
            lst_box.insert(END, data)
            ent_fname.delete(0, END)
            ent_lname.delete(0, END)
            ent_score.delete(0, END)
            ent_fname.focus_set()
        
        elif  len(ent_score.get()) != 0:
            score = int(ent_score.get())
            if score <= 20 and score >= 0:
                data = f'{ent_fname.get()}-{ent_lname.get()}-{score}'
                lst_box.insert(END, data)
                ent_fname.delete(0, END)
                ent_lname.delete(0, END)
                ent_score.delete(0, END)
                ent_fname.focus_set()  

            else:
                messagebox.showerror('Error', '!نمره باید بین 0 تا 20 باشد')

    else:
        messagebox.showerror('Error', '!نام و نام خانوادگی شما نمیتواند خالی باشد')


# this func clear entire listbox
def clear():
    result = messagebox.askquestion('delete listbox', 'Are you sure you want to clear entire listbox?')
    if result == 'yes':
        lst_box.delete(0, END)  


# this func delete any item you want in listbox
def delete():
    index= lst_box.curselection() 
    result = messagebox.askquestion('delete item', 'Are you sure you want to delete the item?')      
    if result == 'yes':
        lst_box.delete(index)


# this func get data from listbox and send it into the entries
def fetch():
    index = lst_box.curselection()
    data = lst_box.get(index)
    spliting = data.split('-')
    f_name = spliting[0]
    l_name = spliting[1]
    score = spliting[2]
    ent_fname.insert(0, f_name)
    ent_lname.insert(0, l_name)
    ent_score.insert(0, score)


# ============================ Widget ============================

# label section
lbl_fname = Label(win, text= 'Fname:', font= 'arial 12', padx= 20)
lbl_lname = Label(win, text= 'Lname:', font= 'arial 12', padx= 20)
lbl_score = Label(win, text= 'Score:', font= 'arial 12', padx= 20)

lbl_star_fname = Label(win, text= '*', fg= 'red', font= 'Arial 16')
lbl_star_lname = Label(win, text= '*', fg= 'red', font= 'Arial 16')


lbl_fname.place(x= 5, y= 5)
lbl_lname.place(x= 5, y= 35)
lbl_score.place(x= 5, y= 65)

lbl_star_fname.place(x= 5, y= 5)
lbl_star_lname.place(x= 5, y= 35)


# entry section
ent_fname = Entry(win, border= 5, bg= '#90B3D9')
ent_lname = Entry(win, border= 5, bg= '#90B3D9')
ent_score = Entry(win, border= 5, bg= '#90B3D9')


ent_fname.place(x= 90, y= 5)
ent_lname.place(x= 90, y= 35)
ent_score.place(x= 90, y= 65)


# create listbox
lst_box = Listbox(win, width= 60, height= 20, bg= '#9DB4B3')
lst_box.place(x= 50, y= 100)


# button section 
btn_insert = Button(win, text= 'Insert', font= 'Arial 12', width= 10, command= insert, bg= '#4FF81B' )
btn_clear = Button(win, text= 'Clear', font= 'Arial 12', width= 10, command= clear, bg= 'red')
btn_delete = Button(win, text= 'Delete', font= 'Arial 12', width= 10, command= delete, bg= 'red')
btn_fetch = Button(win, text= 'Fetch', font= 'Arial 12', width= 10, command= fetch, bg= '#50F2D3')


btn_insert.place(x= 500, y= 10)
btn_clear.place(x= 500, y= 60)
btn_delete.place(x= 500, y= 110)
btn_fetch.place(x= 500, y= 160)


win.mainloop()