from tkinter import *

def whatever():
    print('Hey bro, nice idk')

root = Tk()

menu = Menu(root)
root.config(menu=menu)

# tearoff remueve los puntos que permiten que el menu se abra en una nueva ventana
subMenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Nothing',menu=subMenu)
subMenu.add_command(label='Really nothing', command=whatever)
subMenu.add_command(label='Maybe something', command=whatever)
subMenu.add_separator()
subMenu.add_command(label='Exit', command=whatever)

editMenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Tools', menu=editMenu)
editMenu.add_command(label='Redo', command=whatever)

root.mainloop()