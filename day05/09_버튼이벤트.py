from tkinter import *

count = 0

def clicked() :
    # print(label['text'])
    global count
    count += 1
    label['text'] = count

win = Tk()
win.geometry("200x200")

label = Label(win, text="버튼 클릭하셈")
label.pack()
Button(win, text="클릭!", command=clicked).pack()


win.mainloop()