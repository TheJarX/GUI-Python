from tkinter import *

root = Tk()

root.resizable(False, False)

photo = PhotoImage(file='./img/15.gif')
label = Label(root, image=photo)

label.pack()


root.mainloop()