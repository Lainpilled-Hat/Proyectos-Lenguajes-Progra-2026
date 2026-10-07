from semantica import MaquinaProcesada
from nodos import Direccion

# Ejecuta la máquina de Turing 
class InterpreteTuring:

    # Elementos de la simulación
    def __init__(self, maquina: MaquinaProcesada, cinta_inicial: str): 
        self.maquina = maquina # Máquina
        self.cinta = list(cinta_inicial) if cinta_inicial else [maquina.simbolo_blanco] # Convierte la cinta de entrada en una lista de símbolos. Si la cinta está vacía, se utiliza el símbolo blanco
        self.cabezal = 0 # Se inicializa el cabezal en la posición 0
        self.estado_actual = maquina.estado_inicial # La máquina comienza en su estado inicial
        self.paso = 0 # Contador de pasos de la simulación

    # Ejecuta la simulación de la Máquina
    def ejecutar(self):
        print("\nINICIO DE LA SIMULACIÓN")
        print(f"{'Paso':<6} | {'Estado':<12} | {'Lee':<5} | Traza de la Cinta")
        print("-" * 65)

        # La simulación continúa hasta que se alcanza un estado final o sale en caso de no encontrar una transición válida
        while 1 == 1:

            # Expande la cinta si el cabezal se mueve fuera de los límites actuales, se expande con el símbolo blanco
            # Si el cabezal se mueve hacia la izquierda 
            if self.cabezal < 0:
                self.cinta.insert(0, self.maquina.simbolo_blanco)
                self.cabezal = 0
            # Si el cabezal se mueve hacia la derecha
            elif self.cabezal >= len(self.cinta):
                self.cinta.append(self.maquina.simbolo_blanco)

            simbolo_actual = self.cinta[self.cabezal] # Símbolo que está leyendo actualmente el cabezal
            cinta_str = "".join(self.cinta)  # Convierte la cinta en un texto para mostrarla
            print(f"{self.paso:<6} | {self.estado_actual:<12} | {simbolo_actual:<5} | {cinta_str} (cabezal en idx: {self.cabezal})")

            # Si el estado actual es un estado final, la simulación termina con éxito
            if self.estado_actual in self.maquina.estados_finales:
                print("-" * 65)
                print(f"ÉXITO: Estado final '{self.estado_actual}' alcanzado.")
                print(f"Cinta Final: {''.join(self.cinta)}")
                return True

            clave = (self.estado_actual, simbolo_actual) # transición: estado actual, símbolo que se está leyendo

            # Si no existe una transición, la simulación termina con error
            if clave not in self.maquina.tabla_transiciones:
                print("-" * 65)
                print(f"DETENCIÓN: No hay regla para el par ({self.estado_actual}, '{simbolo_actual}').")
                print(f"Cinta Final: {''.join(self.cinta)}")
                return False

            trans = self.maquina.tabla_transiciones[clave] # Obtiene la transición correspondiente
            self.cinta[self.cabezal] = trans.nuevo_simbolo # Escribe el nuevo símbolo en la posición actual
            self.estado_actual = trans.nuevo_estado # Cambia al estado indicado por la transición

            # Mueve el cabezal según la dirección de la transición
            if trans.movimiento == Direccion.DER: self.cabezal += 1
            elif trans.movimiento == Direccion.IZQ: self.cabezal -= 1
            
            self.paso += 1 # Aumenta el número de pasos
