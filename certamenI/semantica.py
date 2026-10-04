from typing import Dict, Tuple, Set
from nodos import ProgramaAST, Direccion, SubrutinaAST, TablaSimbolos


class AccionTransicion:
    def __init__(self, nuevo_estado: str, nuevo_simbolo: str, movimiento: Direccion):
        self.nuevo_estado = nuevo_estado
        self.nuevo_simbolo = nuevo_simbolo
        self.movimiento = movimiento


class MaquinaProcesada:
    def __init__(
        self,
        nombre: str,
        alfabeto: Set[str],
        simbolo_blanco: str,
        estados: Set[str],
        estado_inicial: str,
        estados_finales: Set[str]
    ):
        self.nombre = nombre
        self.alfabeto = alfabeto
        self.simbolo_blanco = simbolo_blanco
        self.estados = set(estados)
        self.estado_inicial = estado_inicial
        self.estados_finales = set(estados_finales)

        self.tabla_transiciones: Dict[
            Tuple[str, str], AccionTransicion
        ] = {}

        self.tabla_simbolos = TablaSimbolos()

        for estado in self.estados:
            self.tabla_simbolos.agregar_estado(estado)

        for simbolo in self.alfabeto:
            self.tabla_simbolos.agregar_simbolo(simbolo)

    def agregar_transicion(
        self,
        origen: str,
        lee: str,
        accion: AccionTransicion
    ):
        # 1. Validar que los estados existan
        if not self.tabla_simbolos.existe_estado(origen):
            raise ValueError(
                f"Error Semántico: El estado origen '{origen}' "
                f"no fue declarado en la lista de estados."
            )

        if not self.tabla_simbolos.existe_estado(accion.nuevo_estado):
            raise ValueError(
                f"Error Semántico: El estado destino "
                f"'{accion.nuevo_estado}' no fue declarado."
            )

        # Validar determinismo
        clave = (origen, lee)

        if clave in self.tabla_transiciones:
            raise ValueError(
                f"Error Semántico [Determinismo]: "
                f"Transición duplicada para ({origen}, '{lee}')."
            )

        # Validar símbolos del alfabeto
        if not self.tabla_simbolos.existe_simbolo(lee):
            raise ValueError(
                f"Error Semántico: El símbolo leído "
                f"'{lee}' no pertenece al alfabeto."
            )

        if not self.tabla_simbolos.existe_simbolo(accion.nuevo_simbolo):
            raise ValueError(
                f"Error Semántico: El símbolo escrito "
                f"'{accion.nuevo_simbolo}' no pertenece al alfabeto."
            )

        self.tabla_transiciones[clave] = accion


def construir_maquina_compilada(
    ast: ProgramaAST,
    nombre_maquina: str = None
) -> MaquinaProcesada:

    if not ast.maquinas:
        raise ValueError(
            "Error Semántico: No se declaró ninguna máquina."
        )

    # Permite seleccionar una máquina por nombre
    if nombre_maquina is None:
        m_ast = ast.maquinas[0]
    else:
        m_ast = None

        for maquina in ast.maquinas:
            if maquina.nombre == nombre_maquina:
                m_ast = maquina
                break

        if m_ast is None:
            raise ValueError(
                f"Error Semántico: La máquina "
                f"'{nombre_maquina}' no fue declarada."
            )

    #  Validar alfabeto
    if not m_ast.alfabeto:
        raise ValueError(
            "Error Semántico: El alfabeto no puede estar vacío."
        )

    if "_" not in m_ast.alfabeto:
        raise ValueError(
            "Error Semántico: El alfabeto debe incluir "
            "el símbolo blanco '_'."
        )

    # Validar estado inicial
    if m_ast.estado_inicial not in m_ast.estados:
        raise ValueError(
            "Error Semántico: El estado inicial "
            f"'{m_ast.estado_inicial}' no fue declarado."
        )

    # Validar estados finales
    if not m_ast.estados_finales.issubset(m_ast.estados):
        raise ValueError(
            "Error Semántico: Existen estados finales "
            "que no fueron declarados."
        )

    maquina = MaquinaProcesada(
        m_ast.nombre,
        m_ast.alfabeto,
        m_ast.simbolo_blanco,
        m_ast.estados,
        m_ast.estado_inicial,
        m_ast.estados_finales
    )

    # Expandir subrutinas
    for sub_uso in m_ast.subrutinas_usadas:

        sub_decl = next(
            (
                s for s in ast.subrutinas
                if s.nombre == sub_uso.nombre_subrutina
            ),
            None
        )

        if sub_decl:
            _expandir_subrutina_generica(
                maquina,
                sub_decl,
                sub_uso.parametro_entero
            )

        elif sub_uso.nombre_subrutina == "desplazar":
            _expandir_desplazar(
                maquina,
                sub_uso.parametro_entero
            )

        else:
            raise ValueError(
                f"Error Semántico: La subrutina "
                f"'{sub_uso.nombre_subrutina}' "
                f"no ha sido declarada."
            )

    # Cargar transiciones directas
    for r in m_ast.transiciones:
        maquina.agregar_transicion(
            r.estado_origen,
            r.simbolo_leido,
            AccionTransicion(
                r.estado_destino,
                r.simbolo_escrito,
                r.movimiento
            )
        )

    return maquina


def _expandir_subrutina_generica(
    maquina: MaquinaProcesada,
    sub_ast: SubrutinaAST,
    parametro_val: int
):

    if parametro_val <= 0:
        raise ValueError(
            f"Error Semántico: El parámetro entero de la "
            f"subrutina '{sub_ast.nombre}' debe ser mayor que 0."
        )

    param_nombre = sub_ast.parametro_nombre
    val_str = str(parametro_val)

    for regla in sub_ast.reglas:

        origen = regla.estado_origen.replace(
            param_nombre,
            val_str
        )

        destino = regla.estado_destino.replace(
            param_nombre,
            val_str
        )

        lee = regla.simbolo_leido.replace(
            param_nombre,
            val_str
        )

        escribe = regla.simbolo_escrito.replace(
            param_nombre,
            val_str
        )

        maquina.estados.add(origen)
        maquina.estados.add(destino)

        if not maquina.tabla_simbolos.existe_estado(origen):
            maquina.tabla_simbolos.agregar_estado(origen)

        if not maquina.tabla_simbolos.existe_estado(destino):
            maquina.tabla_simbolos.agregar_estado(destino)

        maquina.agregar_transicion(
            origen,
            lee,
            AccionTransicion(
                destino,
                escribe,
                regla.movimiento
            )
        )


def _expandir_desplazar(
    maquina: MaquinaProcesada,
    n: int
):

    if n <= 0:
        raise ValueError(
            "Error Semántico: El parámetro de "
            "desplazar debe ser mayor que 0."
        )

    maquina.estados.add("q_desp_inicio")

    if not maquina.tabla_simbolos.existe_estado("q_desp_inicio"):
        maquina.tabla_simbolos.agregar_estado("q_desp_inicio")

    estado_actual = "q_desp_inicio"

    for i in range(n):

        if i == n - 1:
            sig_estado = maquina.estado_inicial
        else:
            sig_estado = f"q_desp_{i + 1}"

        maquina.estados.add(sig_estado)

        if not maquina.tabla_simbolos.existe_estado(sig_estado):
            maquina.tabla_simbolos.agregar_estado(sig_estado)

        for sym in maquina.alfabeto:

            maquina.agregar_transicion(
                estado_actual,
                sym,
                AccionTransicion(
                    sig_estado,
                    sym,
                    Direccion.DER
                )
            )

        estado_actual = sig_estado

    maquina.estado_inicial = "q_desp_inicio"