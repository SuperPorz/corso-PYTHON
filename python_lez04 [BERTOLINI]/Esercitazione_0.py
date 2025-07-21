# 1° identifichiamo qual è l'oggetto base che dobbiamo gestire.
#    Stiamo realizzando un software per una libreria, dobbiamo quindi
#    gestire Libri!
#
# 2° implementiamo compra_da_fornitori.
#
# 3° dove mi salvo i libri? Devo capire quale struttura dati devo utilizzare per
#    ricordarmi ciò che ho acquistato.
#
# 4° Implementiamo vendi_libri_nuovi(), seguendo il testo.
#
#           1) Cerchiamo il libro corrispondente a autore_libro e titolo_libro, ---> devo aggiungere titolo e autore in ingresso all'init della classe Libro.
#
#           2) Se è in vendita, lo togliamo dalla merce nuova disponibile
#
#           3) Se non è in vendita, lo comunichiamo al cliente.
#
#           4) Restituiamo un libro al cliente, solo se lo abbiamo trovato.
#
#

PREZZO_UNITARIO_LIBRO           = 10
PREZZO_DI_VENDITA_UNITARIO      = 20

class Libro:
    def __init__(self, titolo, autore) -> None:
        self.titolo     = titolo
        self.autore     = autore


class BookShop:
    def __init__(self, investimento_iniziale) -> None:
        self.cassa                                  = investimento_iniziale
        self.libri_nuovi_da_vendere : list[Libro]   = [ ]

    def compra_da_fornitori(self, quantita, numero_copie):
        # devo comprare dai fornitore più copie di libri.
        spesa_totale = quantita * numero_copie * PREZZO_UNITARIO_LIBRO

        if spesa_totale <= self.cassa:
            # posso comprare i libri!
            for idx in range(quantita):
                for i in range(numero_copie):
                    self.libri_nuovi_da_vendere.append(Libro(f"Titolo-{idx}", f"Autore-{idx}"))
            # decremento i soldi nella cassa
            self.cassa  = self.cassa - spesa_totale

        else:
            print(f"Non è possibile comprare {quantita * numero_copie} libri.") # fast string.

    def vendi_libro_nuovo(self, titolo_libro: str, autore_libro: str) -> Libro:
        # ricerca libri per titolo e autore, se ne trovo uno lo devo restituire in uscita.
        indice_libro_trovato = -1

        for idx,item_libro in enumerate(self.libri_nuovi_da_vendere):
            
            # il libro cercato esiste tra quelli in vendita?
            if (item_libro.titolo == titolo_libro) and (item_libro.autore == autore_libro):
                # ho trovato il libro!
                indice_libro_trovato = idx
                # NON MODIFICATE MAI LA LISTA STESSA IN CUI STATE CERCANDO
                # IL LIBRO!!!!!
                break
        
        if indice_libro_trovato != -1:
            libro_da_vendere = self.libri_nuovi_da_vendere.pop(indice_libro_trovato)
            self.cassa  = self.cassa + PREZZO_DI_VENDITA_UNITARIO
            return libro_da_vendere
        else:
            print(f"Libro dal titolo: {titolo_libro} e autore: {autore_libro} NON TROVATO!")
            return Libro('','')      

libreria = BookShop(100)                
print("Compro dai fornitori 2 libri di 2 copie ciascuno")
libreria.compra_da_fornitori(2, 2)

print(20*"-")
print(f"Cassa attuale: {libreria.cassa}")
for libro in libreria.libri_nuovi_da_vendere:
    print(libro.titolo)
    print(libro.autore)

print(20*"-")
print("Vendiamo un libro.")
libro_acquistato = libreria.vendi_libro_nuovo("Titolo-0", 'Autore-0')
print(libro_acquistato.titolo)
print(libro_acquistato.autore)
print(f"Cassa attuale: {libreria.cassa}")

print(20*"-")
print("Vendiamo un libro.")
libro_acquistato = libreria.vendi_libro_nuovo('HP', "HP")
print(libro_acquistato.titolo)
print(libro_acquistato.autore)
print(f"Cassa attuale: {libreria.cassa}")