# Commento di una sola riga

"""
Nella dichiarazione delle variabili non serve inserire il tipo di dato.
Quando diachiarate una variabile dovete anche inizializzarla, questo evita che
utilizziate una variabile senza che questa non sia prima inizializzata.

Nelle versioni recenti di Python sono state introdotte le type annotations, cioè
potete inserire nella dichiarazione delle variabili anche l'informazione sul tipo
di dato che dovranno contenere.

Se anche utilizzi la variabile con il tipo di dato diverso dalla annotazione, Python
non restituisce un errore di programmazione.
"""

print("Inserisci il tuo nome: ")
name  : str = input()                       # Esempio di type annotation

print(name)

print("Inserisci un numero intero: ")
name = int(input())                         # Errore di VSCode che NON è UN ERRORE di PROGRAMMAZIONE

print("Il numero che hai inserito è: " + str(name))

###################################################################################################
# BOOL
###################################################################################################
quit : bool = False
quit        = True

###################################################################################################
# FLOAT
###################################################################################################
number : float = 33.3
number         = 54.4

###################################################################################################
# STRING
###################################################################################################
my_string : str     = 'Ciao'
my_string           = 'Ciao'

###################################################################################################
# INT
###################################################################################################
my_integer : int     = 12
my_integer           = 12