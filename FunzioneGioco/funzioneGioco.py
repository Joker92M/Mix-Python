import random

def esegui_funzione():
    print(f"Numero generato: {numero}")
    numero = random.randint(1, 10)
    if numero < 5:
        print("Il numero è inferiore a 5. Rieseguo la funzione.")
        esegui_funzione()
    else:
        print("Il numero è maggiore o uguale a 5. Fine.")

# Richiamo la funzione
esegui_funzione()