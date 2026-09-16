import sys
from analizador import procesar_archivo
from semantica import construir_maquina_compilada
from interprete import InterpreteTuring

def inicio():
    if len(sys.argv) < 3:
        print("Uso: python main.py <archivo.tm> <cinta_inicial>")
        sys.exit(1)

    archivo = sys.argv[1]
    cinta_entrada = sys.argv[2]

    # 1. Parsing con ANTLR4
    ast = procesar_archivo(archivo)

    # 2. Análisis Semántico y Tabla de Transiciones
    maquina = construir_maquina_compilada(ast)

    # 3. Simular
    simulador = InterpreteTuring(maquina, cinta_entrada)
    simulador.ejecutar()

if __name__ == "__main__":
    inicio()