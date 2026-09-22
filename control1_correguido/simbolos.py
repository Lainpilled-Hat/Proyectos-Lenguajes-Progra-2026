class Nodo:
    #Representa los nodos de la topologia (FUENTE, OPERADOR, SUMIDERO)
    def __init__(self, identificador, tipo, tiempo=0, replicas=1):
        self.id = identificador
        self.tipo = tipo
        self.tiempo = tiempo
        self.replicas = replicas

    # Muestra la información del nodo de forma ordenada
    def __str__(self):
        return (
            f"{self.id}: "
            f"tipo={self.tipo}, "
            f"tiempo={self.tiempo}, "
            f"replicas={self.replicas}"
        )


class TablaSimbolos:
    # Guarda los nodos creados y verifica que no existan identificadores repetidos
    def __init__(self):
        self.nodos = {}

    def agregar(self, nodo):
        # Evita que se declare más de un nodo con el mismo identificador
        if nodo.id in self.nodos:
            raise Exception(
                f"Error semántico: el nodo '{nodo.id}' ya fue declarado."
            )
        self.nodos[nodo.id] = nodo # Guarda el nodo usando su identificador como clave

    def existe(self, identificador):
        return identificador in self.nodos # Comprueba si un nodo ya fue declarado

    def obtener(self, identificador):
        # Verifica que el nodo exista antes de obtenerlo
        if not self.existe(identificador):
            raise Exception(
                f"Error semántico: el nodo '{identificador}' no existe."
            )
        return self.nodos[identificador]  # Devuelve el nodo