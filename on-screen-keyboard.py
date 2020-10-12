# for python2
try:
    import TKinter as tk
except ImportError:
    import tkinter as tk

from functools import partial

# import tkinter library with an alias
from tkinter import *
import tkinter as tk

# initialise the tkinter app
keyboardApp = tk.Tk()
# title 
keyboardApp.title("On-Screen Keyboard")
# keyboardApp.wm_iconbitmap('/images/keyboard_5643.ico')
# img = PhotoImage(file = 'images/keyboard_5643.ico')
# keyboardApp.tk.call('wm', 'iconphoto', keyboardApp._w, img)
# keyboardApp ['bg'] = 'powder blue'
keyboardApp.config(bg='powder blue')
# disable resizeable property
keyboardApp.resizable(0, 0)

# give a heading for the app
label1 = Label(keyboardApp, text = 'On-screen Keyboard',
               font=('arial', 30, 'bold'),
               bg = 'powder blue',
               fg = '#000000')
               
# form the heading
label1.grid(row = 0, columnspan = 40)

# text box 
textBox = Text(keyboardApp, width = 138, font = (
    'arial', 10, 'bold'))

# form the textbox
textBox.grid(row = 1, columnspan = 40)

# buttons list
buttons = [
    '!', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '<-', '7', '8', '9', '-',
    'Tab', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '[', ']', '4', '5', '6', '+',
    'SHIFT', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '?', 'SHIFT', '1', '2', '3',
    ' Space ' 
]

# initialise row, col for buttons
varRow = 3
varCol = 0

for button in buttons:
    # command to run on every button click - select() function 
    cmd = lambda x = button: select(x)

    # for every button except 'space'
    if button != ' Space ':
        tk.Button(keyboardApp,
        text = button, 
        width = 5,
        bg = 'powder blue',
        fg = '#000000',
        activebackground = '#ffffff',
        activeforeground = '#000990',
        relief = 'raised',
        padx = 3,
        pady = 3, 
        bd = 12,
        font=('arial', 12, 'bold'),
        command = cmd).grid(row = varRow, column = varCol)

    # for the space button
    if button == ' Space ':
        tk.Button(keyboardApp, 
        text = button,
        width = 118, 
        bg = 'powder blue',
        fg = '#000000',
        activebackground = '#ffffff',
        activeforeground = '#000990',
        relief = 'raised',
        padx = 3,
        pady = 3, 
        bd = 12,
        font=('arial', 12, 'bold'),
        command = cmd).grid(row = 6, columnspan = 16)

    # go to next column for every different button
    varCol += 1

    # if number of buttons in one line crosses 15
    if varCol > 15 and varRow == 3:
        varCol = 0
        varRow += 1 

    if varCol > 15 and varRow == 4:
        varCol = 0
        varRow += 1 

# run the main loop of the app
keyboardApp.mainloop()