from tkinter import *

def whatever():
    print('Hey bro, nice idk')

root = Tk()

''' **** MAIN MENU **** '''
menu = Menu(root)
root.config(menu=menu)

root.title("Hack NASA")
root.geometry("600x480")
root.resizable(False, False)
# root.minsize(600,480)
# root.maxsize(600,480)

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

''' **** STATUS BAR **** '''

#Bd stands for border
#relief
status = Label(root, text='Ready to hack NASA', 
                bd=1, 
                relief=SUNKEN,
                anchor=W
                )
status.pack(side=BOTTOM, fill=X)

root.mainloop()