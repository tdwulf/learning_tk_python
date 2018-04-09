
from tkinter import *
from tkinter import messagebox

top =Tk()
C=Canvas(top,bg="red",height=200,width=250)

coord=10,50,240,200
arc = C.create_arc(coord,start=0,extent=150,fill="pink")

line = C.create_line(10,10,200,200,fill="white")

C.pack()
top.mainloop()