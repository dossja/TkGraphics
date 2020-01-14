from tkinter import *

root = Tk()

l1 = Label(root, text = "Login")
ent1 = Entry(root)

l2 = Label(root, text = "Password")
ent2 = Entry(root)

l1.grid(row = 0, sticky = E)    #sticky = E - align to right side of it's container
l2.grid(row = 1, sticky = E)

ent1.grid(row = 0, column = 1)
ent2.grid(row = 1, column = 1)

cbtn = Checkbutton(root, text = "Are you ok?")
cbtn.grid(columnspan = 2)

root.mainloop()
