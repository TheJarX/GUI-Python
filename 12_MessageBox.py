from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo(
    'Message',
    'This is a simpel info message. GOGOGO'
)

tkinter.messagebox.showerror(
    'Error!', 
    'An error has occurred'
)

tkinter.messagebox.askquestion(
    'We need an answer', 
    'R u Gay?'
)

tkinter.messagebox.showwarning(
    'Sure?',
    'Are you sure about that?'
)

answer = tkinter.messagebox.askquestion('Question 1', 'Have u got Money?')

if answer == 'no':
    print('F*ckin stingy')
else:
    print('Oh darling <3 ')
root.mainloop()