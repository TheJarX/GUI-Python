from tkinter import *

root = Tk()

topFrame = Frame(root)
# By default an object is palced on the top
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

btn1 = Button(topFrame,text='Click me! 1', fg="red")
btn2 = Button(topFrame,text='Click me! 2', fg="blue")
btn3 = Button(topFrame,text='Click me! 3', fg="orange")
btn4 = Button(bottomFrame,text='Click me! 4', fg="green")

btn1.pack(side=RIGHT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
btn4.pack(side=BOTTOM)

root.mainloop()