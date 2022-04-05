import json
import os
import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno
import accounts_omac

if os.path.isfile(f"papi.json"):
    with open(f"papi.json") as json_file_cardsCreation:
        dataString_cardsCreation = json.load(json_file_cardsCreation)
        #this makes it so if u use a json beautifier that makes it not being a string anymore, it would still work
        if type(dataString_cardsCreation) == dict:
            configData = dataString_cardsCreation
        else:
            configData = json.loads(dataString_cardsCreation)
    
    ######################## Basic JSON Creation ########################

else:
    configData = {'smaken':['Aardbei', 'Chocolade', 'Vanille', 'Banaan', 'Kaas'],
                            'extraTypes':{'Kaas': ['Oude kaas', 'Jonge kaas']}}

    json_string_configDat = json.dumps(configData)
    with open(f"papi.json", 'w') as outfile:
        json.dump(json_string_configDat, outfile)


smaken = configData['smaken']
order = 0
orders = {}
extraTypes = configData['extraTypes']

#to not get those nasty index out of range errors, you try to get item 20 out of 19 items, this will return you item 0
def noIndexError(number, maxNumber, minNumber = 0):
    '''to not get those nasty index out of range errors, you try to get item 20 out of 19 items, this will return you item 0'''
    while number > maxNumber or number < minNumber:
        if number > maxNumber:
            number -= (maxNumber- minNumber)+1
        elif number < minNumber:
            number += (maxNumber - minNumber) + 1
    return number

def on_closing(windowTitles = 'Accounts_omac_lib'):
    if askyesno(windowTitles, f"Your program will be terminated\nShould we proceed?", icon ='warning'):
        exit()

def YNvraag(vraag, type = 'info'):
    if askyesno('<3', vraag, icon =type):
        return True

def selectOption(vraag,optionList):
    window = tkinter.Tk()
    def submit():
        window.destroy()

    selected = tkinter.StringVar()
    maximum = 4
    for x in range(len(optionList)):
        exec(f'radiobutton_{accounts_omac.removeCharacters(optionList[x])} = ttk.Radiobutton(window, text="{optionList[x]}", value="{optionList[x]}", variable=selected)')
        devided = (x // maximum)
        exec(f'radiobutton_{accounts_omac.removeCharacters(optionList[x])}.grid(column={x - (((x) // maximum)*maximum)}, row={(x // maximum)+1}, ipadx=20, ipady=10, sticky="EW")')
    tkinter.Label(window,text = vraag).grid(column=0, row=0, ipadx=20, ipady=10, sticky="EW", columnspan=4)
    ttk.Button(window,text='Next',command = submit).grid(column=0, row=devided + 2, ipadx=20, ipady=10, sticky="EW", columnspan=4)
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()
    return selected.get()

def aantalVraag(vraag,max = 1000,min = 1):
    def submit():
        window.destroy()  
    window = tkinter.Tk()
    tkinter.Label(window,text = vraag).grid(column=0, row=0, ipadx=20, ipady=10, sticky="EW")
    guessNumber = tkinter.IntVar()
    guessNumber.set(noIndexError(0,max,min))
    spinbox = ttk.Spinbox(window, from_=min,to=max,textvariable=guessNumber,wrap=True, state = 'readonly')
    spinbox.grid(column=0, row=1, ipadx=20, ipady=10, sticky="EW")
    ttk.Button(window,text='Next',command = submit).grid(column=0, row=2, ipadx=20, ipady=10, sticky="EW")
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()
    return guessNumber.get()

zakelijk = YNvraag(f"is dit een zakelijke bestelling?")

while True:
    if zakelijk:
        pass
    else:
        aantalBolletjes = aantalVraag('Hoeveel bolletjes witl u?',8,1)
        orders[f'order {order}'] = {'aantalBolletjes':aantalBolletjes}
        for x in range(aantalBolletjes):
            temp = selectOption(f'voor bolletje {x + 1}, welke smaak wil je?', smaken)
            while temp in extraTypes:
                temp = selectOption(f'voor bolletje {x + 1}, welk type {temp} wil je?', extraTypes[temp])
            orders[f'order {order}'][f'bolletje {x}'] = temp
        print(orders)
        order += 1