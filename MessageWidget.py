
from tkinter import * 

root =Tk()

var = StringVar()
label = Message(root,textvariable=var,relief=RAISED)
var.set("I am a message widget")

label.pack()
mainloop()
