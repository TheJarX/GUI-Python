from tkinter import *

root = Tk(screenName='My First Tkinter window')

lbl1 = Label(root, text='One', bg='red', fg='white')
lbl2 = Label(root, text='Two', bg='green', fg='white')
lbl3 = Label(root, text='Three', bg='purple', fg='white')
lbl4 = Label(root, text='Four', bg='yellow', fg='black')
lbl5 = Label(root, text='Five', bg='Orange', fg='white')

lbl1.pack()
lbl2.pack(fill=X)
lbl3.pack(side=LEFT, fill=Y)
lbl4.pack(side=RIGHT, fill=Y)
lbl5.pack(side=BOTTOM, fill=X)


root.mainloop()