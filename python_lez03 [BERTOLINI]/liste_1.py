# COLLEZIONI ORDINATE di oggetti POTENZIALMENTE DISOMOGENEI, ma vi consiglio di
# creare LISTE OMOGENEE di oggetti.
class Persona:
    def __init__(self, nn, *args) -> None:
        self.name = nn


lista_1 = [ ]                                  # 1° modo UNA LISTA VUOTA

lista_2 = list()                               # 2° modo. UNA LISTA VUOTA


lista_3 = ['Ciao', Persona(4), 1, False]       # 1° modo, UNA LISTA NON VUOTA. (preferibile)

lista_4 = list(('Ciao', Persona(4), 1, False)) # 2° modo, UNA LISTA NON VUOTA

print(lista_4[0])                               # printa Ciao.
print(lista_4[1])                               # printa qualcosa.
print(lista_4[2])                               # printa 1.
print(lista_4[3])                               # printa False.

#print(lista_4[4])                              # IndexError! State accedendo all'elemento
                                                # di una lista che non esiste. Siete fuori
                                                # dalla lista. Provate a decommentare il print()

for idx in range(len(lista_4)):                 # come iterare sulla lista, ovvero come
    print(lista_4[idx])                         # accedere elemento per elemento alla lista.

# La funzione len() vi permette di calcolare la lunghezza di questa lista. Se lista_4 ha
# 4 elementi, len(lista_4) restituirà 4.

# Ma c'è un modo ancora più semplice ed elegante. 
for item in lista_4:                            # accedo alla lista senza preoccuparmi di
    print(item)                                 # quanto questa sia lunga. Non mi serve
                                                # la lunghezza.
                                                # Però, non ho cognizione della posizione
                                                # in cui si trova item.

for idx,item in enumerate(lista_4):             # enumerate() è una classe che fornisce in
    print(idx)                                  # uscita una coppia di valori. A sinistra sempre
    print(item)                                 # l'indice corrente dell'elemento item della
                                                # lista fornita in ingresso ad enumerate()


lista_5 = [Persona("Mario"), Persona("Lucia"), Persona("Marco")]

for idx,item in enumerate(lista_5):
    print(idx)
    print(item.name)