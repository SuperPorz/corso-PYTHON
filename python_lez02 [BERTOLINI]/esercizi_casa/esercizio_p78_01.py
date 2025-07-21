# Scrivere un programma che chieda in input 2 numeri interi separati da spazi e
# che controlli l'eventuale inserimento di quantità non numeriche.

while True:
    print("Inserisci due numeri interi separati da uno spazio.")
    stringa_fornita : str = input()

    # puliamo la stringa da eventuali spazi all'inizio e alla fine dell'input, con la funzione "strip" che li elimina automaticamente:
    nuova_stringa = stringa_fornita.strip(' ')           

    # verifichiamo che ci sia almeno uno spazio nella stringa input, come richiesto dall'esercizio: (se uguale a -1 esce true, allora printa mess. di errore)
    if nuova_stringa.find(' ') == -1:                    
        print("Mi hai inserito una sola quantità.")
        continue

    # ora sono sicuro che ci sia uno spazio. proseguo splittando le due stringhe usando come separatore l'unico spazio ammesso:
    stringhe_separate = nuova_stringa.split(' ')
    
    # ora, se lunghezza tringa è diversa da 2 (quindi input sbagliato rispetto esercizio), printiamo un messaggio di errore. altrimenti, si avanza con "continue":
    if len(stringhe_separate) != 2:
        print("Non hai rispettato le condizioni dell'input! Inserire un numero seguito da un solo spazio e poi un altro numero, infine premere invio")
        continue

    # verifichiamo che le due stringhe siano numeri e non lettere/caratteri speciali o altro:
    if not (stringhe_separate[0].isdigit() and stringhe_separate[1].isdigit()):
        print("Non hai rispettato le condizioni dell'input! Inserire un numero seguito da un solo spazio e poi un altro numero, infine premere invio")
        continue

    # ho due stringhe che contengono quantità numeriche.
    numero1 = int(stringhe_separate[0])
    numero2 = int(stringhe_separate[1])

    # verifichiamo che i due numeri inseriti non siano identici, dato che l'esercizio vuole determinare quale dei due sia il minore e quale il maggiore:
    if numero1 == numero2:
        print("Hai inserito due quantità uguali! Inserisci due numeri diversi")
        continue
    # ora la parte finale, ovvero il confronto dei due numeri e il print del risultato:
    if numero1 > numero2:
        print("Il numero 1 è più grande del numero 2")
    else:
        print("Il numero 2 è più grande del numero 1")
    break


print("Goodbye!")
