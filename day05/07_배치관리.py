from tkinter import *

win = Tk()
f = Frame(win)
win.geometry("200x200")
Button(f, text="버튼1", bg="yellow").pack(side="left")
Button(f, text="버튼2", bg="green").pack(side="left")
Button(f, text="버튼3", bg="blue").pack(side="left")

label = Label(win, text="버튼 위에 배치!")

label.pack()
f.pack()

# f.place(x=30, y=50)
win.mainloop()