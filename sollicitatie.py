import webbrowser
compilations = ['https://www.youtube.com/watch?v=E1dKbVnNE1Q','https://www.youtube.com/watch?v=nW948Va-l10', 'https://www.youtube.com/watch?v=2OiCiL0OpXk', 'https://www.youtube.com/watch?v=DQNDOxsTkGE', 'https://www.youtube.com/watch?v=8Ed_tfGwnh4', 'https://www.youtube.com/watch?v=XGygoMOI6iQ', 'https://www.youtube.com/watch?v=ALUCl2p4aFc']
vraag9 = 0
vraag8 = 0
vraag10 = 0
vraag11= 0
vraag12= 0
manOfVrouw = 'a'
print("+++++++++++++++++++++++++++++++")
print("leuk dat u solliciteerd voor de")
print("baan van Circusdirecteur voor")
print("Circus HotelDeBotel. we hebben")
print("een paar vraagjes voor u.")
print("+++++++++++++++++++++++++++++++")
pizza = input("wilt u een pizza bestellen? J/N")
if pizza.lower() == "j":
    import pizzacalc
    pizzacalc()
enderdragon = input("heeft u wel eens de enderdraak verslagen?J/N")
if enderdragon.lower() != 'j' and enderdragon.lower() != 'n':
    raise NameError('ik denk dat hij stiekem dream is, anders zou hij wel antwoorden')
try:
    vbuck = float(input("hoeveel euro heb je uitgegeven aan Fortnite?"))
except:
    print('ben je zo down? dat is geen nummer dipshit')
else:
    if vbuck < 24:
        raise ValueError('Je liegt! ik weet het zeker')
try:
    vraag1 = int(input("hoeveel jaar heeft u praktijkervaring met dieren-dressuur?"))
except:
    vraag1 = 0
try: vraag2 = int(input("hoeveel jaar heeft u praktijkervaring met jongleren?"))
except: vraag2 = 0
willen = input("wilt u deze baan?J/N")
if willen.lower() != 'j' and willen.lower() != 'n':
    raise NameError('Hij vermijdt de vraag, misschien is het een russische spion!')
try:
    vraag3 = int(input("hoeveel jaar heeft u praktijkervaring met acrobatiek?"))
except:
    vraag3 = 0
sinterklaas = input("bestaat sinterklaas?J/N")
if sinterklaas.lower() == 'n':
    raise NameError('weet u het zeker? \n mama zij van wel\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nsnif snif')
loki = input("simp je voor loki?J/N")
if loki.lower() == 'n':
    for x in range(len(compilations)):
        webbrowser.open_new_tab(compilations[x])
    raise NameError('I will make u simp!')
vraag4 = input("bezit u een Diploma MBO-4? J/N")
vraag5 = input("bezit u een vrachtwagen rijbewijs? J/N")
vraag6 = input("bezit u een hoge hoed? J/N")
input("hoeveel mensen heeft u vermoord?")
vraag7 = input("wat bent u als geboren? man of vrouw? M/V")
if vraag7 == "m" or vraag7 == "M":
    manOfVrouw = 'man'
    vraag8 = input("heeft u een snor? J/N")
    if vraag8 == "j" or vraag8 =="J":
        try: vraag9 = int(input("hoelang is uw snor in cm?"))
        except: vraag9 = 0
    input("heeft u een hernia?J/N")
elif vraag7 == "v" or vraag7 == "V":
    manOfVrouw = 'woman'
    vraag10 = input("wat is uw haarkleur? (r=rood,b=blond,z=zwart)")
    vraag11 = input("wat voor haarstijl heeft u? krul=k,staartjes=s,kaal=a")
    try: vraag12 = int(input("hoe lang is uw haar in cm?"))
    except: vraag12 = 0
else: 
    raise NameError('it is not a man or a women, it might be an attack helicopter!!')
try:kiddos = int(input("hoeveel kinderen heeft u in uw kelder?"))
except: raise ValueError('het is geen nummer aan kinderen, misschien spreekt hij chinees')
if kiddos == 69:
    raise ValueError(f'its a {manOfVrouw} with goals, be carefull')
elif kiddos == 0:
    raise ValueError(f'i don\'t believe this {manOfVrouw}')

try: vraag13=int(input("wat is uw lichaamsgewicht in kg?"))
except: vraag13 = 0
try: vraag14=int(input("hoe lang bent u in cm?"))
except: vraag14 = 0

if vraag7 == "m" or vraag7 == "M":
    if (vraag1 > 4 or vraag2 > 5 or vraag3 > 3) and (vraag4 == "J" or vraag4 == "j") and (vraag5 == "J" or vraag5 == "j") and (vraag6 == "J" or vraag6 == "j") and (vraag8 == "J" or vraag8 == "j") and vraag9 > 10 and vraag13 > 90 and vraag14 > 150:
        print("Gefeliciteerd, u bent een goede kanidaat. stuur nu uw cv maar door")
    else:
        print("Nope, u bent niet in aanmerking gekomen voor deze beropespositie.")
elif vraag7 == "v" or vraag7 == "V":
    if (vraag1 > 4 or vraag2 > 5 or vraag3 > 3) and (vraag4 == "J" or vraag4 == "j") and (vraag5 == "J" or vraag5 == "j") and (vraag6 == "J" or vraag6 == "j") and vraag13 > 90 and vraag14 > 150 and (vraag10 == "r" or vraag10=="R") and (vraag11 == "k" or vraag11=="K") and vraag12 >20:
        print("Gefeliciteerd, u bent een goede kanidaat. stuur nu uw cv maar door")
    else:
        print("Nope, u bent niet in aanmerking gekomen voor deze beropespositie.")




