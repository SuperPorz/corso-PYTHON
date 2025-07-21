
class Impiegato ():

    num_impiegato = [1, 2]
    giorni_tot = 0
    ore_per_giorno = 0
    #media = 0

    def __init__(self, num_impiegato, giorni_tot, ore_per_giorno, ):
        self.num_impiegato  = num_impiegato
        self.giorni_tot     = giorni_tot
        self.ore_per_giorno = ore_per_giorno

    def input_dati(self, num_impiegato, giorni_tot, ore_per_giorno):
        print('Inserire il numero dell\'impiegato di cui si vogliono inserire le INFO: ')
        self.num_impiegato = int(input())
        num_impiegato = self.num_impiegato
        if (num_impiegato == 1):
            print("inserire quanti giorni ha lavorato l'impiegato 1: ")
            self.giorni_tot = int(input())
            giorni_tot = self.giorni_tot
            
            print("inserire quante ore ha lavorato l'impiegato 1: ")
            self.giorni_tot = int(input())


            pass


        
    if (num_impiegato == 1):
        giorni_tot = 3
        ore_per_giorno = [6, 12, 5]
    elif (num_impiegato == 1): 
        giorni_tot = 2
        ore_per_giorno = [11, 6]
    else:
        print('Il numero d\'impiegato inserito non esiste')

    def no_straordinari(self, ore_per_giorno, x):  #con un loop, modifichiamo le ore > 8 settandole a 8
        for x in ore_per_giorno:
            if (x > 8):
                ore_per_giorno[x] = 8 
            else:
                break
    
    def media_giornaliera(self, giorni_tot, ore_per_giorno):
        return sum(ore_per_giorno)/giorni_tot
    
    
        


    
        