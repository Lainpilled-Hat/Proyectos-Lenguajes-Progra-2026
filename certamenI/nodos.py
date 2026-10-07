from dataclasses import dataclass, field
from enum import Enum
from typing import List, Set, Dict


# Direcciones En las que se puede mover el cabezal
class Direccion(Enum):
    IZQ = "IZQ"
    DER = "DER"
    QUIETO = "QUIETO"

# Regla de transición de una Máquina de Turing
@dataclass
class ReglaAST:
    estado_origen: str
    simbolo_leido: str
    estado_destino: str
    simbolo_escrito: str
    movimiento: Direccion

# invocación de una subrutina
@dataclass
class InvocacionSubrutinaAST:
    nombre_subrutina: str
    parametro_entero: int

# Subrutina declarada en el lenguaje
@dataclass
class SubrutinaAST:
    nombre: str
    parametro_nombre: str
    reglas: List[ReglaAST] = field(default_factory=list)

# Máquina de Turing dentro del AST
@dataclass
class MaquinaAST:
    nombre: str
    alfabeto: Set[str] = field(default_factory=set)
    simbolo_blanco: str = "_"
    estados: Set[str] = field(default_factory=set)
    estado_inicial: str = ""
    estados_finales: Set[str] = field(default_factory=set)
    subrutinas_usadas: List[InvocacionSubrutinaAST] = field(default_factory=list)
    transiciones: List[ReglaAST] = field(default_factory=list)

# Programa completo que contiene subrutinas y máquinas de Turing
@dataclass
class ProgramaAST:
    subrutinas: List[SubrutinaAST] = field(default_factory=list)
    maquinas: List[MaquinaAST] = field(default_factory=list)

# Tabla utilizada para registrar estados y símbolos. Comprueba si ya fueron declarados
class TablaSimbolos:
    def __init__(self):
        self.estados: Dict[str, str] = {} # Almacena los estados declarados
        self.simbolos: Dict[str, str] = {} # Almacena los símbolos declarados

    # Agrega un estado a la tabla de símbolos
    def agregar_estado(self, nombre: str):
        # Verifica que no exista otro estado con el mismo nombre
        if nombre in self.estados:
            raise ValueError(
                f"Error Semántico: El estado '{nombre}' está declarado más de una vez."
            )

        self.estados[nombre] = "estado" # Registra el estado

    # Mismo procedimiento para agregar un símbolo a la tabla de símbolos
    def agregar_simbolo(self, simbolo: str):
        if simbolo in self.simbolos:
            raise ValueError(
                f"Error Semántico: El símbolo '{simbolo}' está declarado más de una vez."
            )

        self.simbolos[simbolo] = "simbolo"

    # Comprueba si un estado existe en la tabla
    def existe_estado(self, nombre: str):
        return nombre in self.estados
    # Comprueba si un símbolo existe en la tabla
    def existe_simbolo(self, simbolo: str):
        return simbolo in self.simbolos