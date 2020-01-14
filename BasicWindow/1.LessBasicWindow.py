from tkinter import *

#Creating a blank window
root = Tk()

topFrame = Frame(root)  #Empty container in root
topFrame.pack()         #Placing it somewhere in the Window

botFrame = Frame (root)
botFrame.pack(side = BOTTOM)    #Second one is put in the bottom

btn1 = Button(topFrame, text = "OK", fg = "red", bg = "cyan")
btn2 = Button(topFrame, text = "NOT OK", fg = "green", bg = "cyan")
btn3 = Button(topFrame, text = "VERY NOT OK", fg = "blue", bg = "cyan")
btn4 = Button(botFrame, text = "OH NO", fg = "pink", bg = "black")

btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
btn4.pack()

root.mainloop()     #Window is constantlly displayed

