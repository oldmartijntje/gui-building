import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tkinter.Tk()
messagesTitle = 'BEANS'

def colorChange(*args):
    if color_var.get() == 'Yes':
        moulds_var.set('')
        moulds1.configure(state='disabled')
        moulds2.configure(state='disabled')
        holes1.configure(state='normal')
        holes2.configure(state='normal')
    elif color_var.get() == 'No':
        holes_var.set('')
        moulds1.configure(state='normal')
        moulds2.configure(state='normal')
        holes1.configure(state='disabled')
        holes2.configure(state='disabled')
    else:
        moulds_var.set('')
        holes_var.set('')
        holes1.configure(state='disabled')
        holes2.configure(state='disabled')
        moulds1.configure(state='disabled')
        moulds2.configure(state='disabled')

def holesChange(*args):
    if holes_var.get() == 'Yes':
        stone_var.set('')
        stone1.configure(state='disabled')
        stone2.configure(state='disabled')
        expensive1.configure(state='normal')
        expensive2.configure(state='normal')
    elif holes_var.get() == 'No':
        stone1.configure(state='normal')
        stone2.configure(state='normal')
        expensive_var.set('')
        expensive1.configure(state='disabled')
        expensive2.configure(state='disabled')
    else:
        expensive_var.set('')
        expensive1.configure(state='disabled')
        expensive2.configure(state='disabled')
        stone_var.set('')
        stone1.configure(state='disabled')
        stone2.configure(state='disabled')

def mouldsChange(*args):
    if moulds_var.get() == '':
        crust_var.set('')
        crust1.configure(state='disabled')
        crust2.configure(state='disabled')
    else:
        crust_var.set('')
        crust1.configure(state='normal')
        crust2.configure(state='normal')

def allowButton(*args):
    if expensive_var.get() == '' and stone_var.get() == '' and crust_var.get() == '':
        button.configure(state='disabled')
    else:
        button.configure(state='normal')

def resultsButtonClick(*args):
    if color_var.get() == 'Yes':
        if holes_var.get() == 'Yes':
            if expensive_var.get() == 'Yes':
                tkinter.messagebox.showinfo(title=messagesTitle,message ='emmenthaler')
            else:
                tkinter.messagebox.showinfo(title=messagesTitle,message ='leerdammer')
        else:
            if stone_var.get() == 'Yes':
                tkinter.messagebox.showinfo(title=messagesTitle,message ='pemnigiano reggiano')

            else:
                tkinter.messagebox.showinfo(title=messagesTitle,message ='goudse kaas')
    else:
        if moulds_var.get() == "Yes":
            if crust_var.get() == 'Yes':
                tkinter.messagebox.showinfo(title=messagesTitle,message ='bleu de rochbaron')
            else:
                tkinter.messagebox.showinfo(title=messagesTitle,message ='faume d\'ambert')
        else:
            if crust_var.get() == 'Yes':
                tkinter.messagebox.showinfo(title=messagesTitle,message ='camembert')
            else:
                tkinter.messagebox.showinfo(title=messagesTitle,message ='mozzarella')

colorLabel = ttk.Label(window, text='Is the color Yellow?').grid(column=0, row=0, ipadx=20, ipady=10, sticky="EW")
color_var = tkinter.StringVar()
color1 = ttk.Radiobutton(window, text='Yes', value='Yes', variable=color_var).grid(column=1, row=0, ipadx=20, ipady=10, sticky="EW")
color2 = ttk.Radiobutton(window, text='No', value='No', variable=color_var).grid(column=2, row=0, ipadx=20, ipady=10, sticky="EW")
color_var.trace('w',colorChange)

holesLabel = ttk.Label(window, text='does it have holes?').grid(column=0, row=2, ipadx=20, ipady=10, sticky="EW")
holes_var = tkinter.StringVar()
holes1 = ttk.Radiobutton(window, text='Yes', value='Yes', variable=holes_var,state='disabled')
holes1.grid(column=1, row=2, ipadx=20, ipady=10, sticky="EW")
holes2 = ttk.Radiobutton(window, text='No', value='No', variable=holes_var,state='disabled')
holes2.grid(column=2, row=2, ipadx=20, ipady=10, sticky="EW")
holes_var.trace('w',holesChange)

expensiveLabel = ttk.Label(window, text='is it way too expensive?').grid(column=0, row=3, ipadx=20, ipady=10, sticky="EW")
expensive_var = tkinter.StringVar()
expensive1 = ttk.Radiobutton(window, text='Yes', value='Yes', variable=expensive_var,state='disabled')
expensive1.grid(column=1, row=3, ipadx=20, ipady=10, sticky="EW")
expensive2 = ttk.Radiobutton(window, text='No', value='No', variable=expensive_var,state='disabled')
expensive2.grid(column=2, row=3, ipadx=20, ipady=10, sticky="EW")
expensive_var.trace('w',allowButton)

stoneLabel = ttk.Label(window, text='is it as hard as stone?').grid(column=0, row=4, ipadx=20, ipady=10, sticky="EW")
stone_var = tkinter.StringVar()
stone1 = ttk.Radiobutton(window, text='Yes', value='Yes', variable=stone_var,state='disabled')
stone1.grid(column=1, row=4, ipadx=20, ipady=10, sticky="EW")
stone2 = ttk.Radiobutton(window, text='No', value='No', variable=stone_var,state='disabled')
stone2.grid(column=2, row=4, ipadx=20, ipady=10, sticky="EW")
stone_var.trace('w',allowButton)

mouldsLabel = ttk.Label(window, text='does the cheese have blue moulds?').grid(column=0, row=1, ipadx=20, ipady=10, sticky="EW")
moulds_var = tkinter.StringVar()
moulds1 = ttk.Radiobutton(window, text='Yes', value='Yes', variable=moulds_var,state='disabled')
moulds1.grid(column=1, row=1, ipadx=20, ipady=10, sticky="EW")
moulds2 = ttk.Radiobutton(window, text='No', value='No', variable=moulds_var,state='disabled')
moulds2.grid(column=2, row=1, ipadx=20, ipady=10, sticky="EW")
moulds_var.trace('w',mouldsChange)

crustLabel = ttk.Label(window, text='does it have a crust?').grid(column=0, row=5, ipadx=20, ipady=10, sticky="EW")
crust_var = tkinter.StringVar()
crust1 = ttk.Radiobutton(window, text='Yes', value='Yes', variable=crust_var,state='disabled')
crust1.grid(column=1, row=5, ipadx=20, ipady=10, sticky="EW")
crust2 = ttk.Radiobutton(window, text='No', value='No', variable=crust_var,state='disabled')
crust2.grid(column=2, row=5, ipadx=20, ipady=10, sticky="EW")
crust_var.trace('w',allowButton)

button = ttk.Button(window, text='Give The Name Of Da Cheese',state='disabled', command=resultsButtonClick)
button.grid(column=0, row=6, ipadx=10, ipady=5, sticky="EW",columnspan=3)

window.mainloop()
