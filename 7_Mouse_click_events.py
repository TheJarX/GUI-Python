from tkinter import *

root = Tk()

# Remember alwasy add the ev parameter
def left(ev):
    print('left')

def right(ev):
    print('right')

def middle(ev):
    print('mid')

frame = Frame(root, width=300, height=300)

frame.bind('<Button-1>', left)
frame.bind('<Button-2>', middle)
frame.bind('<Button-3>', right)

frame.pack()

root.mainloop()