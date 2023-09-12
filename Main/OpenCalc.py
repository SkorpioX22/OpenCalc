import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def all_clear():
    entry.delete(0, tk.END)

def add_decimal():
    current = entry.get()
    if '.' not in current:
        entry.delete(0, tk.END)
        entry.insert(0, current + '.')

def operator_pressed(operator):
    global f_num
    global math
    math = operator
    f_num = float(entry.get())
    entry.delete(0, tk.END)

def equals():
    second_num = entry.get()
    entry.delete(0, tk.END)
    if math == "+":
        entry.insert(0, f_num + float(second_num))
    elif math == "-":
        entry.insert(0, f_num - float(second_num))
    elif math == "*":
        entry.insert(0, f_num * float(second_num))
    elif math == "/":
        if float(second_num) != 0:
            entry.insert(0, f_num / float(second_num))
        else:
            entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("OpenCalc")

# Create an entry widget for input with a monospace font
entry_font = ("Courier New", 24)
entry = tk.Entry(root, width=20, borderwidth=5, font=entry_font)
entry.grid(row=0, column=0, columnspan=4)

# Create number buttons with monospace text
button_font = ("Courier New", 18)
buttons = [
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2),
    ("0", 4, 1),
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=button_font, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Create decimal point button
decimal_button = tk.Button(root, text=".", padx=20, pady=20, font=button_font, command=add_decimal)
decimal_button.grid(row=4, column=0)

# Create operation buttons with monospace text
operation_buttons = [
    ("+", "+"), ("-", "-"), ("*", "*"), ("/", "/"),
]

row = 1
col = 3
for (text, operator) in operation_buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=button_font, command=lambda t=operator: operator_pressed(t))
    button.grid(row=row, column=col)
    row += 1

# Create equals, clear, and all clear buttons with monospace text
equals_button = tk.Button(root, text="=", padx=20, pady=20, font=button_font, command=equals)
equals_button.grid(row=4, column=2)

clear_button = tk.Button(root, text="C", padx=20, pady=20, font=button_font, command=clear)
clear_button.grid(row=4, column=1)

ac_button = tk.Button(root, text="AC", padx=20, pady=20, font=button_font, command=all_clear)
ac_button.grid(row=5, column=1)

root.mainloop()
