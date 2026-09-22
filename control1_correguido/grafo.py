class Grafo:
    # Representa la topología con una lista de adyacencia
    def __init__(self):
        self.adyacencia = {}  # Guarda cada nodo junto con los nodos a los que esta conectado

    def agregar_nodo(self, nodo):
        if nodo.id not in self.adyacencia: # Agrega el nodo al grafo si aun no existe
            self.adyacencia[nodo.id] = []

    def conectar(self, origen, destino):
        if origen.id not in self.adyacencia: # Si los nodos no estan en el grafo, se agregan antes de conectarlos
            self.agregar_nodo(origen)
        if destino.id not in self.adyacencia:
            self.agregar_nodo(destino) 

        self.adyacencia[origen.id].append(destino.id) # Guarda la conexion desde el nodo origen hacia el destino

    def vecinos(self, identificador):
        return self.adyacencia.get(identificador, []) # Devuelve nodos conectados al nodo indicado