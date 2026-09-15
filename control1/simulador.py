class Simulador:
    def __init__(self, tabla, grafo):
        self.tabla = tabla
        self.grafo = grafo
        self.contadores = {}

    def obtener_fuentes(self):
        return [
            nodo for nodo in self.tabla.nodos.values()
            if nodo.tipo == 'FUENTE'
        ]

    def recorrer(self, actual, camino, tiempo):
        nodo = self.tabla.obtener(actual)
        camino.append(nodo)

        if nodo.tipo == 'SUMIDERO':
            return camino, tiempo

        if nodo.tipo == 'OPERADOR':
            tiempo += nodo.tiempo

        destinos = self.grafo.vecinos(actual)
        if not destinos:
            return camino, tiempo

        siguiente = destinos[0]
        destino = self.tabla.obtener(siguiente)

        # Manejo de balanceo de carga (Round-Robin) para réplicas
        if destino.replicas > 1:
            contador = self.contadores.get(siguiente, 0)
            indice = contador % destino.replicas
            self.contadores[siguiente] = contador + 1

            camino.append(f"{destino.id}-{indice + 1}")
            tiempo += destino.tiempo

            destinos2 = self.grafo.vecinos(destino.id)
            if destinos2:
                final_nodo = self.tabla.obtener(destinos2[0])
                camino.append(final_nodo)

            return camino, tiempo

        return self.recorrer(siguiente, camino, tiempo)

    def simular(self, cantidad):
        fuentes = self.obtener_fuentes()

        # Validación estructural: presencia de al menos una FUENTE
        if not fuentes:
            raise Exception("Error semántico: la topología debe tener al menos una FUENTE.")

        # Validación estructural: presencia de al menos un SUMIDERO
        sumideros = [nodo for nodo in self.tabla.nodos.values() if nodo.tipo == 'SUMIDERO']
        if not sumideros:
            raise Exception("Error semántico: la topología debe tener al menos un SUMIDERO.")

        for i in range(cantidad):
            fuente = fuentes[0]
            camino, tiempo = self.recorrer(fuente.id, [], 0)

            texto_camino = []
            for nodo in camino:
                if isinstance(nodo, str):
                    texto_camino.append(f"OPERADOR {nodo}")
                else:
                    if nodo.tipo == "OPERADOR":
                        texto_camino.append(f"OPERADOR {nodo.id} (T: {nodo.tiempo})")
                    else:
                        texto_camino.append(f"{nodo.tipo} {nodo.id}")

            print(f"Evento {i + 1}: " + " -> ".join(texto_camino))
            print(f"Tiempo total acumulado: {tiempo}\n")