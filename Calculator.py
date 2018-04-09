
import tkinter as tk 

class Calculator(object):
    def __init__(self,parent=tk.Tk()):

        self.parent=parent
        self.parent.title("Python Calculator")
        self.parent.option_add("*Font","Verdana 12 normal")

        self.decimal_point_open=False
        self.math_expression=None

        menu_bar=tk.Menu(self.parent)
        menu_bar.add_command(label="About",command=self.about)
        self.parent.config(menu=menu_bar)

        self.display_stringvar=tk.StringVar()
        display_entry_validate=(self.parent.register(self.only_number_entry),"%S","%d")
        self.display=tk.Entry(self.parent,font=("Verdana",20,"normal"),validate="key",validatecommand=display_entry_validate,textvariable=self.display_stringvar)
        self.display.bind("<Return>",self.calc_expression)

## Number KeyPad
        self.bt0=tk.Button(self.parent,text="0",command=lambda: self.button_press("0"))
        self.bt1=tk.Button(self.parent,text="1",command=lambda: self.button_press("1"))
        self.bt2=tk.Button(self.parent,text="2",command=lambda: self.button_press("2"))
        self.bt3=tk.Button(self.parent,text="3",command=lambda: self.button_press("3"))
        self.bt4=tk.Button(self.parent,text="4",command=lambda: self.button_press("4"))
        self.bt5=tk.Button(self.parent,text="5",command=lambda: self.button_press("5"))
        self.bt6=tk.Button(self.parent,text="6",command=lambda: self.button_press("6"))
        self.bt7=tk.Button(self.parent,text="7",command=lambda: self.button_press("7"))
        self.bt8=tk.Button(self.parent,text="8",command=lambda: self.button_press("8"))
        self.bt9=tk.Button(self.parent,text="9",command=lambda: self.button_press("9"))
        self.bt_plus=tk.Button(self.parent,text="+",command=lambda: self.button_press("+"))
        self.bt_sub=tk.Button(self.parent,text="-",command=lambda: self.button_press("-"))
        self.bt_multi=tk.Button(self.parent,text="*",command=lambda: self.button_press("*"))
        self.bt_divide=tk.Button(self.parent,text="/",command=lambda: self.button_press("/"))
        self.bt_point=tk.Button(self.parent,text=".",command=lambda: self.button_press("."))
        self.bt_equal=tk.Button(self.parent,text="=",command=lambda: self.button_press("="))
        self.bt_clear=tk.Button(self.parent,text="CLS",command=self.clear)
        self.bt_quit=tk.Button(self.parent,text="(ESC)",command=lambda: self.parent.destroy())
        self.parent.bind("<Escape>", lambda event=None:self.parent.destroy())
        self.mount_gui()
        self.parent.mainloop()

## Graphics component
    def mount_gui(self):
        self.display.grid(row=0,columnspan=4,sticky="ewns",ipady=5,padx=2,pady=2)
        self.bt0.grid(row=4,column=0,sticky="ewns",padx=2,pady=2)
        self.bt1.grid(row=3,column=0,sticky="ewns",padx=2,pady=2)
        self.bt2.grid(row=3,column=1,sticky="ewns",padx=2,pady=2)
        self.bt3.grid(row=3,column=2,sticky="ewns",padx=2,pady=2)
        self.bt4.grid(row=2,column=0,sticky="ewns",padx=2,pady=2)
        self.bt5.grid(row=2,column=1,sticky="ewns",padx=2,pady=2)
        self.bt6.grid(row=2,column=2,sticky="ewns",padx=2,pady=2)
        self.bt7.grid(row=1,column=0,sticky="ewns",padx=2,pady=2)
        self.bt8.grid(row=1,column=1,sticky="ewns",padx=2,pady=2)
        self.bt9.grid(row=1,column=2,sticky="ewns",padx=2,pady=2)
        self.bt_plus.grid(row=3,column=3,sticky="ewns",padx=2,pady=2)
        self.bt_sub.grid(row=2,column=3,sticky="ewns",padx=2,pady=2)
        self.bt_divide.grid(row=4,column=3,sticky="ewns",padx=2,pady=2)
        self.bt_multi.grid(row=1,column=3,sticky="ewns",padx=2,pady=2)
        self.bt_point.grid(row=4,column=1,sticky="ewns",padx=2,pady=2)
        self.bt_equal.grid(row=4,column=2,sticky="ewns",padx=2,pady=2)
        self.bt_clear.grid(row=5,column=0,columnspan=2,sticky="ewns",padx=2,pady=2)
        self.bt_quit.grid(row=5,column=2,columnspan=2,sticky="ewns",padx=2,pady=2)

### Calculator Clear Display
    def clear(self):
        self.display_stringvar.set("")
        self.decimal_point_open=False

### About Function
    def about(self):
        about_window=tk.Toplevel(self.parent)
        about_window.title("Python Calculator About")
        tk.Label(about_window, text="Calculator",font=("verdana",16,"bold")).grid(row=0,column=0,padx=5,pady=5,sticky="s")
        tk.Label(about_window, text="Python Calculator").grid(row=1,column=0,padx=5,pady=5,sticky="s")
        tk.Label(about_window, text="This Calculator developed in Python 3 using Tkinter").grid(row=3,column=0,padx=5,sticky="s")
        tk.Label(about_window, text="LIC: MIT").grid(row=4,column=0,padx=5,pady=5,sticky="s")

### Validation of Entries
    def only_number_entry(self,key_press,cod):
        valid_chars = "0123456789.+-*/"
        expression_now=self.display_stringvar.get()
        num_chars_now=len(expression_now)

        if(num_chars_now==0):
            valid_chars_for_init="0123456789"
            return key_press in valid_chars_for_init
        else:
            last_char=expression_now[num_chars_now-1]

            if(last_char in "+-*/" and key_press in "+-*/." and cod =="1"):
                return False
            
            elif(last_char in "+-*/" and key_press in "+-*/." and cod =="0"):
                return True
            elif(last_char == "." and key_press in "+-*/." and cod =="1"):
                return False
            elif(last_char == "." and key_press in "+-*/." and cod =="0"):
                return True
            elif(self.decimal_point_open and key_press=="."):
                return False
            elif(not self.decimal_point_open and key_press=="."):
                self.decimal_point_open = True
                return True
            elif(last_char in "0123456789" and key_press in "+-*/"):
                self.decimal_point_open=False
                return True

### interface button pressed 
    def button_press(self,bt):
        expression_now=self.display_stringvar.get()
        char_num=len(expression_now)
        if(char_num == 0):
            valid_chars_for_init="0123456789"
            if(bt in valid_chars_for_init):
                expression_now+=bt
                self.display_stringvar.set(expression_now)
        else:
            last_char=expression_now[char_num-1]
            if(bt=="." and not last_char in "+-*/"):
                if(self.decimal_point_open):
                    print("decimal point unavailable")
                else:
                    expression_now += bt
                    self.display_stringvar.set(expression_now)
                    self.decimal_point_open = True
            else:
                if(last_char in ".0123456789" and bt in "0123456789"):
                    expression_now+=bt
                    self.display_stringvar.set(expression_now)
                
                elif(last_char in "0123456789" and not self.decimal_point_open and bt in "+-*/"):
                    expression_now+=bt
                    self.display_stringvar.set(expression_now)
                    self.decimal_point_open=False
                elif(self.decimal_point_open and not last_char=='.' and bt in "+-*/"):
                    expression_now += bt
                    self.display_stringvar.set(expression_now)
                    self.decimal_point_open = False
                elif(last_char in "+-*/" and bt in "0123456789"):
                    expression_now+=bt
                    self.display_stringvar.set(expression_now)
                
                elif(bt=="=" and last_char in "0123456789"):
                ## Calc Expression
                    self.calc_expression()
    
    def prepare_expression(self):
        elementos=[]
        index=0
        for char in self.display_stringvar.get():
            if(len(elementos)==0 and char in "0123456789"):
                elementos.append(char)
            elif(len(elementos)>0 and char in "+-*/"):
                elementos.append(char)
                index+=1
            elif(elementos[index] in "+-*/"):
                elementos.append(char)
                index+=1
            else:
                elementos[index]+=char
        
        self.math_expression=elementos
    
    def calc_expression(self,event=None):
        self.prepare_expression()

        while("*"in self.math_expression or "/" in self.math_expression):
            index=0
            for element in self.math_expression:
                if(element == "*"):
                    v1=float(self.math_expression[index-1])
                    v2=float(self.math_expression[index+1])
                    result = str(v1*v2)
                    self.math_expression[index]=result
                    self.math_expression.pop(index+1)
                    self.math_expression.pop(index-1)
                    index+=1
                    break
                if(element=="/"):
                    v1=float(self.math_expression[index-1])
                    v2=float(self.math_expression[index+1])
                    result = str(v1/v2)
                    self.math_expression[index]=result
                    self.math_expression.pop(index+1)
                    self.math_expression.pop(index-1)
                    index+=1
                    break
                else:
                    index+=1

        while(len(self.math_expression)>1):
            index=0
            for element in self.math_expression:
                if(element=="+"):
                    v1=float(self.math_expression[index-1])
                    v2=float(self.math_expression[index+1])
                    result = str(v1+v2)
                    self.math_expression[index]=result
                    self.math_expression.pop(index+1)
                    self.math_expression.pop(index-1)
                    index+=1
                    break
                if(element == "-"):
                    v1=float(self.math_expression[index-1])
                    v2=float(self.math_expression[index+1])
                    result = str(v1-v2)
                    self.math_expression[index]=result
                    self.math_expression.pop(index+1)
                    self.math_expression.pop(index-1)
                    index+=1
                    break
                else:
                    index+=1
        final_result =str(round(float(self.math_expression[0]),1))
        self.display_stringvar.set(final_result)

if(__name__ == "__main__"):
    calc=Calculator()





        

