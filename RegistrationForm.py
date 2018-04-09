from tkinter import *

root =Tk()
root.geometry("600x600")

label_0= Label(root,text="Registration Form",width=20,font=("bold",20))
label_0.place(x=90,y=55)

label_1= Label(root,text="Full Name: ",width=20,font=("bold",12))
label_1.place(x=80,y=130)
entry_1=Entry(root)
entry_1.place(x=240,y=130)

label_2= Label(root,text="Email: ",width=20,font=("bold",12))
label_2.place(x=68,y=180)
entry_2=Entry(root)
entry_2.place(x=240,y=180)

label_3= Label(root,text="Gender: ",width=20,font=("bold",12))
label_3.place(x=70,y=230)
var=IntVar()

Radiobutton(root,text="Male",padx=5,variable=var,value=1).place(x=235,y=230)
Radiobutton(root,text="Female",padx=20,variable=var,value=2).place(x=290,y=230)

label_4 = Label(root, text="Country: ", width=20,font=("bold",12))
label_4.place(x=70,y=280)
list1=["Australia","Canada","USA","South Africa","Europe"];
c=StringVar()
droplist=OptionMenu(root,c,*list1)
droplist.config(width=20)
c.set("Select Your Country")
droplist.place(x=240,y=280)

label_4 = Label(root,text="Progamming Language: ",width=25,font=("bold",10))
label_4.place(x=85,y=330)
var1=IntVar()
Checkbutton(root,text="Python 2",variable=var1).place(x=235,y=330)
Checkbutton(root,text="Python 3",variable=var1).place(x=330,y=330)

Button(root,text="Submit",width=20,bg="green",fg="white").place(x=180,y=380)

mainloop()