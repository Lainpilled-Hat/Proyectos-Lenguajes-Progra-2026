import ply.lex as lex

# Palabras reservadas del lenguaje
reservar = {
    'FUENTE': 'FUENTE',
    'OPERADOR': 'OPERADOR',
    'SUMIDERO': 'SUMIDERO',
    'CONECTAR': 'CONECTAR',
    'A': 'A',
    'TIEMPO_SERVICIO': 'TIEMPO_SERVICIO',
    'REPLICAS': 'REPLICAS',
    'SIMULAR': 'SIMULAR'
}

# Tipos de elementos reconocidos
tokens = [
    'ID',
    'NUMERO'
] + list(reservar.values())

# Reconoce identificador de los nodos
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservar.get(t.value, 'ID')
    return t

# Reconoce numeros int
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\r' # Ignora espacios en blanco, sangrías (Tab) y saltos de línea

# Comentario ignorado #
def t_COMENTARIO(t):
    r'\#.*'
    pass

# Cuenta saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Fin de archivo
def t_eof(t):
    return None

# Error cuando encuentra un caracter no reconocido
def t_error(t):
    raise Exception(f"Error léxico: carácter inesperado '{t.value[0]}' en la línea {t.lexer.lineno}")

lexer = lex.lex()