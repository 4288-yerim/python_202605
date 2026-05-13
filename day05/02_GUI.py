from tkinter import *

window = Tk()
window.title("첫번째 프로그램!")
window.geometry("500x500")
label = Label(window, text="Hello Python")
label.pack()

window.mainloop()