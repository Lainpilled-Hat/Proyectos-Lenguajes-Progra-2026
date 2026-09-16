from typing import Dict, Tuple, Set
from nodos import ProgramaAST, Direccion

class AccionTransicion:
    def __init__(self, nuevo_estado: str, nuevo_simbolo: str, movimiento: Direccion):
        self.nuevo_estado = nuevo_estado
        self.nuevo_simbolo = nuevo_simbolo
        self.movimiento = movimiento

class MaquinaProcesada:
    def __init__(self, nombre: str, alfabeto: Set[str], simbolo_blanco: str, estados: Set[str], estado_inicial: str, estados_finales: Set[str]):
        self.nombre = nombre
        self.alfabeto = alfabeto
        self.simbolo_blanco = simbolo_blanco
        self.estados = set(estados)
        self.estado_inicial = estado_inicial
        self.estados_finales = estados_finales
        self.tabla_transiciones: Dict[Tuple[str, str], AccionTransicion] = {}

    def agregar_transicion(self, origen: str, lee: str, accion: AccionTransicion):
        clave = (origen, lee)
        if clave in self.tabla_transiciones:
            raise ValueError(f"Error Semántico [Determinismo]: Transición duplicada para ({origen}, '{lee}')")
        if lee not in self.alfabeto or accion.nuevo_simbolo not in self.alfabeto:
            raise ValueError(f"Error Semántico: Símbolo '{lee}' o '{accion.nuevo_simbolo}' no pertenece al alfabeto.")
        self.tabla_transiciones[clave] = accion

def construir_maquina_compilada(ast: ProgramaAST, nombre_maquina: str = None) -> MaquinaProcesada:
    m_ast = ast.maquinas[0] if not nombre_maquina else next(m for m in ast.maquinas if m.nombre == nombre_maquina)
    
    if m_ast.estado_inicial not in m_ast.estados:
        raise ValueError("Estado inicial no fue declarado.")
    if not m_ast.estados_finales.issubset(m_ast.estados):
        raise ValueError("Existen estados finales no declarados.")

    maquina = MaquinaProcesada(
        m_ast.nombre, m_ast.alfabeto, m_ast.simbolo_blanco, 
        m_ast.estados, m_ast.estado_inicial, m_ast.estados_finales
    )

    for sub in m_ast.subrutinas_usadas:
        if sub.nombre_subrutina == "desplazar":
            _expandir_desplazar(maquina, sub.parametro_entero)

    for r in m_ast.transiciones:
        maquina.agregar_transicion(
            r.estado_origen, r.simbolo_leido, 
            AccionTransicion(r.estado_destino, r.simbolo_escrito, r.movimiento)
        )

    return maquina

def _expandir_desplazar(maquina: MaquinaProcesada, n: int):
    maquina.estados.add("q_desp_inicio")
    estado_actual = "q_desp_inicio"
    for i in range(n):
        sig_estado = maquina.estado_inicial if i == n - 1 else f"q_desp_{i+1}"
        maquina.estados.add(sig_estado)
        for sym in maquina.alfabeto:
            maquina.agregar_transicion(estado_actual, sym, AccionTransicion(sig_estado, sym, Direccion.DER))
        estado_actual = sig_estado
    maquina.estado_inicial = "q_desp_inicio"