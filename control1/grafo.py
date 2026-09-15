class Grafo:
    """Representa la topología mediante una lista de adyacencia."""
    def __init__(self):
        self.adyacencia = {}

    def agregar_nodo(self, nodo):
        if nodo.id not in self.adyacencia:
            self.adyacencia[nodo.id] = []

    def conectar(self, origen, destino):
        if origen.id not in self.adyacencia:
            self.agregar_nodo(origen)
        if destino.id not in self.adyacencia:
            self.agregar_nodo(destino)

        self.adyacencia[origen.id].append(destino.id)

    def vecinos(self, identificador):
        return self.adyacencia.get(identificador, [])