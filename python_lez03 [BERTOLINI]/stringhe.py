# LE STRINGHE NON SONO MUTABILI!

nome = 'Mario'
print(nome)
#nome[4] = 'a'                         # Questo dà TypeError. Il tipo str, non è mutabile.

nome = 'Maria'
nuovo_nome = nome                      # sto creando un nuovo puntatore che punta a Maria.

print(nuovo_nome)                      # Maria
print(nome)                            # Maria

nuovo_nome = 'Lucia'                   # nuovo nome punterà ad una cella diversa che conterrà
                                       # Lucia.

print(nuovo_nome)                       # Lucia
print(nome)                             # Maria

# La stessa cosa accade con le quantità numeriche, o meglio, ACCADE CON TUTTE LE QUANTITA'
# NON MUTABILI.


cognome         = 'Rossi'
nuovo_cognome   = cognome

cognome         = 'Rosa'

print(cognome)                          # Rosa
print(nuovo_cognome)                    # Rossi

# I due puntatori, o le due frecce, sono indipendenti. Sono frecce diverse.

# Garbage collector programma interno all'interprete Python che scansiona il nostro
# programma e guarda se una cella è accessibile. Se non lo è la DEALLOCA AUTOMATICAMENTE.