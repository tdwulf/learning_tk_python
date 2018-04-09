
from tkinter import *

root = Tk()

var =StringVar()
label=Label(root,textvariable=var,relief =RAISED)

var.set("Im a label")
label.pack()
root.mainloop()