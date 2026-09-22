import sys
import parser as parser_module
from lexer import lexer
from parser import parser, tabla, grafo
from simulador import Simulador


def main():

    # Verifica archivo de entrada
    if len(sys.argv) != 2:
        print("Uso: python main.py archivo.txt")
        return

    archivo = sys.argv[1]

    try:
        # Abre el archivo
        with open(archivo, "r", encoding="utf-8-sig") as f:
            contenido = f.read()

        parser.parse(contenido, lexer=lexer) # Analiza el archivo utilizando el lexer y parser

        print("Topología cargada correctamente.\n")

        # Muestra los nodos que fueron registrados en la tabla de símbolos
        print("Tabla de símbolos:") 
        for nodo in tabla.nodos.values():
            print(nodo)

        print("\nSimulación:\n")

        simulador = Simulador(tabla, grafo) # Crea el simulador utilizando la tabla de símbolos y el grafo
        simulador.simular(parser_module.simulacion) # Ejecuta la cantidad de eventos indicada en SIMULAR

    except Exception as e:
        print(e) # Muestra cualquier error 


# Ejecuta el programa cuando se llama directamente desde la consola (python main.py)
if __name__ == "__main__":
    main()