# @author: Andrea Bertolini
# @date: 14-05-2025

quit    = False
index   = 0

while quit == False:                    # modo visto in flowgorithm
    index = index + 1

    print(index)

    if index > 10:
        quit = True

"""
Analogamente all'istruzione di IF, il WHILE LOOP necessita della condizione booleana
seguita SEMPRE da :
Tutto ciò che vogliamo scrivere all'interno del while va indentato
"""

while quit == False:                    # modo visto in flowgorithm
    index = index + 1

    print(index)

if index > 10:                          # Qui l'IF è FUORI DAL WHILE, viene dunque eseguito
    quit = True                         # DOPO il while. Cioè MAI.

index = 0

while True:                             # Modo equivalente di fare la stessa cosa.
    index = index + 1

    print(index)

    if index > 10:
        break                           # l'istruzione break, quando eseguita, fa uscire dal ciclo.

    else:
        continue                        # quando eseguito, il continue causa l'esecuzione diretta del ciclo successivo
        print("Ciao")                   # questa non verrà eseguita!

print("End")