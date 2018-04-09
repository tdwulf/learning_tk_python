
from tkinter import * 

root =Tk()

v=IntVar()

Label(root,text="""choose a programming language :""",justify=LEFT,padx=20).pack()

Radiobutton(root,text="Python 3",padx=20,variable=v,value=1).pack(anchor=W)
Radiobutton(root,text="Python 2",padx=20,variable=v,value=2).pack(anchor=W)
mainloop()
