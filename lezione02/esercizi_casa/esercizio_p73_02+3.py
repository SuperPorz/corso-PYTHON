 ##### ESERCIZIO 2, pag. 73 SLIDES PYTHON-1: "data una stringa di 3 parole, printala con lettere CAPITAL; poi CAPITAL su ogni parola ma solo sulla prima lettera"

print("inserire esattamente 3 parole (non una di più e non una di meno)")
# prima richiesta dell'esercizio
stringa = input()
print(stringa.upper())

# seconda richiesta dell'esercizio
listaStringa = stringa.split()
a = listaStringa[0]
b = listaStringa[1]
c = listaStringa[2]
print(a.capitalize(), b.capitalize(), c.capitalize())


##### ESERCIZIO 3, pag. 73 SLIDES PYTHON-1: printa la stringa dell'esercizio precedente (ultima parte)
z = stringa.replace(" ", "")
print ("La lunghezza della stringa è: ", len(z))

#metodo alternativo per la lunghezza senza gli spazi
a1 = len(a)
b1 = len(b)
c1 = len(c)
z1 = a1 + b1 + c1
print("La lunghezza della stringa è: ", z1)

#lunghezza totale inclusi gli spazi
print("se includiamo gli spazi, la lunghezza è: ", len(stringa))