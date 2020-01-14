from tkinter import *

root = Tk()

l1 = Label(root, text = "Hello from the other side", bg = "black", fg = "white")
l1.pack()           #Label container is as big as a label is

l2 = Label(root, text = "Hello from the othereees side :)", bg = "black", fg = "yellow")
l2.pack(fill = X)   #Label container is has the same height as label, but is as wide as Window (if nothing blocking on a side)

l3 = Label(root, text = "Hello from the nowhere side :)", bg = "black", fg = "green")
l3.pack(side = LEFT, fill = Y)  #Label container is has the same width as label, but is as high as Window (if nothing blocking on a top/bottom)
                                #It is also glued to the left side of the Window

root.mainloop()
