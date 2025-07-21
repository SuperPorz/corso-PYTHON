class Pizza:
    def __init__(self, prezzo, costo): # NON è IL COSTRUTTORE
        self.prezzo     = prezzo
        self.contatore  = 0
        self.costo      = costo   

    def azzera_contatore(self):
        self.contatore = 0


class Ordinazione:
    def __init__(self, ora: int, minuti: int, nome: str, pizza: Pizza) -> None:
        self.ora    = ora
        self.minuti = minuti
        self.nome   = nome
        self.pizza  = pizza


class Pizzeria:

    COSTO_SALUME            = 2.00 # costo stimato della porzione necessaria per ciascuna pizza
    COSTO_MOZZARELLA        = 0.75 #
    COSTO_MOZZARELLA_BUFALA = 1.20 #
    COSTO_POMODORO          = 0.50 #

    COSTO_ACQUA             = 0.50 #    
    COSTO_FARINA            = 1.00 #
    COSTO_LIEVITO           = 0.40 #

    def __init__(self, cassa) -> None:
        self.cassa                          = cassa
        self.ordinazioni: list[Ordinazione] = []
        self.menu: dict[str, Pizza]         = {}
        self._compila_menu()

    def _compila_menu(self):
        ...



if __name__ == '__main__':




    da_tony = Pizzeria(20_000,)