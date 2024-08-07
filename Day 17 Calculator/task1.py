import tkinter as tk
from tkinter import ttk
import math

# Function to switch to scientific calculator
def switch_to_scientific():
    for button in scientific_buttons:
        button.grid()

# Function to switch to basic calculator
def switch_to_basic():
    for button in scientific_buttons:
        button.grid_remove()

# Function to handle button click
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "AC":
        screen.set("")
    elif text == "+/-":
        if screen.get():
            if screen.get().startswith('-'):
                screen.set(screen.get()[1:])
            else:
                screen.set('-' + screen.get())
    else:
        screen.set(screen.get() + text)

# Creating the main window
root = tk.Tk()
root.geometry("300x400")
root.title("Calculator")

# Entry screen
screen = tk.StringVar()
entry = ttk.Entry(root, textvar=screen, font="lucida 20 bold")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, pady=10, sticky='nsew')

# Configure grid weights for resizing
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Button layout
buttons = [
    ['AC', '+/-', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '00', '.', '=']
]

scientific_buttons = []

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        button = ttk.Button(root, text=text)
        button.grid(row=i+1, column=j, ipadx=10, ipady=10, padx=5, pady=5, sticky='nsew')
        button.bind("<Button-1>", click)
        if text in ['sin', 'cos', 'tan', 'log']:
            scientific_buttons.append(button)

# Adding scientific buttons
scientific_operations = ['sin', 'cos', 'tan', 'log']
for i, op in enumerate(scientific_operations):
    button = ttk.Button(root, text=op)
    button.grid(row=i+1, column=4, ipadx=10, ipady=10, padx=5, pady=5, sticky='nsew')
    button.bind("<Button-1>", click)
    scientific_buttons.append(button)
    button.grid_remove()

# Toggle button
toggle_button = ttk.Button(root, text="Scientific", command=switch_to_scientific)
toggle_button.grid(row=6, column=0, columnspan=2, ipadx=10, ipady=10, padx=5, pady=5, sticky='nsew')

# Basic button
basic_button = ttk.Button(root, text="Basic", command=switch_to_basic)
basic_button.grid(row=6, column=2, columnspan=2, ipadx=10, ipady=10, padx=5, pady=5, sticky='nsew')

# Main loop
root.mainloop()
