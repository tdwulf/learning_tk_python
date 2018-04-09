
from tkinter import *

root = Tk()

S=Scrollbar(root)
T=Text(root,height=20,width=50)
S.pack(side=RIGHT,fill=Y)
T.pack(side=LEFT,fill=Y)

S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote ="""My name is Wulfie. 
I am an Awesome Programmer.
Always learning new code.
Lorem ipsum dolor sit amet, 
consectetur adipiscing elit. 
Duis in ullamcorper eros, 
posuere dignissim elit. 
Praesent molestie gravida rhoncus. 
Curabitur aliquet risus ac ornare 
pharetra. Donec vitae dictum ante, 
non iaculis tellus. In suscipit, 
metus id accumsan ornare, 
enim mi facilisis metus, 
eu pretium quam massa sed nisl. 
Nunc hendrerit ligula nec mi interdum, 
in tempus lorem molestie. 
Maecenas dignissim elit odio, 
ac porttitor velit cursus ac. 
Morbi lectus dolor, 
vulputate at venenatis eu, 
iaculis consequat ante. 
Integer auctor suscipit dui, 
ut aliquet augue tristique vel. C
urabitur placerat sagittis enim,
et varius nibh ultrices vel. 
Donec a tincidunt nunc. 
Fusce porttitor enim at lacus 
dignissim pulvinar. 
Nunc aliquam fermentum 
lorem in facilisis."""

T.insert(END,quote)
mainloop()