from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

blackLn = canvas.create_line(0, 0, 200, 50)
redLn = canvas.create_line(0, 100, 200, 50, fill='red')

''' 

canvas.delete(redLn)
canvas.delte(ALL)

'''

root.mainloop()