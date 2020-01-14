from tkinter import *

#Creating a blank window
root = Tk()

#Variables are called lables
theLabel = Label(root, text = "This is easy")
theLabel.pack()     #It is put whenever the Tkinter wants, don't specify

root.mainloop()     #Window is constantlly displayed
