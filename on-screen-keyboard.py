try:
    import TKinter as tk
except ImportError:
    import tkinter as tk

from functools import partial

from tkinter import *
import tkinter as tk

keyboardApp = tk.Tk()
keyboardApp.title("On-Screen Keyboard")
# keyboardApp.wm_iconbitmap('/images/keyboard_5643.ico')
# img = PhotoImage(file = 'images/keyboard_5643.ico')
# keyboardApp.tk.call('wm', 'iconphoto', keyboardApp._w, img)
# keyboardApp ['bg'] = 'powder blue'
keyboardApp.config(bg='powder blue')
keyboardApp.resizable(0, 0)

label1 = Label(keyboardApp, text = 'On-screen Keyboard',
               font=('arial', 30, 'bold'),
               bg = 'powder blue',
               fg = '#000000').grid(row = 0, columnspan = 40)
entry = Text(keyboardApp, width = 138, font = (
    'arial', 10, 'bold')).grid(row = 1, columnspan = 40)

buttons = [
    '!', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '<-', '7', '8', '9', '-',
    'Tab', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '[', ']', '4', '5', '6', '+',
    'SHIFT', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '?', 'SHIFT', '1', '2', '3',
    ' Space ' 
]

varRow = 3
varCol = 0

for button in buttons:
    cmd = lambda x = button: select(x)
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

    varCol += 1
    if varCol > 15 and varRow == 3:
        varCol = 0
        varRow += 1 

    if varCol > 15 and varRow == 4:
        varCol = 0
        varRow += 1 

keyboardApp.mainloop()