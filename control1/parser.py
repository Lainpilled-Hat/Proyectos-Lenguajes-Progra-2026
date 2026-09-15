import ply.yacc as yacc
from lexer import tokens
from simbolos import Nodo, TablaSimbolos
from grafo import Grafo

tabla = TablaSimbolos()
grafo = Grafo()
simulacion = 0

def p_programa(p):
    '''programa : instrucciones'''
    p[0] = p[1]

def p_instrucciones_multiple(p):
    '''instrucciones : instrucciones instruccion'''
    p[0] = p[1] + [p[2]]

def p_instrucciones_una(p):
    '''instrucciones : instruccion'''
    p[0] = [p[1]]

def p_instruccion_fuente(p):
    '''instruccion : FUENTE ID'''
    nodo = Nodo(p[2], 'FUENTE')
    tabla.agregar(nodo)
    grafo.agregar_nodo(nodo)
    p[0] = nodo

def p_instruccion_operador(p):
    '''instruccion : OPERADOR ID TIEMPO_SERVICIO NUMERO'''
    nodo = Nodo(p[2], 'OPERADOR', p[4], 1)
    tabla.agregar(nodo)
    grafo.agregar_nodo(nodo)
    p[0] = nodo

def p_instruccion_operador_replicas(p):
    '''instruccion : OPERADOR ID TIEMPO_SERVICIO NUMERO REPLICAS NUMERO'''
    nodo = Nodo(p[2], 'OPERADOR', p[4], p[6])
    tabla.agregar(nodo)
    grafo.agregar_nodo(nodo)
    p[0] = nodo

def p_instruccion_sumidero(p):
    '''instruccion : SUMIDERO ID'''
    nodo = Nodo(p[2], 'SUMIDERO')
    tabla.agregar(nodo)
    grafo.agregar_nodo(nodo)
    p[0] = nodo

def p_instruccion_conectar(p):
    '''instruccion : CONECTAR ID A ID'''
    origen = tabla.obtener(p[2])
    destino = tabla.obtener(p[4])
    grafo.conectar(origen, destino)
    p[0] = None

def p_instruccion_simular(p):
    '''instruccion : SIMULAR NUMERO'''
    global simulacion
    simulacion = p[2]
    p[0] = None

def p_error(p):
    if p:
        # Al usar raise Exception, detenemos el parser inmediatamente en el primer error
        raise Exception(f"Error sintáctico: token inesperado '{p.value}' en la línea {p.lineno}")
    else:
        raise Exception("Error sintáctico: fin inesperado de archivo")
    
parser = yacc.yacc()