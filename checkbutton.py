
from tkinter import *

import tkinter

top=Tk()

CheckVar1=IntVar()
CheckVar2=IntVar()
C1=Checkbutton(top,text="Python 3",variable=CheckVar1,onvalue=1,offvalue=0,height=10,width=20)
C2=Checkbutton(top,text="Python 2",variable=CheckVar2,onvalue=1,offvalue=0,height=10,width=20)

C1.pack()
C2.pack()
top. mainloop()