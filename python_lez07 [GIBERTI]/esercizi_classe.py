# scrivere una funzione generatrice di acronimi; funzionamento: prende in input una stringa e restituisce un acronimo composto dall'unione
# di tutte le prime lettere maiuscole di ogni parola (lettere in minuscolo non vengono considerate)

def acronimi (string:str):
    
    result = ''
    for word in string.split():
        if word.islower():
            result += word[0].upper() #prende il primo carattere e lo butta in maiuscolo
        else:
            result += word[0].upper() #prende il primo carattere e lo butta in maiuscolo
    
    print(result)
        
acronimi('Paola franco Calligola') 



# scrivere una funzione che prenda un valore di temperatura in formato stringa, seguito dal simbolo F oppure C, e restituisca stringa analoga
# con valore convertito in celsius o farenheit:
# F = C*9/5 + 32
# C = (F-32) * 5-9

def temperatura (string:str):
    if (string[-1] == 'F'):
        f = string.replace(string[-1], '') 
        f = float(f)
        result = (f-32) * (5/9)
        print(result, '°C')
    elif (string[-1] == 'C'):
        c = string.replace(string[-1], '') 
        c = float(c)
        result = c*(9/5) + 32
        print(result, '°F')
    else:
        result = 'errore! misura sconosciuta'
        print(result)
    
temperatura('55C')
temperatura('122F') 
temperatura('16G') 

# scrivere una funzione che prenda un numero qualunque di variabili numeriche e restituisca il minimo tra essi senza usare built-in di python; 
# usare quella creata nelle preceddenti lezioni:

def minimum_2_values(a, b):
    if a < b:
        return a
    else:
        return b
    
""" def generic_min(*args:int):
    for i in range(0, len(args), 1):
        x = minimum_2_values(args[i], args[i+1])
        if x == args[i]:
            t = args[i]
        else:
            t = args[i+1]
    print(t)
    
generic_min(3, 5, 22, 1, 68) """


## prof:

def minimum(*numbers:int):
    min = numbers[0]
    
    for n in numbers:
        if minimum_2_values(min, n) != min:
            min = n
    print(min)
    
minimum(3, 5, 22, 1, 68)

# scrivere una funzione che restituisca il prodotto di tutti gli argomenti che vengono forniti alla chiamata dela funzione
# versione_1 -> in caso di immissione di argomenti non numerici, restituire un messaggio di errore
# versione_2 -> scarta le eventuali variabili non numeriche (mostrando cosa viene scartato) ed eseguire il calcolo con i rimanenti elementi

""" def prodotto_v1(*numeri):  # (non funziona)
    for i in numeri:
        if i == 0:
            t = 0
        elif i.isdigit() == True and i != numeri[-1]:
            t *= i * (i+1)
            continue
        elif i.isdigit() == True and i == numeri[-1]:
            t *= t * i
            continue
        else:
            print('Errore! Inseriti valori non numerici')
            return False
    print(t)
    
prodotto(1, 1, 'k', 1)  """
             

## prof:

def multiplication_v1(*vars):
    
    res = 1
    
    for var in vars:
        if type(var) != int and type(var) != float:
            print('Errore! Inseriti valori non numerici')
            return
        
        res *= var
    
    print(res)

print('VERS_1----------------')        
multiplication_v1(1, 1, 'k', 1)
multiplication_v1(6.5, 4, 3, 10) 


##################### (funziona)

def multiplication_v2(*vars):
    
    res = 1
    
    for var in vars:
        if type(var) != int and type(var) != float:
            print(var, 'non è numerico! elemento scartato')
            continue
        else:
            res *= var  
    
    print(res) 
    
print('VERS_2----------------')
multiplication_v2(10, 7, 'k', 21)
multiplication_v2(-5.6, 12, 'CIAO', 'AUGURI')
multiplication_v2(6.5, 4, 3, 10)         
  
  
# scrivere una funzione che restituisca area di quadrato sei nei keyword viene fornita una variabile chiamata 'lato', oppure area cerchio se 
# variabile = 'raggio'

def get_area(**misura):                          ##################### (funziona)
    for key, value in misura.items():
        if key == 'lato':
            area = value * value
        elif key == 'raggio':
            area = value**2 * 3.14
        else: 
            area = 'errore! operazione sconosciuta'
    
    print(f"Il valore dell'area della figura scelta è: {area}")

print('altro esercizio----------------')
get_area(lato = 10)
get_area(raggio = 10)
get_area(pinco = 10)


# espandere la funzione get_area per includere l'area di un rettangolo con lati 'lato1' e 'lato2'
            
def get_area_2(**misura):                          ##################### (funziona)
    for key, value in misura.items():
        if key == 'lato':
            area = value * value
        elif key == 'raggio':
            area = value**2 * 3.14
        elif 'lato1' in misura.keys() and 'lato2' in misura.keys():
            area = misura['lato1'] * misura['lato2']
        else: 
            area = 'errore! operazione sconosciuta'
    
    print(f"Il valore dell'area della figura scelta è: {area}")

print('altro esercizio----------------')
get_area_2(lato1 = 10, lato2 = 15)
get_area_2(lato2 = 7, lato1 = 10)


#prof

def get_area_2_prof(**misura):  
    
    #controllo se ci sono 2 kwargs
    if len(misura)==2 and 'lato1' in misura.keys() and 'lato2' in misura.keys():
        area = misura['lato1'] * misura['lato2']
    else:
        for key, value in misura.items():
            if key == 'lato':
                area = value * value
            elif key == 'raggio':
                area = value**2 * 3.14
            else: 
                area = 'errore! operazione sconosciuta'
    
    print(f"Il valore dell'area della figura scelta è: {area}")

print('altro esercizio_prof----------------')
get_area_2_prof(lato1 = 10, lato2 = 15)
get_area_2_prof(lato2 = 7, lato1 = 10)

''' 
Utilizzo funzioni custom in progetti di grandi dimensioni
E' buona norma ospitare le funzioni in moduli di file con estensione .py nella stessa folder delmain, in modo poi da poterle richiamare dove si
vuole nel progetto;

Supponiamo di aver salvato il file modulo.py in cui è contenuta la definizione di una funzione; la sintassi per richiamarla è l aseguente:

____________________________
import modulo
modulo.nome_funzione(arg1, arg2, ...) 
----------------------------

oppure posso importare la singola funzione:

____________________________
from modulo import nome_funzione
nome_funzione(arg1, arg2, ...)
----------------------------

'''
'''
''' 


class Pet:
    def __init__(self, nome, tipo, eta):
        self.nome = nome
        self.tipo = tipo
        self.eta = eta
        
    def describe(self):
        stringa = f"{self.nome} è un {self.tipo} di {self.eta} anni"
        print(stringa)

cane = Pet('fufi', 'cane', 4)
gatto = Pet('bubula', 'gatto', 7)

cane.describe()
gatto.describe()