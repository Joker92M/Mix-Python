# Aggiungere un libro alla libreria
def AggiuntaLibro(libri):
    while True:
        try:
            nLibri = int(input("Quanti libri vuoi inserire? "))
            break
        except ValueError:
            print("Inserisci un numero intero.")
            
    for i in range(nLibri):
        libro = input(f"Inserisci il libro {i+1}: ")
        libri.append(libro)
        print(f"Hai aggiunto il libro {i+1}: '{libri[i]}'")


# Prendere in prestito un libro
def PrestitoLibro(libri, libriPrestito):
    while True:
        try:
            nLibriPrestati = int(input("Quanti libri vuoi in prestito? "))
            break
        except ValueError:
            print("Inserisci un numero intero.")
    
    for i in range(nLibriPrestati):
        libroPrestito = input("Quale libro vuoi in prestito? ")
        
        if libroPrestito in libri:
            libriPrestito.append(libroPrestito)
            libri.remove(libroPrestito)
            print(f"Hai preso in prestito il libro: {libroPrestito}")
        else:
            print(f"Il libro '{libroPrestito}' non è disponibile.")


# Riportare un libro preso in prestito
def RestituisciLibro(libri, libriPrestito):
    while True:
        try:
            nLibriRestituiti = int(input("Quanti libri vuoi restituire? "))
            break
        except ValueError:
            print("Inserisci un numero intero.")
    
    for i in range(nLibriRestituiti):
        libroRestituito = input("Quale libro vuoi restituire? ")
    
    if libroRestituito in libriPrestito:
        libriPrestito.remove(libroRestituito)
        libri.append(libroRestituito)
        print(f"Hai riportato il libro: {libroRestituito}")
    else:
        print(f"Il libro '{libroRestituito}' non è stato preso in prestito.")


# Verificare la disponibilità di un libro
def DisponibilitaLibro(libri):
    libro = input("Di quale libro vuoi verificare la disponibilità? ")
    
    if libro in libri:
        print(f"Il libro '{libro}' è disponibile.")
    else:
        print(f"Il libro '{libro}' non è disponibile.")


# Visualizzare i libri disponibili
def LibriDisponibili(libri):
    if libri:
        print("Libri disponibili nella libreria:")
        for libro in libri:
            print(libro)
    else:
        print("Non ci sono libri disponibili nella libreria.")


# Visualizzare i libri attualmente in prestito
def LibriInPrestito(libriPrestito):
    if libriPrestito:
        print("Libri attualmente in prestito:")
        for libro in libriPrestito:
            print(libro)
    else:
        print("Non ci sono libri in prestito.")