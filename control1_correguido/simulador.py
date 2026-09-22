class Simulador:
    def __init__(self, tabla, grafo):
         # Guarda la tabla de símbolos y el grafo
        self.tabla = tabla
        self.grafo = grafo
        self.contadores = {} # Maneja que réplica debe recibir el siguiente evento

    # Busca todos los nodos que corresponden a una FUENTE
    def obtener_fuentes(self):
        return [
            nodo for nodo in self.tabla.nodos.values()
            if nodo.tipo == 'FUENTE'
        ]

    # Obtiene el nodo actual y lo agrega al camino recorrido
    def recorrer(self, actual, camino, tiempo):
        nodo = self.tabla.obtener(actual)
        camino.append(nodo)

        # Si se llega a un sumidero, termina
        if nodo.tipo == 'SUMIDERO':
            return camino, tiempo

        # Los operadores agregan su tiempo al tiempo total
        if nodo.tipo == 'OPERADOR':
            tiempo += nodo.tiempo

        destinos = self.grafo.vecinos(actual) # Obtiene los nodos conectados al nodo actual
        if not destinos:  # Si no hay conexiones se termina el recorrido
            return camino, tiempo

        siguiente = destinos[0] #primer destino disponible
        destino = self.tabla.obtener(siguiente)

        # Manejo de balanceo de carga (Round-Robin) para réplicas
        if destino.replicas > 1:
            contador = self.contadores.get(siguiente, 0) # Contador actual de la réplica
            indice = contador % destino.replicas # Calcula que réplica recibira el evento
            self.contadores[siguiente] = contador + 1 # Actualizamos contador

            camino.append(f"{destino.id}-{indice + 1}") # Agrega al camino la réplica seleccionada
            tiempo += destino.tiempo # Se suma el tiempo 

            destinos2 = self.grafo.vecinos(destino.id) # Busca el siguiente nodo después del operador replicado
            if destinos2:
                final_nodo = self.tabla.obtener(destinos2[0])
                camino.append(final_nodo)

            return camino, tiempo

        return self.recorrer(siguiente, camino, tiempo) # Si el destino no esta replicado, sigue recorriendo el grafo

    def simular(self, cantidad):
        fuentes = self.obtener_fuentes() #Obtine fuentes 

        # Debe existir al menos una FUENTE
        if not fuentes:
            raise Exception("Error semántico: la topología debe tener al menos una FUENTE.")

        # Busca sumideros
        sumideros = [nodo for nodo in self.tabla.nodos.values() if nodo.tipo == 'SUMIDERO']
        if not sumideros: # Debe existir al menos un SUMIDERO
            raise Exception("Error semántico: la topología debe tener al menos un SUMIDERO.")

        # Simula la cantidad de eventos
        for i in range(cantidad):
            fuente = fuentes[0] # Comenzando desde la primera fuente
            camino, tiempo = self.recorrer(fuente.id, [], 0) # Obtiene el camino y tiempo total

            texto_camino = [] # Lo que se mostrara en pantalla

            for nodo in camino:
                if isinstance(nodo, str):
                    texto_camino.append(f"OPERADOR {nodo}") # Réplicas
                else:
                    if nodo.tipo == "OPERADOR":
                        texto_camino.append(f"OPERADOR {nodo.id} (T: {nodo.tiempo})") # Tiempo de los operadores
                    else:
                        texto_camino.append(f"{nodo.tipo} {nodo.id}") # Fuentes y sumideros

            print(f"Evento {i + 1}: " + " -> ".join(texto_camino)) # Muestra el recorrido realizado por el evento
            print(f"Tiempo total acumulado: {tiempo}\n") # Muestra el tiempo total del evento