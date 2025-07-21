
lista_1 = [1, 2, 3]

lista_2 = lista_1

lista_2.append(4)

print(f"lista 1 è: {lista_1}")
print(f"lista 2 è: {lista_2}")

# lista_1 si è modificata (è comparso 4), ma non sono stato io direttamente a farlo!
# SIDE EFFECT. Il problema è dato da riga 4!

# lista_1 e lista_2 puntano alla stessa cella di memoria!!!
# QUESTO FENOMENO é ALTAMENTE PERICOLOSO!!! CAUSA BUG se NON SI FA ATTENZIONE.
# LA RIGA 4 è pericolosissima. USARE CON CAUTELA.

# L'unico caso che utilizzo io personalmente riguarda le funzioni.
# posso realizzare quello che è chiamato in ALTRI LINGUAGGI il passaggio per riferimento.
def funzione_prova(lista_ : list) -> bool:
    
    lista_.append(42)

    return False

abc = ["a", "b", 'c']

funzione_prova(abc)

print(abc)

abc_copia = abc.copy()                      # abc.copy() ha lo stesso effetto di fare
                                            # abc[:] dove : significa accedere a tutti gli
                                            # elementi della lista. E' meglio preferire
                                            # l'utilizzo del .copy(), perchè più leggibile.
abc_copia.append(35)
print(f"abc_copia è: {abc_copia}")
print(f"abc è: {abc}")

lista_lunga = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]       # list slicing
print(lista_lunga)
print(lista_lunga[0:4])                     # printa [5, 6, 7, 8], si va dall'indice 0 fino all'indice di destra -1
print(lista_lunga[1:4])                     # printa [6, 7, 8], si va dall'indice 1 fino a 4-1
print(lista_lunga[2:4])                     # printa [7, 8], si va dall'indice 2 fino a 4-1
print(lista_lunga[ :4])                     # equivale a lista_lunga[0:4]

print(lista_lunga[::-1])                    # fa il reverse della lista.
lista_lunga.reverse()                       # che è equivalente ad utilizzare il metodo reverse()
print(lista_lunga)                          # Il metodo è più leggibile!!