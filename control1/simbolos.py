class Nodo:
    """Representa los nodos de la topología (FUENTE, OPERADOR, SUMIDERO)."""
    def __init__(self, identificador, tipo, tiempo=0, replicas=1):
        self.id = identificador
        self.tipo = tipo
        self.tiempo = tiempo
        self.replicas = replicas

    def __str__(self):
        return (
            f"{self.id}: "
            f"tipo={self.tipo}, "
            f"tiempo={self.tiempo}, "
            f"replicas={self.replicas}"
        )


class TablaSimbolos:
    """Tabla de Símbolos para validar unicidad y referencias de nodos."""
    def __init__(self):
        self.nodos = {}

    def agregar(self, nodo):
        if nodo.id in self.nodos:
            raise Exception(
                f"Error semántico: el nodo '{nodo.id}' ya fue declarado."
            )
        self.nodos[nodo.id] = nodo

    def existe(self, identificador):
        return identificador in self.nodos

    def obtener(self, identificador):
        if not self.existe(identificador):
            raise Exception(
                f"Error semántico: el nodo '{identificador}' no existe."
            )
        return self.nodos[identificador]