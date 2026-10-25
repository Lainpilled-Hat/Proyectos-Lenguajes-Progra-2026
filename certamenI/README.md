# Tecnologías usadas:
- Python
- Makefile
- ANTLR


# Modo de Uso:

Desde la carpeta del proyecto, al ejecutar `make`, se muestra la ayuda. Para ejecutar la máquina, usa `make run`. Los valores predeterminados son `ejemplo.tm`, `1011` y `_`:

```
make run [VENV=venv] INPUT1=<archivo.tm> INPUT2=<cinta_inicial> INPUT3=<simbolo_blanco> [INPUT4=<nombre_maquina>]
```
Ejemplo de uso:
```
make run VENV=venv INPUT1=ejemplo.tm INPUT2=1011 INPUT3=_ INPUT4=Sumador
```

Desde el directorio `certamenI`, ejecuta:

```
python main.py <archivo.tm> <cadena> <simbolo_blanco>
python main.py <archivo.tm> <cadena> <simbolo_blanco> <nombre_maquina>
```

Ejemplo de uso:
```
python main.py ejemplo.tm 101 -
python main.py ejemplo.tm 101 - Inversor
```

El blanco no está fijado a `-`: puedes elegir `a`, `m`, `-` u otro carácter válido. La cinta inicial es una cadena de símbolos del alfabeto; no está limitada a
`0` y `1`.

Las subrutinas se invocan por su nombre como llamadas estilo función. Si la
subrutina declara un parámetro entero, se indica entre paréntesis; si no recibe
parámetros, se escribe solo el nombre.

ejemplo:
```
marcar_celdas(3)
preparar_cinta
```
El número entre paréntesis es el argumento de la subrutina. En
`subrutina.tm`, `N` se usa en los nombres `q_paso_N` y `q_fin_N`; por tanto,
`marcar_celdas(1)` genera reglas con `q_paso_1` y `q_fin_1`. La máquina debe
conectar esos mismos estados en sus transiciones.

Otros comandos:
```
make help
make
make clean
```
