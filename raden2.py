import random
import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno

points = 0

#to not get those nasty index out of range errors, you try to get item 20 out of 19 items, this will return you item 0
def noIndexError(number, maxNumber, minNumber = 0):
    '''to not get those nasty index out of range errors, you try to get item 20 out of 19 items, this will return you item 0'''
    while number > maxNumber or number < minNumber:
        if number > maxNumber:
            number -= (maxNumber- minNumber)+1
        elif number < minNumber:
            number += (maxNumber - minNumber) + 1
    return number

def positive(num):
    if num < 0:
        num *= -1
    return num

def info(message, number):
    if number > 0:
        showinfo('<3',f'{message}, You need to go Higher')
    else:
        showinfo('<3',f'{message}, You need to go Lower')


def game():
    global guesses
    def guess():
        global points
        global guesses
        guesses += 1
        label.configure(text=f'Guessed {guesses}/10')
        difference = number - guessNumber.get()
        if difference == 0:
            showinfo('<3','You have won!')
            points += 1
            window.destroy()
        elif guesses == 10:
            showinfo('<3','You failed, oops')
            window.destroy()
        elif positive(difference) <= 20:
            info('You are close', difference)
        elif positive(difference) <= 50:
            info('You are warm', difference)
        else:
            info('Not even close', difference)

    guesses = 0
    number = random.randint(1,999)
    print(number)
    window = tkinter.Tk()
    button = ttk.Button(window,command=guess,text='Guess')
    button.grid(column=0, row=3, ipadx=20, ipady=10, sticky="EW",columnspan=2)
    label = tkinter.Label(window,text='Guessed 0/10')
    label.grid(column=0, row=0, ipadx=20, ipady=10, sticky="EW",columnspan=2)
    guessNumber = tkinter.IntVar()
    guessNumber.set(10)
    spinbox = ttk.Spinbox(window, from_=0,to=1000,textvariable=guessNumber,wrap=True, state = 'readonly')
    spinbox.grid(column=1, row=1, ipadx=20, ipady=10, sticky="EW")
    tkinter.Label(window,text='Guess:').grid(column=0, row=1, ipadx=20, ipady=10, sticky="EW")
    ttk.Button(window,command=lambda:guessNumber.set(noIndexError(guessNumber.get()+100,1000)),text='+100').grid(column=0, row=2, ipadx=20, ipady=10, sticky="EW")
    ttk.Button(window,command=lambda:guessNumber.set(noIndexError(guessNumber.get()-100,1000)),text='-100').grid(column=1, row=2, ipadx=20, ipady=10, sticky="EW")




    window.mainloop()

game()
while True:
    if askyesno('<3', f"Do you want to play again?\nScore: {points}", icon ='warning'):
        game()
    else:
        exit()