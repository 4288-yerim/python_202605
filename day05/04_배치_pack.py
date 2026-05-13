from tkinter import *

win = Tk()
win.geometry("200x200")
Button(win, text="버튼1", bg="yellow").pack(side="left")
Button(win, text="버튼2", bg="green").pack(side="left")
Button(win, text="버튼3", bg="blue").pack(side="left")

win.mainloop()