import sys
from analizador import procesar_archivo
from semantica import construir_maquina_compilada
from interprete import InterpreteTuring


def inicio():

    if len(sys.argv) < 4 or len(sys.argv) > 5:
        print(
            "Uso: python main.py <archivo.tm> "
            "<cinta_inicial> <simbolo_blanco> [nombre_maquina]"
        )
        sys.exit(1)

    archivo = sys.argv[1] # Primer argumento: archivo que contiene la máquina de Turing (.tm)
    cinta_entrada = sys.argv[2] # Segundo argumento: cinta inicial
    simbolo_blanco = sys.argv[3] # Tercer argumento: símbolo que representa el espacio en blanco en la cinta
    nombre_maquina = sys.argv[4] if len(sys.argv) == 5 else None # Cuarto argumento: nombre de la máquina de Turing, opcional

    try:
        ast = procesar_archivo(archivo)  # Lee el archivo DSL y construye el árbol sintáctico.

        # Análisis semántico 
        maquina = construir_maquina_compilada(
            ast,
            nombre_maquina,
            simbolo_blanco
        )

        # Simular
        simulador = InterpreteTuring(
            maquina,
            cinta_entrada
        )

        simulador.ejecutar()

   # Cualquier otro error ocurrido durante la ejecución
    except ValueError as e:
        print(f"\n[!] {e}")
        sys.exit(1)

    except Exception as e:
        print(
            f"\n[!] Error durante la ejecución: {e}"
        )
        sys.exit(1)


if __name__ == "__main__":
    inicio()