"""
La sintassi dell'istruzione IF è:

    if condizione:
        codice
    else:
        codice

Attenzione all'indentazione!
"""

quit = False

if quit == False:
    print("quit è uguale a False")
else:
    print("quit è uguale a True")

numero = -33

if numero > 0:
    print("numero è maggiore di 0")
elif numero < 0:
    print("numero minore di 0")
else:
    print("numero uguale a 0")

"""
Possiamo anche concatenare più condizioni di IF, mediante l'utilizzo della parola elif.
Possiamo utilizzare quanti elif vogliamo, alla fine possiamo terminare con un else.

Il blocco else è eseguito solamente se non sono verificate tutte le condizioni precedenti.

Notate che elif ed else sono del tutto opzionali.
"""

denaro = 1_000_000       # €

print(denaro)

if denaro > 100_000:
    print("Sono ricco!")