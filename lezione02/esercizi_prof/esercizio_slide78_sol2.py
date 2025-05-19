# Scrivere un programma che chieda in input 2 numeri interi separati da spazi e
# che controlli l'eventuale inserimento di quantità non numeriche.
while True:
    print("Inserisci due numeri interi separati da uno spazio.")
    stringa_fornita : str = input()

    # gestiamo il caso in cui la stringa cominci con lo spazio.

    nuova_stringa = stringa_fornita.lstrip(' ').rstrip(' ')             ## stringa_fornita.strip()

    if nuova_stringa.find(' ') == -1:                                   # lo spazio non è stato trovato
        print("Mi hai inserito una sola quantità.")
        continue

    # sicuro che ci sia uno spazio.
    stringhe_separate = nuova_stringa.split(' ')
    # print(stringhe_separate)
    if len(stringhe_separate) != 2:
        print("Non hai inserito il numero di quantità richiesto!")
        continue

    if not (stringhe_separate[0].isdigit() and stringhe_separate[1].isdigit()):
        print("Mi hai inserito due quantità errate!")
        continue

    # ho due stringhe che contengono quantità numeriche.
    numero1 = int(stringhe_separate[0])
    numero2 = int(stringhe_separate[1])

    if numero1 >= numero2:
        print("Il numero 1 è più grande del numero 2")
    else:
        print("Il numero 2 è più grande del numero 1")

    break


        

print("Goodbye!")

# ROBE DA SISTEMARE
#           1)          Se ci sono più di due numeri dire all'utente di inserirne esattamente
#                       due.        FATTO
#           
#           2)          utilizzare un loop fintanto che l'utente non inserisce quantità
#                       corrette.
#
#           4)          Cosa succede se ciò che inserisco inizia con un carattere da un numero e non
#                       è uno spazio.
#
#           3)  Cosa succede se metto una virgola come separatore?
#                       Gestito in maniera sufficientemente corretta.
