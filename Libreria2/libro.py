class Libreria:
    def __init__(self):
        self.libri = []
        self.libriPrestito = []

    def AggiuntaLibro(self):
        while True:
            try:
                nLibri = int(input("Quanti libri vuoi inserire? "))
                break
            except ValueError:
                print("Inserisci un numero intero.")
        
        for i in range(nLibri):
            libro = input(f"Inserisci il libro {i+1}: ")
            self.libri.append(libro)
            print(f"Hai aggiunto il libro {i+1}: {self.libri[i]}")

    def PrestitoLibro(self):
        while True:
            try:
                nLibriPrestati = int(input("Quanti libri vuoi in prestito? "))
                break
            except ValueError:
                print("Inserisci un numero intero.")
            
        for i in range(nLibriPrestati):
            libroPrestito = input("Quale libro vuoi in prestito? ")
            
            if libroPrestito in self.libri:
                self.libriPrestito.append(libroPrestito)
                self.libri.remove(libroPrestito)
                print(f"Hai preso in prestito il libro: {libroPrestito}")
            else:
                print(f"Il libro '{libroPrestito}' non è disponibile.")

    def RestituisciLibro(self):
        while True:
            try:
                nLibriRestituiti = int(input("Quanti libri vuoi restituire? "))
                break
            except ValueError:
                print("Inserisci un numero intero.")
                
        for i in range(nLibriRestituiti):
            libroRestituito = input("Quale libro vuoi restituire? ")
        
        if libroRestituito in self.libriPrestito:
            self.libriPrestito.remove(libroRestituito)
            self.libri.append(libroRestituito)
            print(f"Hai riportato il libro: {libroRestituito}")
        else:
            print(f"Il libro '{libroRestituito}' non è stato preso in prestito.")

    def DisponibilitaLibro(self):
        libro = input("Di quale libro vuoi verificare la disponibilità?")
        
        if libro in self.libri:
            print(f"Il libro '{libro}' è disponibile.")
        else:
            print(f"Il libro '{libro}' non è disponibile.")

    def LibriDisponibili(self):
        if self.libri:
            print("Libri disponibili nella libreria:")
            for libro in self.libri:
                print(libro)
        else:
            print("Non ci sono libri disponibili nella libreria.")

    def LibriInPrestito(self):
        if self.libriPrestito:
            print("Libri attualmente in prestito:")
            for libro in self.libriPrestito:
                print(libro)
        else:
            print("Non ci sono libri in prestito.")