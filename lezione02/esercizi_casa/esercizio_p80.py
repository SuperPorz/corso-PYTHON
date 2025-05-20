

#INPUT INIZIALE
print("Inserisci quanti IMPIEGATI considerare: ")
input1 = input()
int_input1 = int(input1) #esempio input: 6

listaImpiegati = [] #numero degli impiegati
listaGiorni = [] #numero dei giorni
listaOre = [] #numero delle ore
listaMedie = [] #elenco delle medie giornaliere
listaSommaOrePerImpiegato = [] #elenco somma ore per impiegato



#PRIMO PUNTO: input giorni per dipendente e ore per ciascun giorno di ciascun dipendente
for idx in range(0, int_input1, 1):
    print("Inserisci quanti GIORNI ha l'impiegato ", idx + 1)
    a = input() #esempio input: 3
    imp_giorni = int(a)
    listaImpiegati.append(idx+1)
    
    for t in range(0, imp_giorni, 1):
         print("Inserisci quante ORE ha lavorato l'impiegato ", idx + 1, "nel giorno: ", t + 1)
         b = input() #esempio input: 4
         imp_ore = int(b)
         if imp_ore > 8:
            imp_ore = 8
            listaOre.append(imp_ore)
            listaGiorni.append(t + 1)
         else:
              listaOre.append(imp_ore)
              listaGiorni.append(t + 1)
    mediaGG = sum(listaOre[0:]) / imp_giorni 
    listaMedie.append(mediaGG)
    listaSommaOrePerImpiegato.append(sum(listaOre[0:]))
         

#SECONDO PUNTO: spesa totale azienda e paga oraria
for oreTotali in listaOre:
    sum(listaOre[0:])
    print(oreTotali)

pagaOraria = 14
spesaAzienda = oreTotali * pagaOraria
print("la paga oraria é: ", pagaOraria)
print("la spesa totale aziendale è: ", spesaAzienda, " €")
              
#TERZO PUNTO: printare a fine programma IMPIEGATO, media ore/giorno, ore giornaliere, ore totali, stipendio   

#dizImpiegati = dict(zip(listaGiorni, listaImpiegati))


for y in listaImpiegati:
    print("IMPIEGATO: ", listaImpiegati[y])
    #print("ore per ciascun giorno: ", listaOre[y * pagaOraria], " €")  DAVVERO TOSTA poichè devo estrarre porzioni specifiche di lista dipendenti da input utente
    print("media giornaliera: ", listaMedie[y], " ore/gg")
    print("ore totali lavorate: ", listaSommaOrePerImpiegato[y], " ore")
    p = y * pagaOraria
    print("stipendio spettante: ", listaSommaOrePerImpiegato[p], " €")
    

    y = y + 1
         



