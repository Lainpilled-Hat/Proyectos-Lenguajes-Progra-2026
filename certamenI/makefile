.PHONY: all run clean

all:
	python -m py_compile analizador.py interprete.py main.py nodos.py semantica.py

run: all
	python main.py ejemplo.tm 1011

clean:
	rm -rf __pycache__ *.pyc