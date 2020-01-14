from tkinter import *

root = Tk()

canvas = Canvas(root, width = 300, height = 200)
canvas.pack()

blackLine = canvas.create_line(0, 0, 150, 100)
redLine = canvas.create_line(0, 200, 150, 100, fill = "red")

greenBox = canvas.create_rectangle(100, 50, 200, 150, fill = "blue")

root.mainloop()
