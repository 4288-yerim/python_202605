from tkinter import *

win = Tk()
win.geometry("200x200")
Button(win, text="버튼1", bg="yellow").place(x=5, y=5)
Button(win, text="버튼2", bg="green").place(x=20, y=50)
Button(win, text="버튼3", bg="blue").place(x=50, y=30)
Button(win, text="버튼4", bg="orange").place(x=100, y=100)

win.mainloop()