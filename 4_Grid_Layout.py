from tkinter import *

root = Tk()

lblUsername = Label(root, text='Username: ')
lblPassword = Label(root, text='Password: ')
# Text inputs
etyUser = Entry(root)
etyPass = Entry(root)

# By default: columns=0
lblUsername.grid(row=0)
lblPassword.grid(row=1)

etyUser.grid(row=0, column=1)
etyPass.grid(row=1, column=1)

root.mainloop()