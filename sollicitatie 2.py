import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno, showerror

win = False

def on_closing(windowTitles = 'Accounts_omac_lib'):
    if askyesno(windowTitles, f"Your program will be terminated\nShould we proceed?", icon ='warning'):
        exit()

vraag9 = 0
vraag8 = 0
vraag10 = 0
vraag11= 0
vraag12= 0

showinfo('<3',f'''+++++++++++++++++++++++++++++++
leuk dat u solliciteerd voor de
baan van Circusdirecteur voor
Circus HotelDeBotel. we hebben
een paar vraagjes voor u.
+++++++++++++++++++++++++++++++''')

def YNvraag(vraag, type = 'info'):
    if askyesno('<3', vraag, icon =type):
        return True
    else:
        return False
def aantalVraag(vraag):
    def submit():
        window.destroy()
        
    window = tkinter.Tk()
    tkinter.Label(window,text = vraag).grid(column=0, row=0, ipadx=20, ipady=10, sticky="EW")
    guessNumber = tkinter.IntVar()
    guessNumber.set(0)
    spinbox = ttk.Spinbox(window, from_=0,to=1000,textvariable=guessNumber,wrap=True, state = 'readonly')
    spinbox.grid(column=0, row=1, ipadx=20, ipady=10, sticky="EW")
    ttk.Button(window,text='Next question',command = submit).grid(column=0, row=2, ipadx=20, ipady=10, sticky="EW")
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()
    return guessNumber.get()


print(aantalVraag("wat is uw lichaamsgewicht in kg?"))

if YNvraag('wilt u een pizza bestellen?'):
    try:
        import pizzacalc
        pizzacalc()
    except:
        showerror('<3', 'error')
vraag1 = aantalVraag("hoeveel jaar heeft u praktijkervaring met dieren-dressuur?")
vraag2 = aantalVraag("hoeveel jaar heeft u praktijkervaring met jongleren?")
vraag3 = aantalVraag("hoeveel jaar heeft u praktijkervaring met acrobatiek?")
YNvraag('heeft u wel eens de enderdraak verslagen?')
YNvraag('heb je geld uitgegeven aan fortnite?')
YNvraag('wil je deze baan?')
YNvraag('bestaat sinterklaas?')
vraag4 = YNvraag("bezit u een Diploma MBO-4? J/N")
vraag5 = YNvraag("bezit u een vrachtwagen rijbewijs? J/N")
vraag6 = YNvraag("bezit u een hoge hoed? J/N")

vraag7 = YNvraag('bent u een man?')
if vraag7:
    vraag8 = YNvraag("heeft u een snor? J/N")
    if vraag8:
        vraag9 = aantalVraag("hoelang is uw snor in cm?")
vraag10 = YNvraag('bent u een vrouw?')
if vraag10:
    vraag11 = aantalVraag("hoe lang is uw haar in cm?")

vraag13 = aantalVraag("wat is uw lichaamsgewicht in kg?")
vraag14 = aantalVraag("hoe lang bent u in cm?")
if vraag13 > 90 and vraag14 > 150 and vraag4 and vraag5 and vraag6:
    if vraag7 and vraag8 and vraag9>=10:
        win = True
    elif vraag10 and vraag11>=20:
        win = True
    else:
        pass
if win:
    showinfo('<3', 'You have been accepted, yay')
else:
    showinfo('<3', 'sorry you failed')