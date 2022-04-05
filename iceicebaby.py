def snapUNiet():
    print("Sorry dat is geen optie die we aanbieden...")
def bonnetjeCheck(nummer,naam,prijs,aankopen):
    if aankopen[nummer] > 0 and nummer < 4 or nummer == 8 and aankopen[nummer]>0:
        print(naam+str(aankopen[nummer])+" x "+prijs+"   = €" + str(round(aankopen[nummer]*float(prijs),2)))
        return aankopen[nummer]*float(prijs)
    elif nummer == 5 and aankopen[nummer] > 0:
        return float(prijs)*aankopen[9]
    elif aankopen[nummer] > 0 and nummer > 3:
        return aankopen[nummer]* float(prijs)
    else:
        return 0
def inputSelectie(mode,keuze:str = "nee"):
    loop = 1
    while loop == 1:
        stringInput = input("")
        if mode == 4:
            if stringInput == "1" or stringInput== "2":
                    loop = 0
                    aantalBolletjes = int(stringInput)
            else:
                snapUNiet()
        if mode == 3:
            if stringInput.lower() == "a" or stringInput.lower()== "b"or stringInput.lower()== "c"or stringInput.lower()== "d":
                    loop = 0
            else:
                snapUNiet()
        if mode == 0:
            if stringInput.lower() == "a" or stringInput.lower()== "b":
                    loop = 0
            else:
                snapUNiet()
        if mode == 1:
            if stringInput == "69":
                print(f"\ngo to horny jail BONK\nje gaat geen 69 {keuze} krijgen vriend\n\nhoe veel {keuze} wilt u?")
            else:
                try:
                    aantalBolletjes = int(stringInput)
                    if aantalBolletjes >= 1 and aantalBolletjes <= 3 or aantalBolletjes >= 1 and keuze == "liter":
                        loop = 0
                    elif aantalBolletjes >= 4 and aantalBolletjes <=8:
                        print(f"Dan krijgt u van mij {aantalBolletjes} {keuze}")
                        loop = 0
                    elif aantalBolletjes > 8:
                        print("Sorry, zulke grote bakjes hebben we niet")
                    else:
                        snapUNiet()
                except:
                    snapUNiet()
        if mode == 2:
            if stringInput.lower() == "y":
                again = 1
                loop = 0
            elif stringInput.lower() == "n":
                again = 0
                loop = 0
                print("Bedankt en tot ziens!")
            else:
                snapUNiet()
    if mode == 0 or mode == 3:
        return stringInput.lower()
    elif mode == 1 or mode == 4:
        return aantalBolletjes  
    elif mode == 2:
        return again 
def smaakjes(aantalBolletjes,keuze):
    if aantalBolletjes[8] ==0:
        bolletjesOfLiter = 3
    else:
        bolletjesOfLiter = 8
    for x in range( 1, aantalBolletjes[bolletjesOfLiter]+1):
        loop = 1
        while loop == 1:
            print(f"Welke smaak wilt u voor {keuze} nummer {x}? A) Aardbei, C) Chocolade of V) Vanille?")
            smaakKeuze = input().lower()
            if smaakKeuze != "a" and smaakKeuze != "c" and smaakKeuze != "m" and smaakKeuze != "v":
                snapUNiet()
            else:
                loop = 0
def toppingsKeuzeNaarNummer(toppingsKeuze,bakjeOfHoorntje, aankopen):
    if toppingsKeuze == "b":
        aankopen[10] = 4
        return aankopen
    elif toppingsKeuze == "c":
        aankopen[9] += aankopen[3]
        aankopen[10] = 5
        return aankopen
    elif toppingsKeuze == "d":
        if bakjeOfHoorntje == "a":
            aankopen[10] = 6
            return aankopen
        elif bakjeOfHoorntje == "b":
            aankopen[10] = 7
            return aankopen
    else:
        aankopen[10] = 0 
        return aankopen         
def bonnetjeCreatie(aankopen):
    toppings = 0
    kosten = 0
    print('--------["Papi Gelato"]--------\n')
    kosten += bonnetjeCheck(0, "Bolletjes       ", "0.95", aankopen)
    kosten += bonnetjeCheck(8, "Liter           ", "9.80", aankopen)
    kosten += bonnetjeCheck(1, "Horrentje       ", "1.25", aankopen)
    kosten += bonnetjeCheck(2, "Bakje           ", "0.75", aankopen)
    toppings += bonnetjeCheck(4, "Slagroom        ", "0.50", aankopen)
    toppings += bonnetjeCheck(5, "Sprinkles       ", "0.30", aankopen)
    toppings += bonnetjeCheck(6, "Caramel Saus    ", "0.60", aankopen)
    toppings += bonnetjeCheck(7, "Caramel Saus    ", "0.90", aankopen)
    kosten += toppings
    if toppings != 0:
        print("Toppings                   = €"+str(round(toppings,2)))
    print("                           -------+\nTotaal                     = €"+str(round(kosten, 2)))
    if aankopen[8] > 0:
        print("BTW (6%)                   = €" + str(round(kosten/106*6,2)))
aankopen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
again = 1   
print("Welkom bij Papi Gelato")
print("Bent u 1) particulier of 2) zakelijk?")
particulierOfZakelijk = inputSelectie(4)
while again == 1:
    if particulierOfZakelijk == 1:
        print("hoe veel bolletjes wilt u?")
        aankopen[3] = inputSelectie(1,"bolletjes")
        aankopen[0] += aankopen[3]
        smaakjes(aankopen,"bolletjes")
        if aankopen[3] < 4:
            print(f"Wilt u deze {aankopen[3]} bolletje(s) in A) een hoorntje of B) een bakje?")
            bakjeOfHoorntje = inputSelectie(0)
            if bakjeOfHoorntje == "a":
                aankopen[1] += 1
                bestelling = "hoorntje"
            elif bakjeOfHoorntje == "b":
                aankopen[2] += 1
                bestelling = "bakje"
        else:
            bakjeOfHoorntje = 'b'
            aankopen[2] += 1
            bestelling = "bakje"
        print("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?")
        toppingKeuze = inputSelectie(3)
        aankopen = toppingsKeuzeNaarNummer(toppingKeuze,bakjeOfHoorntje,aankopen)
        if aankopen[10] != 0:
            aankopen[aankopen[10]] +=1
        print(f"Hier is uw {bestelling} met {aankopen[3]} bolletje(s). Wilt u nog meer bestellen? (Y/N)")
        again = inputSelectie(2)
    else:
        again = 0
        print("hoe veel liter wilt u?")
        aankopen[8] = inputSelectie(1,"liter")
        smaakjes(aankopen,"liter")
bonnetjeCreatie(aankopen)