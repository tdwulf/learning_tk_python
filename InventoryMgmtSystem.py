
from tkinter import *
import tkinter.messagebox as tkmessagebox
import sqlite3
import tkinter.ttk as ttk 

root=Tk()
root.title("Python Inventory Management System")
width=1024
height=720
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x=(screen_width/2) - (width/2)
y=(screen_height/2) - (height/2)

root.geometry("%dx%d+%d+%d" % (width,height,x,y))
root.resizable(0,0)
root.config(bg="#800000")

## Variables 
USERNAME = StringVar()
PASSWORD = StringVar()
PRODUCT_NAME = StringVar()
PRODUCT_PRICE = IntVar()
PRODUCT_QTY = IntVar()
SEARCH = StringVar()

## METHODS 

def database():
    global conn,cursor
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'admin' (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS 'product' (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT, product_qty TEXT, product_price TEXT)")
    cursor.execute("SELECT * FROM 'admin' WHERE 'username' ='admin' AND 'password' = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO 'admin' (username,password) VALUES('admin','admin')")
        conn.commit()

#exit

def Exit():
    result=tkmessagebox.askquestion("Python Inventory Management System","Are you sure you want to exit? ",icon="warning")
    if result == "yes":
        root.destroy()
        exit()

def Exit2():
    result=tkmessagebox.askquestion("Python Inventory Management System","Are you sure you want to exit? ",icon="warning")
    if result == "yes":
        Home.destroy()
        exit()  

def ShowLoginForm():
    global loginform
    loginform=Toplevel()
    loginform.title("Python Inventory Management System - Account/Login")
    width=600
    height=500
    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()
    x=(screen_width/2)-(width/2)
    y=(screen_height/2)-(height/2)
    loginform.resizable(0,0)
    loginform.geometry("%dx%d+%d+%d" % (width,height,x,y))
    LoginForm()

#login form
def LoginForm():
    global lbl_result
    TopLoginForm=Frame(loginform,width=600,height=100,bd=1,relief=SOLID)
    TopLoginForm.pack(side=TOP,pady=20)
    lbl_text=Label(TopLoginForm,text="Admin Login",font=("arial",18),width=600)
    lbl_text.pack(fill=X)
    MidLoginForm=Frame(loginform,width=400)
    MidLoginForm.pack(side=TOP,pady=50)
    lbl_username=Label(MidLoginForm,text="Username:",font=("arial",18),bd=18)
    lbl_username.grid(row=0)
    lbl_password=Label(MidLoginForm,text="Password: ",font=("arial",18),bd=18)
    lbl_password.grid(row=1)
    lbl_result=Label(MidLoginForm,text="",font=("arial",18))
    lbl_result.grid(row=3,columnspan=2)
    username=Entry(MidLoginForm,textvariable=USERNAME,font=("arial",25),width=15)
    username.grid(row=0,column=1)
    password=Entry(MidLoginForm,textvariable=PASSWORD,font=("arial",25),width=15,show="*")
    password.grid(row=2,column=1)
    btn_login=Button(MidLoginForm,text="Login",font=("arial",18),width=30,command=Login)
    btn_login.grid(row=2,columnspan=2,pady=20)
    btn_login.bind("<Return>",Login)

## HOME

def Home():
    global Home
    Home = Tk()
    Home.title("Python Inventory Management System - Home")
    width = 1024
    height = 720
    screen_width=Home.winfo_screenwidth()
    screen_height=Home.winfo_screenheight()
    x=(screen_width/2)-(width/2)
    y=(screen_height/2)-(height/2)
    Home.geometry("%dx%d+%d+%d" % (width,height,x,y))
    Home.resizable(0,0)
    Title= Frame(Home,bd=1,relief=SOLID)
    Title.pack(pady=10)
    lbl_display=Label(Title,text="Python Inventory Management System",font=("arial",45))
    lbl_display.pack()
    menubar=Menu(Home)
    filemenu = Menu(menubar,tearoff=0)
    filemenu2 = Menu(menubar,tearoff=0)
    filemenu.add_command(label="Logout",command=Logout)
    filemenu2.add_command(label="Exit",command=Exit2)
    filemenu2.add_command(label="Add New",command=ShowAddNew)
    filemenu2.add_command(label="View",command=ShowView)
    menubar.add_cascade(label="Account",command=filemenu)
    menubar.add_cascade(label="Inventory",command=filemenu2)
    Home.config(menu=menubar)
    Home.config(bg="#99FF99")

## Show add New Item

def ShowAddNew():
    global addnewform
    addnewform=Toplevel()
    addnewform.title("Python Inventory Management System - Add New")
    width = 600
    height = 500
    screen_width=Home.winfo_screenwidth()
    screen_height=Home.winfo_screenheight()
    x=(screen_width/2)-(width/2)
    y=(screen_height/2)-(height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width,height,x,y))
    addnewform.resizable(0,0)
    AddNewForm()

# ADD New Form
def AddNewForm():
    TopAddNew=Frame(addnewform,width=600,height=100,bd=1,relief=SOLID)
    TopAddNew.pack(side=TOP,pady=20)
    lbl_text=Label(TopAddNew,text="Add New Product",font=("arial",18),width=600)
    lbl_text.pack(fill=X)
    MidAddNew=Frame(addnewform,width=600)
    MidAddNew.pack(side=TOP,pady=50)
    lbl_productname=Label(MidAddNew,text="Product Name: ",font=("arial",25),bd=10)
    lbl_productname.grid(row=0,sticky=W)
    lbl_qty=Label(MidAddNew,text="Product Qty: ",font=("arial",25),bd=10)
    lbl_qty.grid(row=1,sticky=W)
    lbl_price=Label(MidAddNew,text="Product Price: ",font=("arial",25),bd=10)
    lbl_price.grid(row=2,sticky=W)
    productname=Entry(MidAddNew,textvariable=PRODUCT_NAME,font=("arial",25),width=15)
    productname.grid(row=0,column=1)
    productqty=Entry(MidAddNew,textvariable=PRODUCT_QTY,font=("arial",25),width=15)
    productqty.grid(row=1,column=1)
    productprice=Entry(MidAddNew,textvariable=PRODUCT_PRICE,font=("arial",25),width=15)
    productprice.grid(row=2,column=1)
    btn_add=Button(MidAddNew,text="ADD",font=("arial",18),width=30,bg="#009ACD",command=ShowAddNew)
    btn_add.grid(row=3,columnspan=2,pady=20)

# View Form

def ViewForm():
    global tree 
    TopViewForm=Frame(ViewForm,width=600,bd=1,relief=SOLID)
    TopViewForm.pack(side=TOP,fill=X)
    LeftViewForm=Frame(ViewForm,width=600)
    LeftViewForm.pack(side=LEFT,fill=X)
    MidViewForm=Frame(ViewForm,width=600)
    MidViewForm.pack(side=RIGHT,fill=X)
    lbl_text=Label(TopViewForm,text="View Product",font=("arial",18),width=600)
    lbl_text.pack(fill=X)
    lbl_textsearch=Label(LeftViewForm,text="Search",font=("arial",15))
    lbl_textsearch.pack(side=TOP,anchor=W)
    search=Entry(LeftViewForm,textvariable=SEARCH,font=("arial",15),width=10)
    search.pack(side=TOP,padx=10,pady=10,fill=X)
    btn_search=Button(LeftViewForm,text="Search",command=Search)
    btn_search.pack(side=TOP,padx=10,pady=10,fill=X)
    btn_reset=Button(LeftViewForm,text="Search",command=Search)
    btn_reset.pack(side=TOP,padx=10,pady=10,fill=X)
    btn_delete=Button(LeftViewForm,text="Search",command=Search)
    btn_delete.pack(side=TOP,padx=10,pady=10,fill=X)
    scrollbarx=Scrollbar(MidViewForm,orient=HORIZONTAL)
    scrollbary=Scrollbar(MidViewForm,orient=VERTICAL)
    tree=ttk.Treeview(MidViewForm,columns=("ProductID","Product Name","Product Qty","Product Price"),selectmode="database",height=100,yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT,fill=X)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM,fill=X)

    tree.heading("ProductID",text="ProductID",anchor=W)
    tree.heading("Product Name",text="Product Name",anchor=W)
    tree.heading("Product Qty",text="Product Qty",anchor=W)
    tree.heading("Product Price",text="Product Price",anchor=W)
    tree.column("#0",stretch=False,minwdith=0,width=0)
    tree.column("#1",stretch=False,minwdith=0,width=0)
    tree.column("#2",stretch=False,minwdith=0,width=200)
    tree.column("#3",stretch=False,minwdith=0,width=120)
    tree.column("#4",stretch=False,minwdith=0,width=120)
    tree.pack()
    DisplayData()

## Display Data Method
def DisplayData():
    database()
    cursor.execute("SELECT * FROM 'product'")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert("","end",values=(data))
    cursor.close()
    conn.close()

## SEARCH Method

def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        database()
        cursor.execute("SELECT * FROM 'product' WHERE 'product_name' LIKE ?",("%"+str(SEARCH.get())+"%",))
        fetch=cursor.fetchall()
        for data in fetch:
            tree.insert("","end",value(data))
        cursor.close()
        conn.close()

#RESET Method

def Reset():
    tree.delete(*tree.get_children)
    DisplayData()
    SEARCH.set("")

#Delete Method

def Delete():
    if not tree.selection():
        print("ERROR")
    else:
        result=tkmessagebox.askquestion("Python Inventory Management System","Are you sure you want to delete item?",icon="warning")
        if result == "yes":
            curItem=tree.focus()
            contents=(tree.item(curItem))
            selecteditem=contents["values"]
            tree.delete(curItem)
            database()
            cursor.execute("DELETE FROM 'product' WHERE 'product_id'=%d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

## View Product

def ShowView():
    global viewform 
    viewform=Toplevel()
    viewform.title=("Python Inventory Management System - View Product")
    width=600
    height=400
    screen_width=Home.winfo_screenwidth()
    screen_height=Home.winfo_screenheight()
    x=(screen_width/2)-(width/2)
    y=(screen_height/2)-(height/2)
    viewform.geometry("%dx%d+%d+%d" % (width,height,x,y))
    viewform.resizable(0,0)
    ShowView()

# Login / Log Out Form

def Logout():
    result=tkmessagebox.askquestion("Python Inventory Management System","Are you sure you want to log out?",icon="warning")
    if result == "yes":
        admin_id=""
        root.deiconify()
        Home.destroy()

def Login(event=None):
    global admin_id
    database()
    if USERNAME.get()=="" or PASSWORD.get()=="":
        lbl_result.config(text="Please Complete the required field(s)",fg="red")
    else:
        cursor.execute("SELECT * FROM 'admin' WHERE 'username'=? AND 'password'=?",(USERNAME.get(),PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM 'admin' WHERE 'username'=? AND 'password'=?",(USERNAME.get(),PASSWORD.get()))
            data=cursor.fetchone()
            admin_id=data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            ShowHome()
        else:
            lbl_result.config(text="Invalid Login Credentials",fg="red")
            USERNAME.set("")
            PASSWORD.set("")
        cursor.close()
        conn.close()

def ShowHome():
    root.widthdraw()
    Home()
    loginform.destroy()

## MenuBar Widgets

menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Account",command=ShowLoginForm)
filemenu.add_command(label="Exit",command=Exit)
menubar.add_cascade(label="File",command=filemenu)
root.config(menu=menubar)

Title= Frame(root,bd=1,relief=SOLID)
Title.pack(pady=10)
lbl_display=Label(Title,text="Python Inventory Management System",font=("arial",45))
lbl_display.pack()

if __name__ == "__main__":
    root.mainloop()
