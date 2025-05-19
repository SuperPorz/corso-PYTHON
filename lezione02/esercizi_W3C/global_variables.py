#qui creiamo una variabile globale e la usiamo all'interno di una funzione (il valore di x sarà quello assegnato in GLOBALE)
x = "awesome"

def myfunc():
  print("Python is " + x)      ###qui printa "python is awesome" (usando il valore della variabile GLOBALE)

myfunc()

#qui dichiariamo una var.glob, poi la usiamo dentro una funz. ma assegnado un valore diverso (quindi sarà locale); quella esterna (globale) manterrà il suo valore iniziale
x = "awesome"                  #variabile GLOBALE

def myfunc():
  x = "fantastic"              #variabile LOCALE con valore assegnato diverso da quello GLOBALE
  print("Python is " + x)      ###qui printa "python is fantastic" (usando il valore della variabile LOCALE)

myfunc()                       

print("Python is " + x)        ###qui printa "python is awesome" (usando il valore della variabile GLOBALE)

#qui usiamo la keyword "global": permette di creare variabile GLOBALE all'interno di una funz; essa quindi si potrà usare esternamente mantenendo il valore assegnato dentro la funz.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)       ###qui printa "python is fantastic" (usando il valore della variabile GLOBALE ma interna alla funz)