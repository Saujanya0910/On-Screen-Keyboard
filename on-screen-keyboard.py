# import tkinter library with an alias
from tkinter import *
import tkinter as tk

from functools import partial

keyboardApp = tk.Tk()   # initialise the tkinter app
keyboardApp.title("On-Screen Keyboard")     # title 
keyboardApp.wm_iconbitmap('On-Screen-Keyboard\images\keyboard_5643.ico')       # icon - ADD YOUR RELATIVE PATH IF ICON DOESN'T LOAD
keyboardApp.config(bg='powder blue')    # background
keyboardApp.resizable(0, 0)     # disable resizeable property

# heading for the app
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
    '!', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '←', '7', '8', '9', '-',
    'Tab', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '[', ']', '4', '5', '6', '+',
    'Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '?', '1', '2', '3', '*',
    ' Space ' 
]

# initialise row, col for buttons
varRow = 3
varCol = 0

# toggle shift button press
shift_on = False
# save references of letter buttons
letter_buttons = []

# check if the button corresponds to a letter
def is_letter(s):
    return len(s) == 1 and 'a' <= s <= 'z'

# function for button click
def buttonClick(input):
    global shift_on

    if input == 'Shift':
        # toggle shift status
        shift_on = not shift_on
        # update text of letter buttons according to status of shift btn
        for btn in letter_buttons:
            text = btn['text']
            btn['text'] = text.upper() if shift_on else text.lower()
    else:
        if input == ' Space ':
            textBox.insert(INSERT,' ')
        elif input == 'Tab':
            textBox.insert(INSERT, '    ')
        elif input == '←':
            backspace()
        else:
            # update text of letter buttons
            if is_letter(input):
                input = input.upper() if shift_on else input.lower()
            textBox.insert(INSERT, input)

# function for backspace
def backspace():
    textBox.delete('insert-1chars', INSERT)

for button in buttons:
    # command to run on every button click - buttonClick() function 
    cmd = lambda x = button: buttonClick(x)

    # for every button except 'space'
    if button != ' Space ':
        btn = tk.Button(keyboardApp,
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
            command = cmd)
        btn.grid(row = varRow, column = varCol)
        # save reference of letter buttons
        if is_letter(button):
            letter_buttons.append(btn)

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

    # if number of buttons in one line crosses 15, go to next row and 0th col
    if varCol > 15 and varRow == 3:
        varCol = 0
        varRow += 1 

    if varCol > 15 and varRow == 4:
        varCol = 0
        varRow += 1 

# run the main loop of the app
keyboardApp.mainloop()