from semantica import MaquinaProcesada
from nodos import Direccion

class InterpreteTuring:
    def __init__(self, maquina: MaquinaProcesada, cinta_inicial: str):
        self.maquina = maquina
        self.cinta = list(cinta_inicial) if cinta_inicial else [maquina.simbolo_blanco]
        self.cabezal = 0
        self.estado_actual = maquina.estado_inicial
        self.paso = 0

    def ejecutar(self, max_pasos: int = 500):
        print("\n--- INICIO DE LA SIMULACIÓN ---")
        print(f"{'Paso':<6} | {'Estado':<12} | {'Lee':<5} | Traza de la Cinta")
        print("-" * 65)

        while self.paso < max_pasos:
            if self.cabezal < 0:
                self.cinta.insert(0, self.maquina.simbolo_blanco)
                self.cabezal = 0
            elif self.cabezal >= len(self.cinta):
                self.cinta.append(self.maquina.simbolo_blanco)

            simbolo_actual = self.cinta[self.cabezal]
            cinta_str = "".join(self.cinta)
            print(f"{self.paso:<6} | {self.estado_actual:<12} | {simbolo_actual:<5} | {cinta_str} (cabezal en idx: {self.cabezal})")

            if self.estado_actual in self.maquina.estados_finales:
                print("-" * 65)
                print(f"ÉXITO: Estado final '{self.estado_actual}' alcanzado.")
                print(f"Cinta Final: {''.join(self.cinta).strip(self.maquina.simbolo_blanco)}")
                return True

            clave = (self.estado_actual, simbolo_actual)
            if clave not in self.maquina.tabla_transiciones:
                print("-" * 65)
                print(f"DETENCIÓN: No hay regla para el par ({self.estado_actual}, '{simbolo_actual}').")
                print(f"Cinta Final: {''.join(self.cinta).strip(self.maquina.simbolo_blanco)}")
                return False

            trans = self.maquina.tabla_transiciones[clave]
            self.cinta[self.cabezal] = trans.nuevo_simbolo
            self.estado_actual = trans.nuevo_estado

            if trans.movimiento == Direccion.DER: self.cabezal += 1
            elif trans.movimiento == Direccion.IZQ: self.cabezal -= 1

            self.paso += 1