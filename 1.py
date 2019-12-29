from tkinter import *

root = Tk(screenName='My First Tkinter window')
theLabel = Label(root, text='This is too easy!')
# We use this line to diplay the object
theLabel.pack()

root.mainloop()