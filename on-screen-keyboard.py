# import tkinter library with an alias
from tkinter import *
import tkinter as tk

from functools import partial

# initialise the tkinter app
keyboardApp = tk.Tk()
# title 
keyboardApp.title("On-Screen Keyboard")
# icon
keyboardApp.wm_iconbitmap('on-screen-keyboard\images\keyboard_5643.ico')
# background
keyboardApp.config(bg='powder blue')
# disable resizeable property
keyboardApp.resizable(0, 0)

# give a heading for the app
label1 = Label(keyboardApp, text = 'On-screen Keyboard',
               font=('arial', 30, 'bold'),
               bg = 'powder blue',
               fg = '#000000')
               
# create the heading
label1.grid(row = 0, columnspan = 40)

# text box 
textBox = Text(keyboardApp, 
                width = 180, 
                font = ('arial', 10, 'bold'),
                wrap = WORD)

# create the textbox and focus
textBox.grid(row = 1, columnspan = 40)
textBox.focus()

# buttons list
buttons = [
    '!', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '<-', '7', '8', '9', '-',
    'Tab', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '[', ']', '4', '5', '6', '+',
    'Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '?', 'Shift', '1', '2', '3',
    ' Space ' 
]

# initialise row, col for buttons
varRow = 3
varCol = 0

# function for backspace
def backspace():
    text = textBox.get('1.0', 'end-1c')
    text = text[:-1]
    textBox.delete('1.0', INSERT)
    textBox.insert('1.0', text)

def shift():
    while input == 'Shift':
        tk.Button(keyboardApp, relief = 'raised')

# function for button click
def buttonClick(input):
    if input == ' Space ':
        textBox.insert(INSERT,' ')
    elif input == 'Tab':
        textBox.insert(INSERT, '    ')
    elif input == 'Tab':
        textBox.insert(INSERT, '    ')
    elif input == '<-':
        backspace()
    else:
        if input != 'Shift':
            textBox.insert(INSERT, input)
        else:
            shift()

for button in buttons:
    # command to run on every button click - buttonClick() function 
    cmd = lambda x = button: buttonClick(x)

    # for every button except 'space'
    if button != ' Space ':
        tk.Button(keyboardApp,
            text = button, 
            width = 7,
            bg = 'black',
            fg = 'white',
            activebackground = 'white',
            activeforeground = 'black',
            relief = 'raised',
            padx = 3,
            pady = 3, 
            bd = 5,
            font=('arial', 12, 'bold'),
            command = cmd).grid(row = varRow, column = varCol)

    # for the space button
    if button == ' Space ':
        tk.Button(keyboardApp, 
            text = button,
            width = 50, 
            bg = 'black',
            fg = 'white',
            activebackground = 'white',
            activeforeground = 'black',
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