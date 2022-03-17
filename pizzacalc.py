import tkinter
from tkinter import ttk
import accounts_omac
import random
from tkinter.messagebox import showinfo

appIDorName = 'pizzacalcTKINTERidkWHY'

effects = ['aa','ab','ac','ad','ae']

configSettings = accounts_omac.configFileConsole()
data = accounts_omac.defaultConfigurations.defaultLoadingTkinter(configSettings)
if data == False:
    exit()
data = accounts_omac.saveAccount(data, configSettings)

dictionaryCollectables = {'item':{'01': {'name':'small pizza', 'description': 'It\'s a sweat small pizza baked with love'},
                                    '02': {'name':'medium pizza', 'description': 'It\'s a sweat medium pizza baked with love'},
                                    '03': {'name':'large pizza', 'description': 'It\'s a sweat large pizza baked with love'},
                                    '11': {'name':'cold small pizza', 'description': 'u let it get cold, poor small pizza gone to waste'},
                                    '12': {'name':'cold medium pizza', 'description': 'The bigger the pizza, the bigger the waste'},
                                    '13': {'name':'cold large pizza', 'description': 'you wasted a lot of ingredients by letting this large pizza get cold'}},
                        'effects': {'aa': {'name': 'slightly burnt', 'description': 'almost perfect, slightly burnt. next time take it out 10 seconds earlier'},
                                    'ab': {'name': 'perfectly baked', 'description': 'this is the result you want to achieve, a pefect piece of food'},
                                    'ac': {'name': 'crispy', 'description': 'not everyones favorite, but still amazingly made'},
                                    'ad': {'name': 'fully burnt', 'description': 'did you leave it in the furnace for 1 hour too long or something? it\'s completely black'},
                                    'ae': {'name': 'raw', 'description': 'you didn\'t put it in the furnace'}}}

if appIDorName in data['collectables']:
    data['collectables'][appIDorName][1] = dictionaryCollectables
else:
    data['collectables'][appIDorName] = [[], dictionaryCollectables]

window = tkinter.Tk()

def addNumber(*args):
    global numbers
    if small_value.get() == numbers[len(numbers)-1] or medium_value.get() == numbers[len(numbers)-1] or large_value.get() == numbers[len(numbers)-1]:
        numbers.append(len(numbers)-1)
        small_box.config(value = numbers)
        medium_box.config(value = numbers)
        large_box.config(value = numbers)
    
        
def buttonPress(*args):
    global data
    for i in range(len(data['collectables'][appIDorName][0])):
        if data['collectables'][appIDorName][0][i]['item'] == '01':
            data['collectables'][appIDorName][0][i]['item'] = '11'
        elif data['collectables'][appIDorName][0][i]['item'] == '02':
            data['collectables'][appIDorName][0][i]['item'] = '12'
        elif data['collectables'][appIDorName][0][i]['item'] == '03':
            data['collectables'][appIDorName][0][i]['item'] = '13'
    for x in range(int(small_value.get())):
        data['collectables'][appIDorName][0].append({'item': '01', 'effects': f'{effects[random.randint(0,len(effects)-1)]}'})
    for x in range(int(medium_value.get())):
        data['collectables'][appIDorName][0].append({'item': '02', 'effects': f'{effects[random.randint(0,len(effects)-1)]}'})
    for x in range(int(large_value.get())):
        data['collectables'][appIDorName][0].append({'item': '03', 'effects': f'{effects[random.randint(0,len(effects)-1)]}'})
    window.destroy()
    
    receipt = {'total': 0, 'small' : int(small_value.get()), 'medium' : int(medium_value.get()), 'large' : int(large_value.get())}
    receipt['total'] = receipt['small'] + receipt['medium'] + receipt['large']
    popup = f"| Uw bestelling:\n| {receipt['small']} small: €{receipt['small'] * costs['small']}\n| {receipt['medium']} medium: €{receipt['medium'] * costs['medium']}\n| {receipt['large']} large: €{receipt['large'] * costs['large']}\n|\n| Totaalprijs = €{receipt['large'] * costs['large']+receipt['medium'] * costs['medium'] +receipt['small'] * costs['small']}"
    tkinter.messagebox.showinfo(title=appIDorName,message =popup)

costs = {'small' : 3.99, 'medium' : 5.00, 'large' : 6.00}
small = 3.99
medium = 5.00
large = 6.00
numbers = [0,1]

costsLabel = tkinter.Label(window, text =f"""Prijzen in euro's
small = {costs['small']}
medium = {costs['medium']}
large = {costs['large']}""")
costsLabel.grid(column=0, row=0, ipadx=20, ipady=10, sticky="EW",columnspan = 2)

smallLabel = tkinter.Label(window, text='small pizza\'s:').grid(column=0, row=1, ipadx=20, ipady=10, sticky="EW")
small_value = tkinter.IntVar()
small_value.trace('w',addNumber)
small_box = ttk.Spinbox(window, value = numbers, textvariable=small_value,wrap=True, state = 'readonly')
small_box.grid(column=1, row=1, ipadx=20, ipady=10, sticky="EW")

mediumLabel = tkinter.Label(window, text='medium pizza\'s:').grid(column=0, row=2, ipadx=20, ipady=10, sticky="EW")
medium_value = tkinter.IntVar()
medium_value.trace('w',addNumber)
medium_box = ttk.Spinbox(window, value = numbers, textvariable=medium_value,wrap=True, state = 'readonly')
medium_box.grid(column=1, row=2, ipadx=20, ipady=10, sticky="EW")

largeLabel = tkinter.Label(window, text='large pizza\'s:').grid(column=0, row=3, ipadx=20, ipady=10, sticky="EW")
large_value = tkinter.IntVar()
large_value.trace('w',addNumber)
large_box = ttk.Spinbox(window, value = numbers, textvariable=large_value,wrap=True, state = 'readonly')
large_box.grid(column=1, row=3, ipadx=20, ipady=10, sticky="EW")

button = ttk.Button(window, text = 'order pizzas', command=buttonPress)
button.grid(column=0, row=4, ipadx=20, ipady=10, sticky="EW",columnspan = 2)



window.mainloop()
















data = accounts_omac.saveAccount(data, configSettings)