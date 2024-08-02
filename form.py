import tkinter as tk
import os 




app = tk.Tk()
app.title("Form")
app.geometry("500x500")
address = tk.StringVar()
name = tk.StringVar()
email = tk.StringVar()


def show():
    if not os.path.exists('form.txt'):
        with open("form.txt", 'a') as f:
           f.writelines("Name:"+"Address:"+"Email")
           f.write(f"{name.get()},{address.get()},{email.get()}")


tk.Label(app, text="Name:").pack()
name_enter = tk.Entry(app, textvariable=name)
name_enter.pack()
tk.Label(app, text="Email:").pack()
email_enter = tk.Entry(app, textvariable=email)
email_enter.pack()
tk.Label(app, text="Address:").pack()
address_enter = tk.Entry(app, textvariable=address)
address_enter.pack()

tk.Button(app, text="Add", padx=20, pady=2, command=show).pack()
app.mainloop()