
from tkinter import Tk,Toplevel,Button

root = Tk()

second_window=Toplevel()
second_window.title("Second Window")

def destroy_second_window():
    second_window.destroy()

close_button = Button(root,text="Close Second Window", command=destroy_second_window)
close_button.pack()
root.mainloop()



