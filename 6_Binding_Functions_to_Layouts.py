from tkinter import *

root = Tk()

def printName(ev):
    print('Hello, my name is Gerard')

btnCallFn = Button(root, text='Print my name!')
btnCallFn.bind('<Button-1>', printName)
btnCallFn.pack()

root.mainloop()