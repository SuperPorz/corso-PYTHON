# Come si elencano i metodi di una classe, sia questa già implementata da qualcuno, che
# implentata da noi.

# Bisogna usare una funzione chiamata: dir( )

print(dir(list))

help(list.append)

lista_ = [ ]                     # Lista vuota

lista_.append(1)
lista_.append(2)
lista_.append(3)
lista_.append(4)
lista_.append('5')

print(lista_)                    # Lista con 5 elementi.

help(list.pop)

print(lista_.pop())
print(lista_)

print(lista_.pop(2))
print(lista_)

help(list.count)

print(lista_.count(1))

lista_.append(1)
lista_.append(1)
lista_.append(1)
print(lista_) 
print(lista_.count(1))          # Conto quante volte l'1 compare all'interno di lista_

print(lista_.count(42))         # 0, perchè 42 non compare all'interno di lista_


def dir_speciale(object):

    metodi_disponibili : list[str]  = dir(object)

    metodi_filtrati                 = [ ]

    for item in metodi_disponibili:
        if '__' not in item:
            metodi_filtrati.append(item)
    
    return metodi_filtrati


print(dir_speciale(list))


lista_1 = [1, 2, 3]

lista_2 = [4, 5, 6]

lista_1.extend(lista_2)
print(lista_1)

lista_3 = lista_1 + lista_2
print(lista_3)