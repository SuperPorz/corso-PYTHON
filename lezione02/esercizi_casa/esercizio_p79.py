#####################################
####  PRIMA PARTE - IMPIEGATO 1 #####
#####################################

#input iniziale-3
print("Inserisci quanti GIORNI ha lavorato Impiegato 1: (massimo 3 giorni)")
input1 = input()
int_input1 = int(input1)

# verifico che il numero giorni stia in un range accettabile:
while True:
    if int_input1 <= 0 or int_input1 >= 4:
        print("inserire un numero di giorni compreso tra 1 e 3")
        input1 = input()
        int_input1 = int(input1)
        continue      
    else:
        break

# ciclo for per archiviare le ore lavorate nei diversi giorni:
for idx in range(0, int_input1, 1):
    print("Inserisci quante ORE ha lavorato il giorno:", idx + 1)
    print("(le ore di straordinario saranno ignorate)")
    a = input()
    imp1_giorno1 = int(a)
    if int_input1 == 1:
            imp1_giorno2 = 0
            imp1_giorno3 = 0
            break 
    elif int_input1 >= 2:
        idx = idx + 1


    if idx == 1:
        print("Inserisci quante ORE ha lavorato il giorno:", idx + 1)
        print("(le ore di straordinario saranno ignorate)")
        b = input()
        imp1_giorno2 = int(b)
        if int_input1 == 2:
            imp1_giorno3 = 0
            break 
        elif int_input1 == 3:
            idx = idx + 1 

    
    if idx == 2:
        print("Inserisci quante ORE ha lavorato il giorno:", idx + 1)
        print("(le ore di straordinario saranno ignorate)")
        c = input()
        imp1_giorno3 = int(c)
        break

# ignoro le ore di straordinario per ciascun giorno:
if imp1_giorno1 > 8:
    imp1_giorno1 = 8
    
if imp1_giorno2 > 8:
    imp1_giorno2 = 8

if imp1_giorno3 > 8:
    imp1_giorno3 = 8

######################################
####  SECONDA PARTE - IMPIEGATO 2 ####
######################################

#input iniziale
print("Inserisci quanti GIORNI ha lavorato Impiegato 2: (massimo 2 giorni)")
input2 = input()
int_input2 = int(input2)

# verifico che il numero giorni stia in un range accettabile:
while True:
    if int_input2 <= 0 or int_input2 >= 3:
        input2 = input()
        int_input2 = int(input2)
        print("inserire un numero di giorni pari a 1 oppure 2") 
        continue    
    else:
        break

# ciclo for per archiviare le ore lavorate nei diversi giorni:
for idx in range(0, int_input2, 1):
    print("Inserisci quante ORE ha lavorato il giorno:", idx + 1)
    print("(le ore di straordinario saranno ignorate)")
    a = input()
    imp2_giorno1 = int(a)
    if int_input2 == 1:
            imp2_giorno2 = 0
            break 
    elif int_input2 == 2:
        idx = idx + 1

    if idx == 1:
        print("Inserisci quante ORE ha lavorato il giorno:", idx + 1)
        print("(le ore di straordinario saranno ignorate)")
        b = input()
        imp1_giorno2 = int(b)
        idx = idx + 1
        break

# ignoro le ore di straordinario per ciascun giorno:
if imp2_giorno1 > 8:
    imp2_giorno1 = 8
    
if imp2_giorno2 > 8:
    imp2_giorno2 = 8

######################################
#######  TERZA PARTE - CALCOLI #######
######################################

#calcoli impiegato 1
oreTotali_imp1 = imp1_giorno1 + imp1_giorno2 + imp1_giorno3
avg_imp1 = oreTotali_imp1 / int_input1 

#calcoli impiegato 2
oreTotali_imp2 = imp2_giorno1 + imp2_giorno2
avg_imp2 = oreTotali_imp2 / int_input2

#calcoli totali
oreTotali = oreTotali_imp1 + oreTotali_imp2


print("l'impiegato 1 ha lavorato per un totale di: ", oreTotali_imp1, "ore, con una media giornaliera di: ", avg_imp1)
print("l'impiegato 2 ha lavorato per un totale di: ", oreTotali_imp2, "ore, con una media giornaliera di: ", avg_imp2)
print("la somma delle ore lavorate da entrambi gli impiegati ammonta a ", oreTotali, "ore")

