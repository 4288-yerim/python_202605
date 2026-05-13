from tkinter import *
from tkinter import messagebox
import random

ran_num = random.randint(1,100)
count = 0

def try_game() :
    global count
    try_num = int(num.get())
    count += 1
    if try_num > ran_num :
        messagebox.showinfo("실패", "DOWN!")
    elif try_num < ran_num :
        messagebox.showinfo("실패","UP!")
    else :
        num.delete(0, END)
        messagebox.showinfo("성공", f"정답! {count}만에 맞추셨습니다.")
        init_game()

def init_game() :
    messagebox.showinfo("알림","게임을 다시 시작합니다!")
    global ran_num
    global count
    ran_num = random.randint(1,100)
    count = 0
    num.delete(0, END)
    
win = Tk()
win.geometry("300x300")
f = Frame(win)

Label(win, text="숫자 게임!").pack(pady=30)
num = Entry(f)
num.pack(side="left")
Button(f, text="시도", command=try_game).pack(side="left")
Button(f, text="초기화", command=init_game).pack(side="left")
f.pack(pady=20)
 
win.mainloop()