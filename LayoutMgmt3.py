
import tkinter as tk
import random

root = tk.Tk()
root.geometry("170x500+30+30")

lang=["Python 3","Python 2","JS","Ruby","C++","HTML"]
label=range(len(lang))

for i in range(len(lang)):
    ct=[random.randrange(256) for x in range(3)]
    brightness=int(round(0.299*ct[0]+0.587*ct[1]+0.114*ct[2]))
    ct_hex="%02x%02x%02x" % tuple(ct)
    bg_color="#"+"".join(ct_hex)
    l=tk.Label(root,text=lang[i],fg="white" if brightness < 120 else "black", bg=bg_color)
    l.place(x=20,y=30+i*30,width=120,height=25)

root.mainloop()