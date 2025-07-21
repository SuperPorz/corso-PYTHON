## esercizio 2: scrivere una funz che restituisca il minimo tra due numeri senza usare built-in

def MINIMO_1(val1, val2):
    if (val1 < val2):
        return print(f'il minimo è {val1}')
    elif (val1 > val2):
        return print(f'il minimo è {val2}')
    else:
        return print('i due numeri sono uguali')

MINIMO_1(3, 19)


## esercizio 3: scrivere una funz che restituisca il minimo tra 3 numeri senza usare built-in DA SISTEMARE

def MINIMO_2(val1,val2,val3):
    if (val1 < val2 & val1 < val3):
        return print(f'il minimo è {val1}')
    elif (val2 < val1 & val2 < val3):
        return print(f'il minimo è {val2}')
    elif (val3 < val1 & val3 < val2):
        return print(f'il minimo è {val3}')
    elif (val3 > val1 & val3 < val2 & val1 < val2):
        return print(f'il minimo è {val1}')
    elif (val3 > val1 & val3 < val2 & val1 > val2):
        return print(f'il minimo è {val2}')
    else:
        return print('error')

MINIMO_2(3, 19, 15)

## esercizio 4: scrivere una funz che controlli se una stringa è palindroma
## esercizio 5: scrivere una funz che accetti una lista e la restituisca priva degli elementi ripetuti

def pulizia_doppioni_1(lista):
    lista_vuota = [ ] 
    for el in lista:
        if el not in lista_vuota:
            lista_vuota.append(el)
    return print(lista_vuota)

x = [1,2,2,3,3,5]
pulizia_doppioni_1(x)


def pulizia_doppioni_2(lista):
    lista_vuota = {lista}
    return print(lista_vuota)

y = ['ciao', 'ciao',3,5]
pulizia_doppioni_1(y)

## esercizio 6: scrivere una funz che 