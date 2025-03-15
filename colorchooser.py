from tkinter import *
from tkinter import colorchooser
root=Tk()
def show():
    myc=colorchooser.askcolor()[1]
    l=Label(root,text=myc).pack()
    l=Label(root,text="New color",bg=myc).pack()
b=Button(root,text="Colors",command=show).pack()
root.mainloop()