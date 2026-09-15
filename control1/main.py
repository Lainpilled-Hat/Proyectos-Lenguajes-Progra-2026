import sys
import parser as parser_module
from lexer import lexer
from parser import parser, tabla, grafo
from simulador import Simulador


def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py archivo.txt")
        return

    archivo = sys.argv[1]

    try:
        with open(archivo, "r", encoding="utf-8-sig") as f:
            contenido = f.read()

        parser.parse(contenido, lexer=lexer)

        print("Topología cargada correctamente.\n")
        print("Tabla de símbolos:")
        for nodo in tabla.nodos.values():
            print(nodo)

        print("\nSimulación:\n")

        simulador = Simulador(tabla, grafo)
        # Se pasa la cantidad importada desde el módulo directamente para evitar valor 0
        simulador.simular(parser_module.simulacion)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()