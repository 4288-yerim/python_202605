from tkinter import *

win = Tk()
win.geometry("200x200")
Button(win, text="버튼1", bg="yellow").grid(row=0, column=0)
Button(win, text="버튼2", bg="green").grid(row=0, column=1)
Button(win, text="버튼3", bg="blue").grid(row=1, column=0)
Button(win, text="버튼4", bg="orange").grid(row=1, column=1)

win.mainloop()