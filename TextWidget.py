from tkinter import * 

root = Tk()

T=Text(root,height=2,width=30)

T.pack()
T.insert(END,"Just a text widget.\nSecond line of text.\n")

mainloop()