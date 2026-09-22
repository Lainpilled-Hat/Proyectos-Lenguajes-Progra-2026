.DEFAULT_GOAL := help
.PHONY: run clean
VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
INPUT = ./ejemplo.txt
help:
	@echo "[VENV] [INPUT] run		Ejecutar script"
	@echo "[VENV] clean			Remover artefactos de build"
	@echo "[VENV]: VENV=venv"
	@echo "[INPUT]: INPUT=ejemplo.txt"

run: $(VENV)/bin/activate
	$(PYTHON) main.py $(INPUT)

$(VENV)/bin/activate: requirements.txt
	python -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	rm -rf __pycache__ parsetab.py parser.out
	rm -rf $(VENV)