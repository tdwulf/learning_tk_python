# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 21:17:46 2018

@author: wulf
"""

from tkinter import *
from tkinter import messagebox

top =Tk()

top.geometry=("200x200")
def hellocallback():
    msg=messagebox.showinfo("Hello TkInter")

b=Button(top,text="ClickMe",command=hellocallback)
b.place(x=50, y=50)
top.mainloop()

