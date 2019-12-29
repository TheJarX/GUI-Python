from tkinter import *

root = Tk()

lblUsername = Label(root, text='Username: ')
lblPassword = Label(root, text='Password: ')
# Text inputs
etyUser = Entry(root)
etyPass = Entry(root)
c = Checkbutton(root, text='Keep me logged in')

# By default: columns=0
lblUsername.grid(row=0, sticky=E)
lblPassword.grid(row=1, sticky=W)

etyUser.grid(row=0, column=1)
etyPass.grid(row=1, column=1)

c.grid(columnspan=2)


root.mainloop()