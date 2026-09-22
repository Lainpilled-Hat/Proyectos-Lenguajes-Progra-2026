# Tecnología usadas:
- Python
- ply
- ply.yacc
- ply.lex
- Makefile

[Link Canva](https://www.canva.com/design/DAHUWL3BRBo/evR9vjDOjvCdBQYFBQ6leQ/edit)

# Modo de Uso:

En el directorio ./control1, ejecutar el siguiente comando:

```
make [VENV] [INPUT] run
```
Ejemplo de uso:
```
make VENV=lenguajesprogra INPUT=./ejemplo.txt run 
```

Otros comandos:
```
make help
make
make [VENV] clean
```

# Problema:

FUENTE genera o captura tuplas desde el exterior y las inyecta en la topología
OPERADOR recibe tuplas desde uno o más nodos anteriores, las procesa y emite tuplas de salida hacia los nodos siguientes
SUMIDERO recibe tuplas y las consume como destino final (por ejemplo, almacenándolas). Cada operador realiza una transformación diferente (una única tarea) a las tuplas. 

Hay algunos casos en que el procesamiento realizado por un operador es demasiado alto con respecto a los demás del grafo, en dichos casos, el operador puede ser replicado

“Evento" de simulación corresponde al recorrido completo que hace una tupla, desde que es generada por una FUENTE hasta que es consumida por un SUMIDERO, pasando por los OPERADORES intermedios que la transforman.


# Expresiones regulares:
```
|------------|--------------------------------------|--------------------------------------|
| Token      | Expresión Regular                    | Descripción                          |
|------------|--------------------------------------|--------------------------------------|
| Palabras   | FUENTE, OPERADOR, SUMIDERO, CONECTAR,| Declaración de instrucciones         |
| reservadas | A, TIEMPO_SERVICIO, REPLICAS, SIMULAR|                                      |
|------------|--------------------------------------|--------------------------------------|
| ID         | [a-zA-Z_][a-zA-Z0-9_]*               | Identificadores de nodos. Comienzan  |
|            |                                      | con una letra o guión bajo, seguidos |
|            |                                      | de alfanuméricos.                    |
|------------|--------------------------------------|--------------------------------------|
| NUMERO     | \d+                                  | Números enteros positivos.           |
|            |                                      | Representan tiempos de servicio,     |
|            |                                      | réplicas o eventos.                  |
|------------|--------------------------------------|--------------------------------------|
| t_ignore   | [ \t\r]+                             | Ignora: espacios en blanco,          |
|            |                                      | tabulaciones y retornos de carro.    |
|------------|--------------------------------------|--------------------------------------|
| COMENTARIO | \#.*                                 | Comentarios iniciados con # son      |
|            |                                      | ignorados.                           |
|------------|--------------------------------------|--------------------------------------|
| newline    | \n+                                  | Saltos de línea para el conteo de    |
|            |                                      | filass de ejecución                  |
|------------|--------------------------------------|--------------------------------------|
```

# Contenidos:

## Gramática Libre de contexto:
- Análisis Sintáctico - parser.py

```text
programa        -> instrucciones
instrucciones   -> instrucciones instruccion | instruccion
instruccion     -> FUENTE ID
                 | OPERADOR ID TIEMPO_SERVICIO NUMERO
                 | OPERADOR ID TIEMPO_SERVICIO NUMERO REPLICAS NUMERO
                 | SUMIDERO ID
                 | CONECTAR ID A ID
                 | SIMULAR NUMERO
```

## Tabla de simbolos:
- simbolos.py


## Construcción de la Topología:
- grafo.py


## Validación de Reglas Estructurales:
- simulador.py

## Decisión de diseño en réplicas consecutivas

Cuando un nodo se conecta con un operador que tiene varias réplicas, se utiliza un sistema de balanceo **Round-Robin**. Para esto, se usa un contador que va indicando a qué réplica se debe enviar cada evento, utilizando `contador % destino.replicas`. De esta forma, los eventos se van distribuyendo de manera ordenada entre las distintas instancias (instancia-1, instancia-2,...), evitando que todos lleguen a la misma réplica y permitiendo simular una mejor distribución de la carga.

# Ejemplos:

## Ejemplo correcto sin replicas:
- ejemplo.txt
```
FUENTE SensorTemperatura #comentario
OPERADOR FiltroRuido TIEMPO_SERVICIO 10
SUMIDERO BaseDatos
CONECTAR SensorTemperatura A FiltroRuido
CONECTAR FiltroRuido A BaseDatos
SIMULAR 3
```
- Resultado esperado:
```
Topología cargada correctamente.

Tabla de símbolos:
SensorTemperatura: tipo=FUENTE, tiempo=0, replicas=1
FiltroRuido: tipo=OPERADOR, tiempo=10, replicas=1
BaseDatos: tipo=SUMIDERO, tiempo=0, replicas=1

Simulación:

Evento 1: FUENTE SensorTemperatura -> OPERADOR FiltroRuido (T: 10) -> SUMIDERO BaseDatos
Tiempo total acumulado: 10

Evento 2: FUENTE SensorTemperatura -> OPERADOR FiltroRuido (T: 10) -> SUMIDERO BaseDatos
Tiempo total acumulado: 10

Evento 3: FUENTE SensorTemperatura -> OPERADOR FiltroRuido (T: 10) -> SUMIDERO BaseDatos
Tiempo total acumulado: 10
```


## Ejemplo correcto con replicas:
- ejemploreplicas.txt
```
FUENTE f1
OPERADOR op1 TIEMPO_SERVICIO 5 REPLICAS 3
SUMIDERO s1
CONECTAR f1 A op1
CONECTAR op1 A s1
SIMULAR 4
```
- Resultado esperado:
```
Topología cargada correctamente.

Tabla de símbolos:
f1: tipo=FUENTE, tiempo=0, replicas=1
op1: tipo=OPERADOR, tiempo=5, replicas=3
s1: tipo=SUMIDERO, tiempo=0, replicas=1

Simulación:

Evento 1: FUENTE f1 -> OPERADOR op1-1 -> SUMIDERO s1
Tiempo total acumulado: 5

Evento 2: FUENTE f1 -> OPERADOR op1-2 -> SUMIDERO s1
Tiempo total acumulado: 5

Evento 3: FUENTE f1 -> OPERADOR op1-3 -> SUMIDERO s1
Tiempo total acumulado: 5

Evento 4: FUENTE f1 -> OPERADOR op1-1 -> SUMIDERO s1
Tiempo total acumulado: 5

```


## Ejemplo error semántico:
La tabla de símbolos valida que inexistente nunca fue declarado con OPERADOR, deteniendo el programa antes de construir la red.

- errorsemantico.txt
```
FUENTE f1
SUMIDERO s1
CONECTAR f1 A inexistente
SIMULAR 1
```
- Resultado esperado:
```
Error semántico: el nodo 'inexistente' no existe.
```


## Ejemplo error sintáctico:
A la instrucción OPERADOR op1 TIEMPO_SERVICIO le falta el NUMERO entero al final exigido por la GLC.

- errorsintactico.txt
```
FUENTE f1
OPERADOR op1 TIEMPO_SERVICIO
SUMIDERO s1
CONECTAR f1 A s1
SIMULAR 1
```

- Resultado esperado:
```
Error sintáctico: token inesperado 'SUMIDERO' en la línea 3
```

Esta prueba nos hizo ver que el manejo de error esta incorrecto, ya que nos salian 2 errores. Por lo que decidimos que el programa se detendrá al detectar el primer error.


## Ejemplo error léxico:

El analizador léxico (lexer.py) encuentra el símbolo $, el cual no pertenece a ninguna Expresión Regular definida

- errorlexico.txt
```
FUENTE f1
OPERADOR op1 $ TIEMPO_SERVICIO 5
SUMIDERO s1
CONECTAR f1 A op1
CONECTAR op1 A s1
SIMULAR 1
```

- Resultado esperado:
```
Error léxico: carácter inesperado '$' en la línea 2
```


## Ejemplo error sin sumidero:
El simulador detecta que los datos no tienen un lugar a donde llegar para terminar su recorrido, ya que falta el SUMIDERO.

- errorsumidero.txt
```
FUENTE f1
OPERADOR op1 TIEMPO_SERVICIO 5
CONECTAR f1 A op1
SIMULAR 1
```

- Resultado esperado:
```
Topología cargada correctamente.

Tabla de símbolos:
f1: tipo=FUENTE, tiempo=0, replicas=1
op1: tipo=OPERADOR, tiempo=5, replicas=1

Simulación:

Error semántico: la topología debe tener al menos un SUMIDERO.
```


## Prompts dados a la IA:

- explicame como hacer la tarea del archivo adjunto 
- explicame como construir un gráfico de procesamiento 
- revisa si el codigo adjunto cumple con todo lo pedido en el archivo Control I 2026, en caso que no cumpla algo mencionamelo
