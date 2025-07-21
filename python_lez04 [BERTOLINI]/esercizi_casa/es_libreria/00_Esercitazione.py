import random

COSTO_LIBRO_ACQUISTO_FORNITORI                       = 10 # €
COSTO_LIBRO_VENDITA_CLIENTI                          = 20 # €
USED_BOOK_MAX_PRICE_POSSIBLE                         = 8

class Libro:
    def __init__(self, titolo, autore) -> None:

        self.titolo                                  = titolo
        self.autore                                  = autore

class BookShop:

    def __init__(self, nome: str, investimento_iniziale: float) -> None:
        self.nome_negozio                            = nome
        self.cassa                                   = investimento_iniziale        # €
        self.libri_nuovi_da_vendere: list[Libro]     = [ ]                          # in magazzino
        self.libri_usati_da_vendere: list[Libro]     = [ ]                          # in magazzino

    def mostra_cassa(self):
        print(f"Cassa totale: {self.cassa}€")

    def compra_dai_fornitori(self, quantita: int, numero_copie: int) -> None:
        prezzo_merce = quantita * numero_copie * COSTO_LIBRO_ACQUISTO_FORNITORI
        if self.cassa >= prezzo_merce:
            for idx in range(quantita):
                for _ in range(numero_copie):# _ è una convenzione!! Può esserci qualsiasi nome. Provate a printarlo!
                    # l'underscore indica che quella variabile non serve all'interno del for.
                    self.libri_nuovi_da_vendere.append( Libro(f"titolo {idx+1}", f"autore {idx+1}") )
            self.cassa = self.cassa - prezzo_merce
        else:
            print(f"Cassa: {self.cassa} non sufficiente per acquistare la merce desiderata!")
        # modo ALTERNATIVO.
        # if self.cassa < prezzo_merce:         # guard if
        #     print(f"Cassa: {self.cassa} non sufficiente per acquistare la merce desiderata!")
        #     return
        # # qui sono sicuro di aver abbastanza soldi, procedo!
        # for idx in range(quantita):
        #     for _ in range(numero_copie):# _ è una convenzione!! Può esserci qualsiasi nome. Provate a printarlo!
        #                                  # l'underscore indica che quella variabile non serve all'interno del for.
        #         self.libri_nuovi_da_vendere.append( Libro(f"titolo {idx+1}", f"autore {idx+1}") )
        # self.cassa = self.cassa - prezzo_merce
        
    def elenco_merce(self):
        # printiamo a schermo tutta la merce in magazzino
        for idx, libro in enumerate(self.libri_nuovi_da_vendere):
            # idx è l'indice in cui l'elemento libro si trova in self.libri_nuovi_da_vendere
            # Libro 1:                          # ctrl k  ctrl c serve per commentare un blocco di righe
            # 			titolo                  # ctrl k  ctrl u serve per decommentare un blocco di righe
            # 			autore
            #          
            # Libro 2:
            # 			titolo
            # 			autore
            messaggio = f"Libro {idx+1}:\n\t{libro.titolo}\n\t{libro.autore}\n"
            print(messaggio)
        
        print(f"Numero di libri nuovi in magazzino: {len(self.libri_nuovi_da_vendere)}")

        # printiamo a schermo tutta la merce in magazzino
        for idx, libro in enumerate(self.libri_usati_da_vendere):
            # idx è l'indice in cui l'elemento libro si trova in self.libri_nuovi_da_vendere
            # Libro 1:                          # ctrl k  ctrl c serve per commentare un blocco di righe
            # 			titolo                  # ctrl k  ctrl u serve per decommentare un blocco di righe
            # 			autore
            #          
            # Libro 2:
            # 			titolo
            # 			autore
            messaggio = f"Libro {idx+1}:\n\t{libro.titolo}\n\t{libro.autore}\n"
            print(messaggio)
        
        print(f"Numero di libri usati in magazzino: {len(self.libri_usati_da_vendere)}")

    def vendi_libro_nuovo(self, titolo_libro: str, autore_libro: str) -> Libro:
        # vendere al cliente un libro presente tra gli articoli in vendita
        indice_libro_desiderato = -1

        # Il libro è effettivamente in vendita??
        for idx, item in enumerate(self.libri_nuovi_da_vendere):
            
            if (item.autore == autore_libro) and (item.titolo == titolo_libro):
                # ho trovato il libro tra la merce!
                # devo salvarmi l'indice in cui libro desiderato compare nella lista
                indice_libro_desiderato     = idx
                break

        # MAI MODIFICARE la lista su cui stiamo scorrendo! O scorriamo la lista oppure la modifichiamo.
        # Se indice_libro_desiderato rimane a -1, io dentro all'if non ci sono mai andato! Non ho trovato mai
        # la corrispondenza titolo-autore.
        if indice_libro_desiderato == -1:
            # libro non trovato
            print(f"Libro desiderato dal titolo {titolo_libro} e autore {autore_libro} NON TROVATO!")
            return Libro('', '',)
        else:
            # libro trovato, indice_libro_desiderato contiene l'indice in cui libro si trova all'interno della
            # lista.
            libro_voluto    = self.libri_nuovi_da_vendere.pop(indice_libro_desiderato)
            self.cassa      = self.cassa + COSTO_LIBRO_VENDITA_CLIENTI

            return libro_voluto

    def stima_prezzo_libro(self, libro: Libro) -> float:
        if self._stato_buono():
            prezzo_stimato: float = self._decidi_prezzo()
            if prezzo_stimato == 0:
                print(f"Il libro {libro.titolo} di {libro.autore} non ha mercato!")
                return 0
            else:
                # accetta il libro, restituisci l'importo stimato al cliente.
                print(f"L'importo stimato di {libro.titolo} di {libro.autore} è: {prezzo_stimato}€")
                self.libri_usati_da_vendere.append(libro)
                self.cassa      = self.cassa - prezzo_stimato
                return prezzo_stimato
        else:
            print(f"Il libro: {libro.titolo} di {libro.autore} non è in buono stato! Non posso accettarlo!")
            return 0

    def _stato_buono(self) -> bool:
        random_number = random.Random()
        return random_number.choice([True,False])

    def _decidi_prezzo(self) -> float:
        random_number = random.Random()
        return random_number.choice(range(USED_BOOK_MAX_PRICE_POSSIBLE+1))

negozio_feltrinelli = BookShop('Feltrinelli', 250)       # istanza di BookShop

negozio_feltrinelli.compra_dai_fornitori(5, 2)
print("Prima di vendere")
negozio_feltrinelli.elenco_merce()
negozio_feltrinelli.mostra_cassa()
negozio_feltrinelli.vendi_libro_nuovo('Biancaneve', 'abc')

libro_acquistato = negozio_feltrinelli.vendi_libro_nuovo('titolo 3', 'autore 3')
print("Dopo aver venduto")
negozio_feltrinelli.elenco_merce()
negozio_feltrinelli.mostra_cassa()

prezzo = negozio_feltrinelli.stima_prezzo_libro(Libro('Game of Thrones, le cronache del ghiaccio e del fuoco', 'George R.R. Martin'))
print(f"Importo assegnato al cliente {prezzo}€")
prezzo = negozio_feltrinelli.stima_prezzo_libro(Libro('Matilde', 'Rohal Dahl'))
print(f"Importo assegnato al cliente {prezzo}€")
prezzo = negozio_feltrinelli.stima_prezzo_libro(Libro("Assasinio sull'Oriente Express", 'Agatha Christie'))
print(f"Importo assegnato al cliente {prezzo}€")
prezzo = negozio_feltrinelli.stima_prezzo_libro(Libro('Pinocchio', 'Collodi'))
print(f"Importo assegnato al cliente {prezzo}€")

negozio_feltrinelli.elenco_merce()
negozio_feltrinelli.mostra_cassa()

# negozio_deagostini  = BookShop('Deagostini', 100)        # istanza di BookShop
# negozio_deagostini.vendi_libro_nuovo('ciao', 'abcd')
# negozio_deagostini.elenco_merce()
# negozio_deagostini.mostra_cassa()