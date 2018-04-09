
from tkinter import *
import os

creds ="tempfile.txt"

def signup():
    global pwordE
    global nameE 
    global roots

    roots = Tk()
    roots.title("Sign Up")
    instruction = Label(roots,text="Please enter your credentials\n")
    instruction.grid(row=0,column=0,sticky=E)

    namel = Label(roots,text="New Username: ")
    pwordl = Label(roots,text="New Password: ")
    namel.grid(row=1,column=0,sticky=W)
    pwordl.grid(row=2,column=0,sticky=W)
    nameE = Entry(roots)
    pwordE = Entry(roots,show="*")
    nameE.grid(row=1,column=1)
    pwordE.grid(row=2,column=1)

    signupButton = Button(roots,text="Sign Up",command=FSSignup)
    signupButton.grid(columnspan=2,sticky=W)

    roots.mainloop()

def FSSignup():
    with open(creds,"w") as f:
        f.write(nameE.get())
        f.write("\n")
        f.write(pwordE.get())
        f.close()
    
    roots.destroy()
    login()


#### LOGIN ####

def login():
    global nameEL
    global pwordEL
    global rootA

    rootA = Tk()
    rootA.title("Login")

    instruction=Label(rootA,text="Please Log-in\n")
    instruction.grid(sticky=E)

    nameL =Label(rootA,text="Username: ")
    pwordL =Label(rootA,text="Password: ")
    nameL.grid(row=1,column=0)
    pwordL.grid(row=2,column=0)
    nameEL = Entry(rootA)
    pwordEL = Entry(rootA,show="*")
    nameEL.grid(row=1,column=1)
    pwordEL.grid(row=2,column=1)

    loginB = Button(rootA,text="Login", command=check_login)
    loginB.grid(columnspan=2, sticky=W)

    rmuser=Button(rootA,text="Delete User",fg="blue",command=del_user)
    rmuser.grid(columnspan=2,sticky=W)
    rootA.mainloop()

## CHECK LOGIN ## 

def check_login():
    with open(creds) as f:
        data = f.readlines()
        uname = data[0].rstrip()
        pword = data[1].rstrip()
    
    if nameEL.get() == uname and pwordEL.get() == pword:
        r = Tk()
        r.title("Welcome")
        r.geometry("150x150")
        rlabel= Label(r,text="Logged In")
        rlabel.pack()
        rlabel.mainloop()
    else:
        r=Tk()
        r.title("Oops")
        r.geometry("150x150")
        rlabel= Label(r,text="\n[!]Invalid Login")
        rlabel.pack()
        r.mainloop()


## DELETE USER ##

def del_user():
    os.remove(creds)
    rootA.destroy()
    signup()

if os.path.isfile(creds):
    login()

else:
    signup()

