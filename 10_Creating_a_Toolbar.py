from tkinter import *

def whatever():
    print('Hey bro, nice idk')

root = Tk()

''' **** MAIN MENU **** '''
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

''' **** TOOLBAR ****'''
toolbar = Frame(root, bg='blue')

insertBtn = Button(toolbar, text='Insert Image', command=whatever)
insertBtn.pack(side=LEFT, padx=2, pady=2)

printBtn = Button(toolbar, text='Print', command=whatever)
printBtn.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

root.mainloop()