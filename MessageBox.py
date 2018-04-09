
from tkinter import *
from tkinter import messagebox

top=Tk()
top.geometry("200x200")

def hello():
    messagebox.showinfo("Click Me","Hi User")

b1= Button(top,text="Click Me",command=hello)
b1.place(x=35,y=50)

top.mainloop()
