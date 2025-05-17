
#due modi identici di printare la stessa cosa: "python is awesome". separatori comma e + sono equivalenti nella funzione PRINT
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python"      #tuttavia qui le 3 stringhe vengono tutte attaccate una all'altra: "Pythonisawesome". 
y = "is"
z = "awesome"
print(x + y + z)

x = "Python "    #Per risolvere, scrivere ad esempio 1a stringa così: "Python "->con lo spazio dopo la n
y = "is "
z = "awesome"
print(x + y + z)


#nel caso di numeri come argomento variabile, nel PRINT l'operatore + esegue la somma
a = 5
b = 7
print(a+b)