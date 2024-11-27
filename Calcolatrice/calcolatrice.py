while True:
    operazione = input("Scegli l'operazione (+, -, *, /): ")
    if  operazione in ('+', '-', '*', '/'):
        num1 = float(input("Inserisci il primo numero: "))
        num2 = float(input("Inserisci il primo numero: "))
        
        if operazione == '+':
            print(f"{num1} + {num2} = {num1 + num2}")

        elif operazione == '-':
            print(f"{num1} - {num2} = {num1 - num2}")

        elif operazione == '*':
            print(f"{num1} * {num2} = {num1 * num2}")

        elif operazione == '/':
            if (num2 != 0):
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Errore: divisione per zero non consentita.")
    else:
        print("Operazione non valida.")