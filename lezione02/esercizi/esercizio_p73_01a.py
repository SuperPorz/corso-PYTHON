##### ESERCIZIO 1, pag. 73 SLIDES PYTHON-1: "NUMERO PREFERITO" versione più cazzuta (però non c'è controllo sui numeri)

print("inserisci 4 numeri separati da spazio, poi alla sinistra di quello preferito agiungere una p")

#prima parte: riceviamo input, splittiamo gli elementi, creiamo 2 variabili con lista vuota (1 per item scelto, e una per gli altri items)
stringaNumeri = input()
listaNumeri = stringaNumeri.split()
bloccoScelto = []
altriNumeri = []

#seconda parte: ciclo WHILE (controllo input) + ciclo FOR sulla lista splittata
check = True    
while check == True:    
    for x in listaNumeri:
        if "p" in x:
            bloccoScelto.append(x)  # buttiamo l'elemento che contiene "p" dentro la lista BLOCCO SCELTO
            break

    for y in listaNumeri:
        if not "p" in y:
            altriNumeri.append(y)   # buttiamo gli elementi che non contengono "p" dentro la lista ALTRI NUMERI
            continue

    z = ''.join(altriNumeri).replace("p", '')     # controlliamo che gli altri elementi siano tutti numeri; se TRUE si esce dal ciclo WHILE
    if z.isdigit() == True:
        check = False
    else:
        print('inserisci solo numeri, assassino!!')

#terza parte: JOIN su blocco scelto converto lista>stringa; REPLACE tolgo 'p' e sostituisco con NON-carattere; butto tutto dentro variab. NUMERO SCELTO e printo
numeroScelto2 = ''.join(bloccoScelto).replace("p", '')
print("ABRACADABRA!! il tuo numero preferito é: ", numeroScelto2)
