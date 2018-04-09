from tkinter import *

master=Tk()

def var_states():
    print("Male: %d,\nFemale %d" % (var1.get(),var2.get()))

Label(master,text="Your Gender:").grid(row=0,sticky=W)

var1=IntVar()
var2=IntVar()
Checkbutton(master,text="Male",variable=var1).grid(row=1,sticky=W) 
Checkbutton(master,text="Female",variable=var2).grid(row=2,sticky=W) 
Button(master,text="Quit",command=master.quit).grid(row=3,sticky=W,pady=4)
Button(master,text="Show",command=var_states).grid(row=4,sticky=W,pady=4)

mainloop()
