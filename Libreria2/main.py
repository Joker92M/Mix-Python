from libro import Libreria

libreria = Libreria()

while True:
    print("\nGestione Libreria")
    print("1. Aggiunta libro")
    print("2. Prestito libro")
    print("3. Riporta libro")
    print("4. Disponibilità libro")
    print("5. Libri disponibili nella libreria")
    print("6. Libri dati in prestito")
    print("7. Esci")
    
    scelta = int(input("Scegli un'opzione: "))
    
    if scelta == 1:
        libreria.AggiuntaLibro()
    elif scelta == 2:
        libreria.PrestitoLibro()
    elif scelta == 3:
        libreria.RestituisciLibro()
    elif scelta == 4:
        libreria.DisponibilitaLibro()
    elif scelta == 5:
        libreria.LibriDisponibili()
    elif scelta == 6:
        libreria.LibriInPrestito()
    elif scelta == 7:
        print("Uscita dal programma...")
        break
    else:
        print("Opzione non valida, riprova.")