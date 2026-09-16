from lark import Lark, Transformer
from nodos import (
    Direccion, ReglaAST, InvocacionSubrutinaAST, 
    SubrutinaAST, MaquinaAST, ProgramaAST
)

gramatica_dsl = r"""
    start: programa
    programa: (subrutina | maquina)+
    subrutina: "subrutina" CNAME "(" CNAME ")" "{" reglas "}"
    maquina: "maquina" CNAME "{" alfabeto estados inicial finales (usa_subrutina)* transiciones "}"
    alfabeto: "alfabeto" ":" SIMBOLO ("," SIMBOLO)*
    estados: "estados" ":" CNAME ("," CNAME)*
    inicial: "inicio" ":" CNAME
    finales: "finales" ":" CNAME ("," CNAME)*
    usa_subrutina: "usa" CNAME "(" INT ")"
    transiciones: "transiciones" ":" "{" reglas "}"
    reglas: regla*
    regla: CNAME "," SIMBOLO "->" CNAME "," SIMBOLO "," DIRECCION
    SIMBOLO: /[a-zA-Z0-9_]/
    DIRECCION: "IZQ" | "DER" | "QUIETO"
    %import common.CNAME
    %import common.INT
    %import common.WS
    %import common.SH_COMMENT
    %ignore WS
    %ignore SH_COMMENT
"""

class TransformadorAST(Transformer):
    def SIMBOLO(self, tok): return str(tok)
    def CNAME(self, tok): return str(tok)
    def INT(self, tok): return int(tok)
    def start(self, items): return items[0]

    def regla(self, items):
        orig, lee, dest, esc, mov = items
        return ReglaAST(orig, lee, dest, esc, Direccion[mov])

    def reglas(self, items): return list(items)
    def subrutina(self, items): return SubrutinaAST(items[0], items[1], items[2])
    def alfabeto(self, items): return set(items)
    def estados(self, items): return set(items)
    def inicial(self, items): return items[0]
    def finales(self, items): return set(items)
    def usa_subrutina(self, items): return InvocacionSubrutinaAST(items[0], items[1])
    def transiciones(self, items): return items[0]

    def maquina(self, items):
        nombre, alf, est, ini, fin = items[:5]
        subrutinas = [item for item in items[5:-1] if isinstance(item, InvocacionSubrutinaAST)]
        return MaquinaAST(nombre, alf, "_", est, ini, fin, subrutinas, items[-1])

    def programa(self, items):
        return ProgramaAST(
            [item for item in items if isinstance(item, SubrutinaAST)],
            [item for item in items if isinstance(item, MaquinaAST)]
        )

def procesar_archivo(ruta_archivo: str) -> ProgramaAST:
    parser = Lark(gramatica_dsl, parser='lalr', transformer=TransformadorAST())
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        return parser.parse(archivo.read())