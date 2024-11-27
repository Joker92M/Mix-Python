import heapq  # Importiamo il modulo heapq per gestire la coda di priorità usata nell'algoritmo di Dijkstra

class Nodo:  # Definiamo la classe Nodo
    def __init__(self, nome):  # Il costruttore accetta un nome per il nodo
        self.nome = nome  # Assegna il nome al nodo
        self.vicini = {}  # Crea un dizionario vuoto per i nodi vicini

    def aggiungi_vicino(self, nodo, distanza):  # Metodo per aggiungere un nodo vicino e la relativa distanza
        self.vicini[nodo] = distanza  # Aggiunge il nodo e la distanza al dizionario dei vicini

class Grafo:  # Definiamo la classe Grafo
    def __init__(self):  # Il costruttore non accetta parametri
        self.nodi = {}  # Crea un dizionario vuoto per i nodi

    def aggiungi_nodo(self, nodo):  # Metodo per aggiungere un nodo al grafo
        self.nodi[nodo.nome] = nodo  # Aggiunge il nodo al dizionario dei nodi

    def dijkstra(self, nodo_iniziale, nodo_finale):  # Metodo per eseguire l'algoritmo di Dijkstra
        distanze = {nodo: float('inf') for nodo in self.nodi}  # Inizializza le distanze a infinito
        distanze[nodo_iniziale] = 0  # La distanza dal nodo iniziale a se stesso è 0
        coda = [(0, nodo_iniziale)]  # Crea una coda di priorità con il nodo iniziale
        while coda:  # Continua finché la coda non è vuota
            distanza_corrente, nodo_corrente = heapq.heappop(coda)  # Estrae il nodo con la distanza minima
            if distanza_corrente != distanze[nodo_corrente]:  # Se la distanza corrente non è la distanza minima, salta il ciclo
                continue
            for vicino, distanza in self.nodi[nodo_corrente].vicini.items():  # Per ogni nodo vicino
                nuova_distanza = distanza_corrente + distanza  # Calcola la nuova distanza
                if nuova_distanza < distanze[vicino]:  # Se la nuova distanza è minore della distanza corrente
                    distanze[vicino] = nuova_distanza  # Aggiorna la distanza
                    heapq.heappush(coda, (nuova_distanza, vicino))  # Aggiunge il nodo alla coda
        return distanze[nodo_finale]  # Restituisce la distanza minima dal nodo iniziale al nodo finale

# Creazione del grafo
grafo = Grafo()  # Crea un nuovo grafo
for nome in 'ABCDEFG':  # Per ogni lettera da 'A' a 'G'
    grafo.aggiungi_nodo(Nodo(nome))  # Crea un nuovo nodo con quel nome e lo aggiunge al grafo

# Aggiunta degli archi
grafo.nodi['A'].aggiungi_vicino('B', 1)
grafo.nodi['A'].aggiungi_vicino('C', 3)
grafo.nodi['B'].aggiungi_vicino('D', 2)
grafo.nodi['B'].aggiungi_vicino('E', 3)
grafo.nodi['C'].aggiungi_vicino('F', 2)
grafo.nodi['D'].aggiungi_vicino('G', 1)
grafo.nodi['E'].aggiungi_vicino('G', 2)
grafo.nodi['F'].aggiungi_vicino('G', 3)

# Calcolo del percorso più breve da A a G
distanza = grafo.dijkstra('A', 'G')
print(f'La distanza più breve da A a G è {distanza}')  # Stampa la distanza più breve da A a G
