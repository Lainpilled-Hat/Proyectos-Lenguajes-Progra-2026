import re
from typing import Dict, Tuple, Set, Optional
from nodos import ProgramaAST, Direccion, SubrutinaAST, TablaSimbolos

# Acción de transición
class AccionTransicion:
    def __init__(self, nuevo_estado: str, nuevo_simbolo: str, movimiento: Direccion):
        self.nuevo_estado = nuevo_estado
        self.nuevo_simbolo = nuevo_simbolo
        self.movimiento = movimiento

# Representa una máquina de Turing procesada y lista para la simulación
class MaquinaProcesada:
    def __init__(
        self, # instancia actual de la clase
        nombre: str, #nombre de la máquina
        alfabeto: Set[str], # conjunto de símbolos del alfabeto
        simbolo_blanco: str, # símbolo que representa el espacio en blanco en la cinta
        estados: Set[str], # conjunto de estados
        estado_inicial: str, # estado inicial
        estados_finales: Set[str] # conjunto de estados finales
    ):
        self.nombre = nombre
        self.alfabeto = alfabeto
        self.simbolo_blanco = simbolo_blanco
        self.estados = set(estados)
        self.estado_inicial = estado_inicial
        self.estados_finales = set(estados_finales)

        # Tabla donde se almacenarán las transiciones
        self.tabla_transiciones: Dict[
            Tuple[str, str], AccionTransicion
        ] = {}

        self.tabla_simbolos = TablaSimbolos()

        for estado in self.estados:
            self.tabla_simbolos.agregar_estado(estado)

        for simbolo in self.alfabeto:
            self.tabla_simbolos.agregar_simbolo(simbolo)

    # Método para agregar una transición
    def agregar_transicion(
        self,
        origen: str,
        lee: str,
        accion: AccionTransicion
    ):
        # Validar que el estado origen exista
        if not self.tabla_simbolos.existe_estado(origen):
            raise ValueError(
                f"Error Semántico: El estado origen '{origen}' "
                f"no fue declarado en la lista de estados."
            )
        
        # Validar que el estado destino exista
        if not self.tabla_simbolos.existe_estado(accion.nuevo_estado):
            raise ValueError(
                f"Error Semántico: El estado destino "
                f"'{accion.nuevo_estado}' no fue declarado."
            )

        # Validar determinismo
        clave = (origen, lee) # Crea la clave usando el estado de origen y el simbolo leído

        # Comprueba si ya existe una transición con esa clave
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
        
        # Validar que el símbolo escrito pertenezca al alfabeto
        if not self.tabla_simbolos.existe_simbolo(accion.nuevo_simbolo):
            raise ValueError(
                f"Error Semántico: El símbolo escrito "
                f"'{accion.nuevo_simbolo}' no pertenece al alfabeto."
            )

        self.tabla_transiciones[clave] = accion

# Construye una máquina procesada
def construir_maquina_compilada(
    ast: ProgramaAST, # Árbol sintáctico
    nombre_maquina: Optional[str] = None,
    simbolo_blanco: str = "_" # Define "_" como símbolo blanco por defecto
) -> MaquinaProcesada: # Se retorna una máquina procesada

    # ERROR: No se declaró ninguna máquina
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

        # Error: La máquina especificada no fue declarada
        if m_ast is None:
            raise ValueError(
                f"Error Semántico: La máquina "
                f"'{nombre_maquina}' no fue declarada."
            )

    # Error: cuando no hay símbolos en el alfabeto
    if not m_ast.alfabeto:
        raise ValueError(
            "Error Semántico: El alfabeto no puede estar vacío."
        )

     # Error: cuando el símbolo blanco tenga exactamente un carácter
    if len(simbolo_blanco) != 1:
        raise ValueError(
            "Error Semántico: El símbolo blanco debe ser "
            "exactamente un carácter."
        )

     # Error: cuando el estado inicial no esté declarado
    if m_ast.estado_inicial not in m_ast.estados:
        raise ValueError(
            "Error Semántico: El estado inicial "
            f"'{m_ast.estado_inicial}' no fue declarado."
        )

     # Error: cuando los estados finales no estén declarados
    if not m_ast.estados_finales.issubset(m_ast.estados):
        raise ValueError(
            "Error Semántico: Existen estados finales "
            "que no fueron declarados."
        )

    alfabeto = (m_ast.alfabeto - {"_"}) | {simbolo_blanco}  # Reemplaza "_" del alfabeto por el símbolo blanco definido

   # Crea una nueva máquina procesada
    maquina = MaquinaProcesada(
        m_ast.nombre,
        alfabeto,
        simbolo_blanco,
        m_ast.estados,
        m_ast.estado_inicial,
        m_ast.estados_finales
    )

    # Recorre las subrutinas utilizadas por la máquina
    for sub_uso in m_ast.subrutinas_usadas:
        sub_decl = next(  # Busca la declaración de la subrutina utilizada
            ( 
                s for s in ast.subrutinas # Recorre todas las subrutinas del programa
                if s.nombre == sub_uso.nombre_subrutina # Hasta encontrar la que coincida
            ),
            None # Si no se encuentra, devuelve None
        )

        # Si se encuentra la subrutina, se valida el uso de parámetros
        if sub_decl:
            if sub_decl.parametro_nombre is None: # Si la subrutina no tiene parámetro
                if sub_uso.parametro_entero is not None: # Pero se le paso un parámetro al invocarla, genera error
                    raise ValueError(
                        f"Error Semántico: La subrutina "
                        f"'{sub_decl.nombre}' no recibe parámetros."
                    )
            elif sub_uso.parametro_entero is None: # Si la subrutina si tiene parámetro y no se entrego, genera error
                raise ValueError(
                    f"Error Semántico: La subrutina "
                    f"'{sub_decl.nombre}' requiere un parámetro entero."
                )

             # Toma las reglas de la subrutina y reemplaza el parámetro por el valor entregado
            _expandir_subrutina_generica(
                maquina,
                sub_decl,
                sub_uso.parametro_entero,
                simbolo_blanco
            )

        # Subrutina "desplazar"
        elif sub_uso.nombre_subrutina == "desplazar":
            if sub_uso.parametro_entero is None: # Si no se entrego un parámetro a la subrutina desplazar, genera error
                raise ValueError(
                    "Error Semántico: La subrutina "
                    "'desplazar' requiere un parámetro entero."
                )
            # Expande la subrutina agregando transiciones a la máquina
            _expandir_desplazar(
                maquina,
                sub_uso.parametro_entero
            )

        # Si la subrutina no fue encontrada, genera error 
        else:
            raise ValueError(
                f"Error Semántico: La subrutina "
                f"'{sub_uso.nombre_subrutina}' "
                f"no ha sido declarada."
            )

    # Cargar transiciones de la maquina
    for r in m_ast.transiciones:
        maquina.agregar_transicion(   # Agrega cada transición a la máquina
            r.estado_origen, # Estado desde donde comienza la transición
            _resolver_simbolo_blanco(r.simbolo_leido, simbolo_blanco), # Se remplaza "BLANCO" por el símbolo blanco real
                r.movimiento

            # Acción que se debe realizar
            AccionTransicion(
                r.estado_destino, # Estado al que debe cambiar la máquina
                _resolver_simbolo_blanco(r.simbolo_escrito, simbolo_blanco),  # Se remplaza "BLANCO" por el símbolo blanco real
            )
        )

    return maquina

# Expande una subrutina 
def _expandir_subrutina_generica(
    maquina: MaquinaProcesada, # Máquina a la que se agregarán las transiciones
    sub_ast: SubrutinaAST, # Declaración de la subrutina
    parametro_val: Optional[int], # Valor del parámetro entero entregado al invocar la subrutina
    simbolo_blanco: str # Símbolo que representa el espacio en blanco en la cinta
):

    # Comprueba si existe un parámetro y si su valor es menor o igual a cero
    if parametro_val is not None and parametro_val <= 0:
        raise ValueError(
            f"Error Semántico: El parámetro entero de la "
            f"subrutina '{sub_ast.nombre}' debe ser mayor que 0."
        )

    param_nombre = sub_ast.parametro_nombre # Obtiene el nombre del parámetro definido en la subrutina
    val_str = str(parametro_val) if parametro_val is not None else "" # Convierte el valor entero recibido a texto, si no hay utiliza cadena vacia

    # Recorre las reglas de la subrutina 
    for regla in sub_ast.reglas:
        # Comprueba si la subrutina tiene un parámetro
        if param_nombre is not None:
            # Reemplaza el parámetro dentro del estado de origen
            origen = _sustituir_parametro(
                regla.estado_origen,
                param_nombre,
                val_str
            )
            # Reemplaza el parámetro dentro del estado de destino
            destino = _sustituir_parametro(
                regla.estado_destino,
                param_nombre,
                val_str
            )

            # Reemplaza el parámetro dentro del símbolo leído
            lee = _sustituir_parametro(
                regla.simbolo_leido,
                param_nombre,
                val_str
            )

            # Reemplaza el parámetro dentro del símbolo escrito
            escribe = _sustituir_parametro(
                regla.simbolo_escrito,
                param_nombre,
                val_str
            )

        # Si la subrutina no tiene parámetro
        else:
            # Utiliza directamente los valores de la regla sin sustitución
            origen = regla.estado_origen
            destino = regla.estado_destino 
            lee = regla.simbolo_leido
            escribe = regla.simbolo_escrito

        maquina.estados.add(origen) # Agrega el estado de origen a los estados de la máquina.
        maquina.estados.add(destino) # Agrega el estado de destino a los estados de la máquina.

        # Verifica si los estados ya existen en la tabla de símbolos, si no, los agrega
        if not maquina.tabla_simbolos.existe_estado(origen):
            maquina.tabla_simbolos.agregar_estado(origen)

        # Verifica si el estado de destino ya existe en la tabla de símbolos, si no, lo agrega
        if not maquina.tabla_simbolos.existe_estado(destino):
            maquina.tabla_simbolos.agregar_estado(destino)

        # Agrega la regla de la subrutina como una transición 
        maquina.agregar_transicion(
            # Origen de la transición, símbolo leído y acción a realizar
            origen,
            _resolver_simbolo_blanco(lee, simbolo_blanco),
            AccionTransicion(
                destino,
                _resolver_simbolo_blanco(escribe, simbolo_blanco),
                regla.movimiento
            )
        )

# Devuelve el símbolo blanco real
def _resolver_simbolo_blanco(simbolo: str, simbolo_blanco: str) -> str:
    return simbolo_blanco if simbolo == "BLANCO" else simbolo

# Reemplaza un parámetro dentro de un texto
def _sustituir_parametro(
    texto: str,
    nombre_parametro: str,
    valor: str
) -> str:
    patron = rf"(?<![A-Za-z0-9]){re.escape(nombre_parametro)}(?![A-Za-z0-9])" # ER para buscar el nombre del parámetro
    return re.sub(patron, valor, texto) # Busca el parámetro dentro del texto y lo reemplaza por su valor

# Expande la subrutina especial "desplazar"
def _expandir_desplazar(
    maquina: MaquinaProcesada,
    n: int
):
    # Comprueba que el número de desplazamientos sea mayor que cero, si no, genera un error
    if n <= 0:
        raise ValueError(
            "Error Semántico: El parámetro de "
            "desplazar debe ser mayor que 0."
        )

    maquina.estados.add("q_desp_inicio") # Agrega el estado inicial generado para la subrutina

    # Comprueba si ese estado ya está en la tabla de símbolos
    if not maquina.tabla_simbolos.existe_estado("q_desp_inicio"):
        maquina.tabla_simbolos.agregar_estado("q_desp_inicio") # Si no existe, lo agrega

    estado_actual = "q_desp_inicio" # Estado actual desde el cual comeienza el desplazamiento

    # Repite el proceso tantas veces como indique n
    for i in range(n):
        # Comprueba si es la última repetición
        if i == n - 1:
            sig_estado = maquina.estado_inicial # Si es la última, el siguiente estado será el estado inicial de la máquina
        # Si todavía no es la última repetición
        else:
            sig_estado = f"q_desp_{i + 1}" # Genera un nombre para el siguiente desplazamiento

        maquina.estados.add(sig_estado) # Agrega el siguiente estado al conjunto de estados

        # Comprueba si el siguiente estado ya está en la tabla de símbolos
        if not maquina.tabla_simbolos.existe_estado(sig_estado):
            maquina.tabla_simbolos.agregar_estado(sig_estado) # Si no existe, lo agrega

        # Recorre todos los símbolos del alfabeto
        for sym in maquina.alfabeto:
            # Agrega una transición para cada símbolo del alfabeto
            maquina.agregar_transicion(
                estado_actual,
                sym, # Símbolo que se está leyendo
                AccionTransicion(  # Acción que realizará la máquina
                    sig_estado,
                    sym,
                    Direccion.DER
                )
            )

        estado_actual = sig_estado # Actualiza el estado actual para la siguiente iteración

    maquina.estado_inicial = "q_desp_inicio" # Cambia el estado inicial de la máquina