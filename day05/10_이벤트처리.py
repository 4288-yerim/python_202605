from tkinter import *
from tkinter import messagebox

# 아이디 test 비밀번호 1234 입력하면 '로그인 성공'
# 아니면 '로그인 실패' 출력
def login() :
    if id.get() == "test" and pwd.get() == "1234" :
        messagebox.showinfo("알림", "로그인 성공!")
    else :
        id.delete(0, END)
        pwd.delete(0, END)
        messagebox.showwarning("경고", "로그인 실패!")

win = Tk()
f = Frame(win)
win.geometry("300x300")

Label(f, text="아이디 : ").grid(row=0, column=0)
id = Entry(f)
id.grid(row=0, column=1)
Label(f, text="비밀번호 : ").grid(row=1, column=0)
pwd = Entry(f, show="*")
pwd.grid(row=1, column=1) 
Button(f, text="로그인!", command=login).grid(
    row=2, column=0, columnspan=2, pady=10
)
f.pack(pady=20)
win.mainloop()