from libro import AggiuntaLibro, PrestitoLibro, RestituisciLibro, DisponibilitaLibro, LibriDisponibili, LibriInPrestito

libri = []
libriPrestito = []

while True:
    print("\nGestione Libreria")
    print("1. Aggiunta libro")
    print("2. Prestito libro")
    print("3. Restituzione libro")
    print("4. Disponibilità libro")
    print("5. Libri disponibili")
    print("6. Libri in prestito")
    print("7. Esci")
    
    scelta = int(input("Scegli un'opzione: "))
    
    if scelta == 1:
        AggiuntaLibro(libri)
    elif scelta == 2:
        PrestitoLibro(libri, libriPrestito)
    elif scelta == 3:
        RestituisciLibro(libri, libriPrestito)
    elif scelta == 4:
        DisponibilitaLibro(libri)
    elif scelta == 5:
        LibriDisponibili(libri)
    elif scelta == 6:
        LibriInPrestito(libriPrestito)
    elif scelta == 7:
        print("Uscita dal programma completata.")
        break
    else:
        print("Opzione non valida, riprova.")