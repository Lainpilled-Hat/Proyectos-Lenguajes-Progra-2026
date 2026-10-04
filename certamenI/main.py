import sys
from antlr4.error.ErrorListener import ErrorListener

from analizador import procesar_archivo
from semantica import construir_maquina_compilada
from interprete import InterpreteTuring


class ErrorANTLR(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errores = []

    def syntaxError(
        self,
        recognizer,
        offendingSymbol,
        line,
        column,
        msg,
        e
    ):
        self.errores.append(
            f"Línea {line}, columna {column}: {msg}"
        )


def inicio():

    if len(sys.argv) < 3:
        print(
            "Uso: python main.py <archivo.tm> "
            "<cinta_inicial> [nombre_maquina]"
        )
        sys.exit(1)

    archivo = sys.argv[1]
    cinta_entrada = sys.argv[2]

    nombre_maquina = None

    if len(sys.argv) >= 4:
        nombre_maquina = sys.argv[3]

    try:

        # Parsing con ANTLR4
        ast = procesar_archivo(archivo)

        # Análisis semántico
        maquina = construir_maquina_compilada(
            ast,
            nombre_maquina
        )

        # Simular
        simulador = InterpreteTuring(
            maquina,
            cinta_entrada
        )

        simulador.ejecutar()

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