from tkinter import *

def doNothing():
    print("Do I do something or nothing?")

root = Tk()

#   Main Menu

mainMenu = Menu(root)
root.config(menu = mainMenu)

subMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "File", menu = subMenu)

subMenu.add_command(label = "New", command = doNothing)
subMenu.add_command(label = "Open", command = doNothing)
subMenu.add_command(label = "Start Page", command = doNothing)
subMenu.add_separator()
subMenu.add_command(label = "Exit", command = root.quit)

editMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "Edit", menu = editMenu)

editMenu.add_command(label = "Go To", command = doNothing)
editMenu.add_command(label = "Find and Replace", command = doNothing)

# Toolbar

toolbar = Frame(root, bg = "gray")

insertBtn = Button(toolbar, text = "Insert?", command = doNothing)
insertBtn.pack(side = LEFT, padx = 2, pady = 2)
printBtn = Button(toolbar, text = "Print?", command = doNothing)
printBtn.pack(side = LEFT, padx = 2, pady = 2)

toolbar.pack(side = TOP, fill = X)

#   Status Bar

status = Label(root, text = "Preparing...", bd = 1, relief = SUNKEN, anchor = W)
status.pack(side = BOTTOM, fill = X)

root.mainloop()
