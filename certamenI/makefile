.DEFAULT_GOAL := help
.PHONY: all run clean
VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
INPUT1 = ./ejemplo.tm
INPUT2 = 1011
help:
	@echo "[VENV] [INPUT1] [INPUT2] run		Ejecutar script"
	@echo "[VENV] clean			Remover artefactos de build"
	@echo "[VENV]: VENV=venv"
	@echo "[INPUT1]: INPUT1=ejemplo.tm"
	@echo "[INPUT2]: 1011"
	
$(VENV)/bin/activate: requirements.txt
	python -m venv $(VENV)
	$(PIP) install -r requirements.txt
	$(PYTHON) -m py_compile analizador.py interprete.py main.py nodos.py semantica.py

run: $(VENV)/bin/activate
	$(PYTHON) main.py $(INPUT1) $(INPUT2)

clean:
	rm -rf __pycache__ *.pyc
	rm -rf $(VENV)