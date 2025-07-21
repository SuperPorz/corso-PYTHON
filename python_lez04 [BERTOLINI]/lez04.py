COSTO_LIBRO_ACQUISTO_FORNITORI = 10 #€

class Libro:
    def __init__(self, titolo, autore, ):
        self.titolo = titolo
        self.autore = autore
        

# INIT SERVE A FARE IN MODO DI POTER SCEGLIERE I PARAMETRI DELLA CLASSE; 
# serve a dare un valore iniziale allo stato interno

class Bookshop:
    def __init__(self, nome, inv_iniziale: float):
        self.nome = nome
        self.cassa = inv_iniziale
        self.libri_nuovi_da_vendere: list[Libro] = [ ]   #con questa lista creiamo il "database" dei libri in stock

    def compra_dai_fornitori(self, quantita, numero_copie): #prima controllare cassa

        #controllo se soldi necessari sono presenti in cassa
        prezzo_merce = quantita * numero_copie * COSTO_LIBRO_ACQUISTO_FORNITORI
        if self.cassa >= prezzo_merce:
            # cassa sufficiente, quindi si entra nel ciclo for per fare l'ordine stock al fornitore
            for idx in range(quantita):  # itera da 0 a quantita-1!!! 
                for _ in range(numero_copie): #usiamo underscore per indicare a noi che useremo la variab.
                    self.libri_nuovi_da_vendere.append( Libro(f"Titolo {idx + 1}", f"Titolo {idx + 1}") )
        else:
            print(f"Cassa: {self.cassa}. Saldo non sufficiente per l'ordine!")


        
    
    def elenco_merci(self):
        #printiamo tutta la merce in magazzino
        for idx, libro in enumerate(self.libri_nuovi_da_vendere):

            messaggio = f"Libro {idx+1}: \n\t{libro.titolo}\n\t{libro.autore}\n"
            print(messaggio)
            



negozio = Bookshop("Feltrinelli", 50_000)

# come si chiama il metodo "compra da fornitori"?

negozio.compra_da_fornitori(5, 2)

negozio = Bookshop("De ASgostini", 150_000)


