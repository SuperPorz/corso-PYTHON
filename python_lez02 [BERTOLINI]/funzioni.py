## DEFINIZIONE DI UNA FUNZIONE - CONTRATTO DELLA FUNZIONE ##
# numero1 e numero2 sono gli ARGOMENTI della funzione, questi possono essere
# tanti, l'importante è che sia esplicitamente indicato nel contratto della
# funzione.
def somma_1(numero1: float, numero2: float) -> float:
    somma = numero1 + numero2
    return somma

def somma_2(numero1: float, numero2: float) -> float:
    return numero1 + numero2

risultato = 0

## CHIAMATA DELLA FUNZIONE
risultato = somma_1(2, 3)             # 1° chiamata

print(risultato)

risultato = somma_1(risultato, 4)     # 2° chiamata

print(risultato)

## ARGOMENTI di DEFAULT di una funzione.
# Normalmente quando si chiama una funzione bisogna rispettare il contratto, quindi
# se la funzione si aspetta 10 parametri, per esempio, bisogna fornire 10 paramentri
# all'atto della chiamata.

# Alcune volte ciò può essere tedioso, a questo servono gli argomenti di default!

# Gli argomenti di default entrano in gioco quando una funzione è chiamata senza
# che questi siano specificati.

def decremento_1(sottraendo, sottratto=1):
    return sottraendo - sottratto

def somma4(numero1 = 3, numero2 = 4, numero3 = 5, numero4 = 6):
    return numero1 + numero2 + numero3 + numero4
# In questo caso, chi chiama la funzione decremento() può scegliere di NON PASSARE
# il secondo argomento. Se ciò avviene, dentro alla funzione sottratto varrà 1.

# Se invece il programmatore specifica anche sottratto, allora il contenuto di sottratto
# sarà esattamente quello fornito all'atto della chiamata.

# N.B. Quando usate argomenti di default, nella definizione e nella chiamata della funzione questi
# DEVONO essere OBBLIGATORIAMENTE elencati DOPO gli argomenti obbligatori (quelli senza l'uguale).
#
#   decremento_1(sottratto=1, 3)                                              # SBAGLIATO!!
#   

risultato_sottrazione = decremento_1(5)                                       # 1° modo. Chiamo la funzione con SOLO
print(risultato_sottrazione)                                                  # gli argomenti obbligatori.

risultato_sottrazione = decremento_1(risultato_sottrazione, 2)                # 2° modo. Chiamo la funzione con anche
print(risultato_sottrazione)                                                  # l'argomento facoltativo.

risultato_sottrazione = decremento_1(risultato_sottrazione, sottratto=2)      # 3° modo. Uguale al 2°, ma specifico anche
print(risultato_sottrazione)                                                  # il nome dell'argomento di default.

risultato_sottrazione = somma4()
risultato_sottrazione = somma4(numero1=66)
risultato_sottrazione = somma4(numero2=42)
risultato_sottrazione = somma4(numero1=66, numero2=42)

## FUNZIONI con il numero di argomenti variabili a runtime
def funzione_1(*args):
    pass

# si utilizza la notazione con l'asterisco. Generalmente si trova *args e va messo
# come ultimo input della funzione, quindi dopo gli argomenti obbligatori e default.

risultato_funzione_1 = funzione_1(1,2,3,4,5)
risultato_funzione_2 = funzione_1(1,'2',3,'4',5,10,12,124,2425,5667,8)
risultato_funzione_2 = funzione_1()

# è utilizzato per esempio quando una funzione deve eseguire l'operazione su un numero
# di input non noto a priori. Oppure la si può utilizzare per prevedere eventuali future
# estensioni alla logica della funzione.
