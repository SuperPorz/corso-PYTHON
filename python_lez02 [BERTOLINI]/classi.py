## CLASSI ##
# Oggetti software dotati di stato o di memoria su cui è possibile eseguire delle
# azioni.
#
# Gli oggetti si creano mediante la parola chiave class

# Le azioni che è possibile compiere sullo stato di un oggetto sono dette METODI.
# Lo stato è comunemente chiamato ATTRIBUTI, PROPRIETA' o CAMPI. Fisicamente lo stato
# è rappresentato da una o più variabili interne alla classe.

class Persona:

    def __init__(self, nome, eta, altezza, cf, salario=12345):                 # inizializzatore
        self.nome            = nome
        self.eta             = eta
        self.altezza         = altezza
        self._cf             = cf
        self.salario         = salario

    def saluta(self, ):                                         # definisco l'azione da
        print("Ciao " + self.nome)                              # compiere sullo stato di Persona

    def give_raise(self, increment):
        self.salario         = self.salario + increment * self.salario
        self._licenzia()                                        # qui si può usare _licenzia()

    def _licenzia(self):
        pass

# Quando definisco un metodo, devo sempre specificare come primo argomento self.
# self è effettivamente l'oggetto stesso (se stesso). Self serve per far sì che
# i metodi possano accedere alla memoria dell'oggetto.

# Con la parola chiave class sto definendo il 'contratto' della mia classe. Sto in altre
# parole descrivendo le caratteristiche che avranno gli oggetti di tipo Persona.

# Gli oggetti di tipo persona sono dette ISTANZE della CLASSE. Posso creare tantissime
# istanze della mia classe Persona, quante voglio.

# Ci sono metodi di una classe che è possibile definire, tra questi troviamo __init__,
# __new__ ... (dunder methods = double underscores methods).

# __init__ inizializza la memoria del mio oggetto. NON è il COSTRUTTORE, ma viene chiamato
# automaticamente all'atto della creazione dell'istanza della classe..

andrea           = Persona('andrea', 27, 1.75, 'CF123456')      # andrea è l'istanza della classe Persona

giulia : Persona = Persona('giulia', 33, 1.67, "CF34786")

andrea.saluta()
andrea.eta
andrea.altezza

andrea.give_raise(0.15)
giulia.saluta()

# qualora troviate CAMPI di una classe nominati con l'underscore, allora questi sono da
# intendersi AD USO ESCLUSIVAMENTE INTERNO alla classe. Ciò vale anche per i metodi!!

# Sono considerate bad practice in Python le seguenti chiamate
andrea._cf
andrea._licenzia()