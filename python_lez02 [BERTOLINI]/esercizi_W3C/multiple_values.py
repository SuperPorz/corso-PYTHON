#valori multipli assegnati a più variabili: orange assegnato a x, banana a y eccetera
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#stessi valori assegnati a più variabili (tutte e 3 conterrano orange, banana e cherry)
x = y = z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#un solo valore assegnato a variabili diverse
x = y = z = "Orange"
print(x)
print(y)
print(z)

#collezione di valori (liste, tuuples ecc) => python permette l'estrazione dei valori all'interno di variabili. Nota: concetti di "membro sinistro e membro destro"
fruits = ["apple", "banana", "cherry"]
asta, besta, cesta = fruits
print(asta)
print(besta)
print(cesta)

