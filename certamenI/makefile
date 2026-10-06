# Checkear para la variable de entorno Windows_NT
OS ?= $(shell echo %OS% 2>/dev/null) # Fetch %OS% from Windows Shell
ifeq ($(OS),Windows_NT) # Windows confirmado
	IS_WINDOWS := 1
else
	UNAME_S := $(shell uname -s 2>/dev/null) # Conseguir el nombre del OS
	ifeq ($(UNAME_S), Linux)
		IS_UNIX := 1
	else ifeq ($(UNAME_S), Darwin) # MacOS usa Darwin
		IS_UNIX := 1
	else # Fallback, asume que es UNIX
		IS_UNIX := 1
	endif
endif

ifeq ($(IS_WINDOWS),1)
	# Comandos de windows
	RM := del /f /q
	RMDIR := rd /s /q
	MKDIR := mkdir
	CP := copy /y
	EXE_EXT := .exe
else
	# Comandos de UNIX (Linux/MacOS/MSYS2 Git Bash)
	RM := rm -f
	RMDIR := rm -rf
	MKDIR := mkdir -p
	CP := cp
	EXE_EXT := 
endif
.DEFAULT_GOAL := help
.PHONY: all run clean
VENV = venv
ifeq ($(IS_UNIX),1)
	PYTHON = $(VENV)/bin/python3
	PIP = $(VENV)/bin/pip
else ifeq ($(IS_WINDOWS),1)
	PYTHON = $(VENV)/Scripts/python.exe
	PIP = $(VENV)/Scripts/pip.exe
endif
INPUT1 = ./ejemplo.tm
INPUT2 = 1011
help:
	@echo "[VENV] [INPUT] run		Ejecutar script"
	@echo "[VENV] clean			Remover artefactos de build"
	@echo "[VENV]: VENV=venv"
	@echo "[INPUT1]: INPUT1=ejemplo.tm"
	@echo "[INPUT2]: INPUT2=1011"

$(VENV)/bin/activate: requirements.txt
	python -m venv $(VENV)
	$(PIP) install -r requirements.txt
	$(PYTHON) -m py_compile analizador.py interprete.py main.py nodos.py semantica.py

run: $(VENV)/bin/activate
	$(PYTHON) main.py $(INPUT1) $(INPUT2)

clean:
	$(RMDIR) __pycache__ *.pyc
	$(RMDIR) $(VENV)