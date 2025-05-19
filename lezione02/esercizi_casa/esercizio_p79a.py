#####################################
####  PRIMA PARTE - IMPIEGATO 1 #####
#####################################

print("Inserisci quanti GIORNI ha lavorato Impiegato 1: (massimo 3 giorni)")
input1 = input()
int_input1 = int(input1)

# verifica inserimento solo numeri positivi
while True:
    if int_input1 <= 0:
        print("inserire solo un numero intero positivo")      
    else:
        break


for idx in range(1, int_input1, 1):
    print("Inserisci quante ORE ha lavorato il giorno:", idx)
    a = input()
    imp1_giorno1 = int(a)
    # verifica inserimento solo numeri positivi
    while True:
        if imp1_giorno1 <= 0:
            print("inserire solo un numero intero positivo")      
        else:
            break
    idx = idx + 0 


    if idx == 1:
        print("Inserisci quante ORE ha lavorato il giorno:", idx + 1)
        b = input()
        imp1_giorno2 = int(b)
        # verifica inserimento solo numeri positivi
        while True:
            if imp1_giorno2 <= 0:
                print("inserire solo un numero intero positivo")      
            else:
                break
        idx = idx + 1 

    
    if idx == 2:
        print("Inserisci quante ORE ha lavorato il giorno:", idx + 1)
        c = input()
        imp1_giorno3 = int(c)
        # verifica inserimento solo numeri positivi
        while True:
            if imp1_giorno3 <= 0:
                print("inserire solo un numero intero positivo")      
            else:
                break
        idx = idx + 1 

    if idx == 3:
        break

if imp1_giorno1 > 8:
    imp1_giorno1 = 8
    print("le ore di straordinario saranno ignorate")
    
if imp1_giorno2 > 8:
    imp1_giorno2 = 8
    print("le ore di straordinario saranno ignorate")

if imp1_giorno3 > 8:
    imp1_giorno3 = 8
    print("le ore di straordinario saranno ignorate")

######################################
####  SECONDA PARTE - IMPIEGATO 2 ####
######################################

print("Inserisci quanti GIORNI ha lavorato Impiegato 2: (massimo 2 giorni)")
input2 = input()
int_input2 = int(input2)

# verifica inserimento solo numeri positivi
while True:
    if int_input2 <= 0:
        print("inserire solo un numero intero positivo")      
    else:
        break


for idx in range(1, int_input2, 1):
    print("Inserisci quante ORE ha lavorato il giorno:", idx)
    d = input()
    imp2_giorno1 = int(d)
    # verifica inserimento solo numeri positivi
    while True:
        if imp2_giorno1 <= 0:
            print("inserire solo un numero intero positivo")      
        else:
            break
    idx = idx + 0 


    if idx == 1:
        print("Inserisci quante ORE ha lavorato il giorno:", idx + 1)
        e = input()
        imp2_giorno2 = int(b)
        # verifica inserimento solo numeri positivi
        while True:
            if imp2_giorno2 <= 0:
                print("inserire solo un numero intero positivo")      
            else:
                break
        idx = idx + 1 

    if idx == 2:
        break

if imp2_giorno1 > 8:
    imp2_giorno1 = 8
    print("le ore di straordinario saranno ignorate")
    
if imp2_giorno2 > 8:
    imp2_giorno2 = 8
    print("le ore di straordinario saranno ignorate")

######################################
#######  TERZA PARTE - CALCOLI #######
######################################

oreTotali_imp1 = imp1_giorno1 + imp1_giorno2 + imp1_giorno3
avg_imp1 = oreTotali_imp1 / int_input1 

oreTotali_imp2 = imp2_giorno1 + imp2_giorno2
avg_imp2 = oreTotali_imp2 / int_input2

oreTotali = oreTotali_imp1 + oreTotali_imp2

print("l'impiegato 1 ha lavorato per un totale di: ", oreTotali_imp1, "ore, con una media giornaliera di: ", avg_imp1)
print("l'impiegato 2 ha lavorato per un totale di: ", oreTotali_imp2, "ore, con una media giornaliera di: ", avg_imp2)
print("la somma delle ore lavorate da entrambi gli impiegati ammonta a ", oreTotali, "ore")

