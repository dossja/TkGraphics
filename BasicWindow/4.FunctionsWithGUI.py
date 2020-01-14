from tkinter import *

root = Tk()

#def printName(event):
#    print("Hello from GUI")

#btn1 = Button(root, text = "Say Hello", command = printName) #def without 'event'
#btn1 = Button(root, text = "Say Hello")
#btn1.bind("<Button-1>", printName)
#btn1.pack()

def leftClick(event):
    print("Left Mouse Button")
        
def middleClick(event):
    print("Middle Mouse Button")
    
def rightClick(event):
    print("Right Mouse Button")


frame = Frame(root, width = 300, height = 300)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)

frame.pack()

root.mainloop()
