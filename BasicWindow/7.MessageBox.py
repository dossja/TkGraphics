from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Window Title', 'Some fun fact')

answer = tkinter.messagebox.askquestion('Quest. 1', 'Do you like this program?')

if answer == 'yes':
    print(':)')
else:
    print(':\'(')

root.mainloop()
