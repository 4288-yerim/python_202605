from tkinter import *
import random

answer = random.randint(1, 100)
count = 0

def guess() :
    global count
    num = int(guess_num.get())
    count += 1
    if num > answer :
        msg = "높음"
    elif num < answer :
        msg = "낮음"
    else :
        msg = f"정답, {count}번만에 맞췄습니다"
        
    mmsg["text"] = msg
    guess_num.delete(0,END)
    
def reset():
    global answer
    global count
    answer = random.randint(1, 100)
    mmsg["text"] = "1부터 100사이의 숫자를 입력하시오."
    guess_num.delete(0, END)
    count = 0
    

win = Tk()
win.geometry("500x300")

Label(win , text="숫자 게임에 오신 것을 환영합니다!").grid(row=0, column=0)

guess_num = Entry(win)
guess_num.grid(row=1, column=0)
try_button = Button(win, text="시도", foreground="green", command=guess).grid(row=1, column=1)
Button(win, text="초기화", foreground="red", command=reset).grid(row=1, column=2)
mmsg = Label(win , text="1부터 100사이의 숫자를 입력하시오.")
mmsg.grid(row=1, column=3)

win.mainloop()