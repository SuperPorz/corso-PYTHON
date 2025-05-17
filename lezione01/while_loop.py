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



while True:                             # Modo equivalente di fare la stessa cosa.
    index = index + 1

    print(index)

    if index > 10:
        break                           # l'istruzione break, quando eseguita, fa uscire dal ciclo.