from dataclasses import dataclass, field
from enum import Enum
from typing import List, Set, Dict


class Direccion(Enum):
    IZQ = "IZQ"
    DER = "DER"
    QUIETO = "QUIETO"


@dataclass
class ReglaAST:
    estado_origen: str
    simbolo_leido: str
    estado_destino: str
    simbolo_escrito: str
    movimiento: Direccion


@dataclass
class InvocacionSubrutinaAST:
    nombre_subrutina: str
    parametro_entero: int


@dataclass
class SubrutinaAST:
    nombre: str
    parametro_nombre: str
    reglas: List[ReglaAST] = field(default_factory=list)


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


@dataclass
class ProgramaAST:
    subrutinas: List[SubrutinaAST] = field(default_factory=list)
    maquinas: List[MaquinaAST] = field(default_factory=list)


class TablaSimbolos:
    def __init__(self):
        self.estados: Dict[str, str] = {}
        self.simbolos: Dict[str, str] = {}

    def agregar_estado(self, nombre: str):
        if nombre in self.estados:
            raise ValueError(
                f"Error Semántico: El estado '{nombre}' está declarado más de una vez."
            )

        self.estados[nombre] = "estado"

    def agregar_simbolo(self, simbolo: str):
        if simbolo in self.simbolos:
            raise ValueError(
                f"Error Semántico: El símbolo '{simbolo}' está declarado más de una vez."
            )

        self.simbolos[simbolo] = "simbolo"

    def existe_estado(self, nombre: str):
        return nombre in self.estados

    def existe_simbolo(self, simbolo: str):
        return simbolo in self.simbolos