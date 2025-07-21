impiegati = [ ]  #lista vuota per gli impiegati (per l'esercizio saranno solo 2) 

class Impiegato:
    def __init__(self, id_impiegato, ) -> None:

        self.nome_impiegato   = id_impiegato 
        self.giorni_lavorati  = 0
        self.registro_ore     = [ ]                  #lista vuota per registrare le ore di ciascun giorno  

    # input dati utente
    def input_dati (self):
        
        #chiedo nome utente e lo inserisco nella lista vuota
        print('Inserire il nome impiegato: ')
        y = input()
        impiegati.append(y)

        #chiedo numero giorni lavorati 
        print('Inserire il numero di giorni lavorati: ')
        self.giorni_lavorati = int(input())

        # faccio ciclo per chiedere le ore di ciascun giorno, dopo setto in automatico il limite a 8 ore
        for x in range(0, self.giorni_lavorati, 1):
            print(f'Inserire il numero di ore per il giorno {x+1}: ')
            ore_giorno = int(input())
            if (ore_giorno > 8):
                ore_giorno = 8
                print('Col cazzo che vedi gli straordinari! Rivolgiti alla CISL! Parassita.')
            else: 
                pass
            self.registro_ore.append(ore_giorno)

    # somma ore totali per impiegato
    def ore_tot (self, ):
        somma = sum(self.registro_ore)
        return somma
    
    # media ore per impiegato
    def media_giornaliera (self, ):
        media =  sum(self.registro_ore) / self.giorni_lavorati
        return media



### MAIN PROGRAM ###


# istanza classe PRIMO impiegato
impiegato_1 = Impiegato(1)  

# metodo input dati sul primo impiegato
impiegato_1.input_dati()


# istanza classe SECONDO impiegato
impiegato_2 = Impiegato(2)  

# metodo input dati sul primo impiegato
impiegato_2.input_dati()


# STAMPA TUTTO L'AMBARADAN
print('registro lavorativo dell\'impiegato:', f' "{impiegati[0]}" ')
for x in impiegato_1.registro_ore:
    print(f'Ore lavorate il giorno {impiegato_1.registro_ore.index(x) + 1}:', x)
print('Ore totali lavorate: ', impiegato_1.ore_tot())
print('Media giornaliera: ', impiegato_1.media_giornaliera(), ' ore/gg')

print('registro lavorativo dell\'impiegato:', f' "{impiegati[1]}" ')
for x in impiegato_2.registro_ore:
    print(f'Ore lavorate il giorno {impiegato_2.registro_ore.index(x) + 1}:', x)
print('Ore totali lavorate: ', impiegato_2.ore_tot())
print('Media giornaliera: ', impiegato_2.media_giornaliera(), ' ore/gg')

