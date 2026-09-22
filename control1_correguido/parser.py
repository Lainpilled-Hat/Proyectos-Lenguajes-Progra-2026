import ply.yacc as yacc
from lexer import tokens
from simbolos import Nodo, TablaSimbolos
from grafo import Grafo

tabla = TablaSimbolos() # Tabla, se guardan los nodos declarados
grafo = Grafo() # Grafo que representa las conexiones entre los nodos
simulacion = 0 # Cantidad de eventos que se deben simular

def p_programa(p):
    '''programa : instrucciones'''
    p[0] = p[1] # El programa esta formado por todas las instrucciones del archivo

def p_instrucciones_multiple(p):
    '''instrucciones : instrucciones instruccion'''
    p[0] = p[1] + [p[2]] # Puede tener varias instrucciones

def p_instrucciones_una(p):
    '''instrucciones : instruccion'''
    p[0] = [p[1]] #  Permite que el programa tenga una sola instrucción

def p_instruccion_fuente(p):
    '''instruccion : FUENTE ID'''

    # Crea una fuente y la guarda en la tabla de símbolos y en el grafo
    nodo = Nodo(p[2], 'FUENTE')
    tabla.agregar(nodo)
    grafo.agregar_nodo(nodo)
    p[0] = nodo

def p_instruccion_operador(p):
    '''instruccion : OPERADOR ID TIEMPO_SERVICIO NUMERO'''

    # Crea un operador con un tiempo de servicio y una sola réplica
    nodo = Nodo(p[2], 'OPERADOR', p[4], 1)
    tabla.agregar(nodo)
    grafo.agregar_nodo(nodo)
    p[0] = nodo

def p_instruccion_operador_replicas(p):
    '''instruccion : OPERADOR ID TIEMPO_SERVICIO NUMERO REPLICAS NUMERO'''

    # Crea un operador, se indica su tiempo de servicio y número de réplicas
    nodo = Nodo(p[2], 'OPERADOR', p[4], p[6])
    tabla.agregar(nodo)
    grafo.agregar_nodo(nodo)
    p[0] = nodo

def p_instruccion_sumidero(p):
    '''instruccion : SUMIDERO ID'''

     # Crea un sumidero y lo agrega a la tabla y al grafo
    nodo = Nodo(p[2], 'SUMIDERO')
    tabla.agregar(nodo)
    grafo.agregar_nodo(nodo)
    p[0] = nodo

def p_instruccion_conectar(p):
    '''instruccion : CONECTAR ID A ID'''

     # Busca los nodos que se quieren conectar
    origen = tabla.obtener(p[2])
    destino = tabla.obtener(p[4])
    grafo.conectar(origen, destino)  # Agrega la conexión
    p[0] = None

def p_instruccion_simular(p):
    '''instruccion : SIMULAR NUMERO'''

    # Guarda el número de simulaciones
    global simulacion
    simulacion = p[2]
    p[0] = None

def p_error(p):
    if p:
        # Al usar raise Exception, detenemos el parser inmediatamente en el primer error
        raise Exception(f"Error sintáctico: token inesperado '{p.value}' en la línea {p.lineno}")
    else:
        raise Exception("Error sintáctico: fin inesperado de archivo") # El archivo termina antes de completar una instrucción
    
parser = yacc.yacc() # Crea el analizador 