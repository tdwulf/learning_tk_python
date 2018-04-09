
from tkinter import *

root = Tk()

labelframe=LabelFrame(root,text="This is a label frame in tkinter.")

labelframe.pack(fill="both",expand="yes")

left=Label(labelframe,text="inside label frame text")
left.pack()

root.mainloop()