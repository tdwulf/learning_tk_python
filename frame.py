from tkinter import *

root = Tk()

frame=Frame(root)
frame.pack()

buttonframe=Frame(root)
buttonframe.pack(side=BOTTOM)

redbutton=Button(frame,text="Red",fg="red")
redbutton.pack(side=LEFT)
bluebutton=Button(frame,text="Blue",fg="blue")
bluebutton.pack(side=LEFT)
brownbutton=Button(frame,text="Brown",fg="brown")
brownbutton.pack(side=LEFT)
greenbutton=Button(frame,text="Green",fg="green")
greenbutton.pack(side=LEFT)
blackbutton=Button(frame,text="Black",fg="black")
blackbutton.pack(side=LEFT)

mainloop()