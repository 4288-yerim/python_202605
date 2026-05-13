from tkinter import *

def login() :
    print("로그인 성공!")

win = Tk()
f = Frame(win)
win.geometry("300x300")
Label(f , text="이름 : ").grid(row=0, column=0)
Entry(f).grid(row=0, column=1)

Label(f , text="비밀번호 : ").grid(row=1, column=0)
Entry(f , show="*").grid(row=1, column=1)

Button(f, text="로그인!", command=login).grid(row=2, column=1, pady=10)

f.pack(pady=20)

win.mainloop()