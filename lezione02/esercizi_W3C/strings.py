
# le stringhe sono array!!!
a = "Hello, World!"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5]) # virgola
print(a[6]) # spazio
print(a[7])
print(a[8])
print(a[9])
print(a[10])
print(a[11])
print(a[12])

# loop di caratteri contenuti in una stringa: 
for x in "banana":
  print(x)

# funzione "length": calcola la lunghezza di una variabile, contando di fatto gli elementi
a = "Hello, World!"
print(len(a))

# funzione "in": restituisce un booleano!!!
frase = "The best things in life are free!"
print("free" in frase)

if "free" in frase:
  print("Yes, 'free' is present.")   #stesso esempio, ma con condizione

# slice (fetta, parte) in un range definito (slicing = estrarre una porzione)
b = "Hello, World!"
print(b[2:5])

#slicing con range ad indici negativi (si inizia a contare gli elementi da destra, ma il primo numero è 1 e non 0)
c = "Hello, World!"
print(c[-5:-2])


#### MODIFICHE ALLE STRINGHE ####

#upper
a = "Hello, World!"                   
print(a.upper())

#lower
a = "Hello, World!"                   
print(a.lower())

#strip  ######################### rimuove spazi bianchi a inizio e fine, non in mezzo)
a = " Hello, World! "                 
print(a.strip())                      

#replace  ####################### rimpiazza un carattere con un altro; il primo è quello da togliere, il secondo quello che lo sostituisce
a = "Hello, World!"                   
print(a.replace("H", "J"))

#split  ######################### restituisce una lista costituita da elementi ottenuti separando la stringa tramite un divisore che indichiamo noi; esempio la virgola
a = "Hello, World!"
print(a.split(",")) # restituisce ['Hello', ' World!'] che è una lista


age = 36
txt = f"My name is John, I am {age}"
print(txt)

# verifichiamo se il primo carattere della stringa è un NUMERO; se si printa TRUE, altrimenti printa UN MESSAGGIO DI ERRORE
t = "0ciao"
t_prima = t[0]

if t_prima.isdigit() == True:
    print(t_prima.isdigit())
else: 
  print('Il primo carattere deve essere per forza un numero!')

