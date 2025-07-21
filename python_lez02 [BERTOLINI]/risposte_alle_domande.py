
# print("Inserisci un numero:")
# user_input = int(input())

# if user_input > 0:
#     print("Il numero è positivo")
# elif user_input == 0:
#     print("Il numero è nullo")
# else:
#     print("il numero è negativo")

NUMERO_UTENTI_CONTEMPORANEI     = 4                 # Python non ha la possibilità, a meno trick, di definire
                                                    # variabili come costanti. Da intendersi come immutabili.
                                                    # Per indicare al programmatore che una variabile è da trattare
                                                    # come costante si utilizzano le maiuscole.

for i in range(5,0,-1):
    print(i)

NUMERO_UTENTI_CONTEMPORANEI     = 42                # Nulla mi vieta di cambiare il suo valore, ma è una bad practice!


print(NUMERO_UTENTI_CONTEMPORANEI)