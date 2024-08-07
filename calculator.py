import tkinter as tk

app=tk.Tk()
app.title("Calculator")
app.geometry("300x300")
def getvalue(value):
    result.insert(tk.END,value)


def equal_value():
    store=result.get()
    value=eval(store)
    result.delete(0,tk.END)
    result.insert(0,value)

def clear_value():
    result.delete(0,tk.END)


result=tk.Entry(app,width=50   ,borderwidth=10)
result.grid(row=0, column=0, columnspan=4)
one=tk.Button(app, text="1" ,padx=20, pady=2, command=lambda:getvalue("1"))
two=tk.Button(app, text="2", padx=20,pady=2,command=lambda:getvalue('2'))
three=tk.Button(app, text="3" ,padx=20, pady=2,command=lambda:getvalue('3'))
four=tk.Button(app, text="4" ,padx=20, pady=2,command=lambda:getvalue('4'))
five=tk.Button(app, text="5" ,padx=20, pady=2,command=lambda:getvalue('5'))
six=tk.Button(app, text="6" ,padx=20, pady=2,command=lambda:getvalue('6'))
seven=tk.Button(app, text="7" ,padx=20, pady=2,command=lambda:getvalue('7'))
eight=tk.Button(app, text="8" ,padx=20, pady=2,command=lambda:getvalue('8'))
nine=tk.Button(app, text="9" ,padx=20, pady=2,command=lambda:getvalue('9'))
zero=tk.Button(app, text="0" ,padx=20, pady=2,command=lambda:getvalue('0'))
mul=tk.Button(app, text="*" ,padx=20, pady=2,command=lambda:getvalue('*'))
div=tk.Button(app, text="/" ,padx=20, pady=2,command=lambda:getvalue('/'))
sum=tk.Button(app, text="+" ,padx=20, pady=2,command=lambda:getvalue('+'))
sub=tk.Button(app, text="-" ,padx=20, pady=2,command=lambda:getvalue('-'))
equal=tk.Button(app, text="=" ,padx=20, pady=2, command=lambda:equal_value())
clear=tk.Button(app, text="C" ,padx=20, pady=2, command=lambda:clear_value())
module=tk.Button(app, text="! " ,padx=20 , pady=2,command=lambda:getvalue('!'))
dot=tk.Button(app, text=".", padx=20, pady=2,command=lambda:getvalue('.'))
mul.grid(row=1, column=0)
div.grid(row=1, column=1)
clear.grid(row=1, column=2)
sum.grid(row=2, column=0)
sub.grid(row=2, column=1)
module.grid(row=2, column=2)
seven.grid(row=3, column=0)
eight.grid(row=3, column=1)
nine.grid(row=3, column=2)
four.grid(row=4, column=0)
five.grid(row=4, column=1)
six.grid(row=4, column=2)
one.grid(row=5, column=0)
two.grid(row=5, column=1)
three.grid(row=5, column=2)
zero.grid(row=6, column=0)
dot.grid(row=6, column=1)
equal.grid(row=6, column=2)
app.mainloop()