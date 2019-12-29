from tkinter import *
class myButtons:
    def __init__(self,master):
        self.master = master
        self.frame = Frame(master, bg='red')
        self.frame.pack()
        self.btnCreated = False

        self.btnPrint = Button(self.frame, 
            text='Print message and show button', 
            command=self.printMsg
        )
        self.btnPrint.pack(side=LEFT)

        self.btnQuit = Button(self.frame, text='Exit', command=self.frame.quit)
        self.btnQuit.pack(side=LEFT)

    def printMsg(self): 
        self.showAnotherBtn()
        print('Hey there!')
    
    def showAnotherBtn(self):
        if not self.btnCreated:
            self.newFrame = Frame(self.master)
            self.newFrame.pack()
            btnAdd = Button(self.newFrame, text='idk if this will work')
            btnAdd.pack()
            self.btnCreated = True
        else:
            self.newFrame.destroy()
            self.btnCreated = False

root = Tk()

myButtons(root)

root.mainloop()