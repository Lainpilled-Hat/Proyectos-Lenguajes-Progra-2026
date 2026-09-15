import ply.lex as lex

# Palabras reservadas del DSL
reserved = {
    'FUENTE': 'FUENTE',
    'OPERADOR': 'OPERADOR',
    'SUMIDERO': 'SUMIDERO',
    'CONECTAR': 'CONECTAR',
    'A': 'A',
    'TIEMPO_SERVICIO': 'TIEMPO_SERVICIO',
    'REPLICAS': 'REPLICAS',
    'SIMULAR': 'SIMULAR'
}

tokens = [
    'ID',
    'NUMERO'
] + list(reserved.values())

# Identificadores (nombres de variables/nodos)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Números enteros
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\r'

# Manejo de comentarios
def t_COMENTARIO(t):
    r'\#.*'
    pass

# Saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Fin de archivo
def t_eof(t):
    return None

# Manejo de errores léxicos
def t_error(t):
    raise Exception(f"Error léxico: carácter inesperado '{t.value[0]}' en la línea {t.lexer.lineno}")

lexer = lex.lex()