import tkinter as tk

app = tk.Tk()
app.title("Calculator")
app.geometry("350x450")

display = tk.Entry(app, font=("Arial", 20), borderwidth=5, relief="ridge")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def button_operator(operator):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + operator)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(app, text=text, padx=20, pady=20, font=("Arial", 14),
                           command=button_equal)
    else:
        button = tk.Button(app, text=text, padx=20, pady=20, font=("Arial", 14),
                           command=lambda t=text: button_click(t) if t not in '+-*/' else button_operator(t))
    button.grid(row=row, column=col, padx=5, pady=5)

button_clear = tk.Button(app, text='C', padx=20, pady=20, font=("Arial", 14),
                         command=button_clear)
button_clear.grid(row=4, column=2, padx=5, pady=5)

app.mainloop()