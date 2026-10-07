from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from TuringDSLLexer import TuringDSLLexer
from TuringDSLParser import TuringDSLParser
from TuringDSLVisitor import TuringDSLVisitor

from nodos import (
    Direccion,
    ReglaAST,
    InvocacionSubrutinaAST,
    SubrutinaAST,
    MaquinaAST,
    ProgramaAST
)

# Almacena los errores
class ErrorANTLR(ErrorListener):

    def __init__(self):
        super().__init__()
        self.errores = []

    def syntaxError(
        self,
        recognizer,
        offendingSymbol,
        line,
        column,
        msg,
        e
    ):
        self.errores.append(
            f"Línea {line}, columna {column}: {msg}"
        )


# Recorre el árbol sintáctico
class TransformadorAST(TuringDSLVisitor):

    def visitPrograma(self, ctx):
        return self.programa(ctx)

    def visitSubrutina(self, ctx):
        return self.subrutina(ctx)

    def visitMaquina(self, ctx):
        return self.maquina(ctx)

    def visitAlfabeto(self, ctx):
        return self.alfabeto(ctx)

    def visitEstados(self, ctx):
        return self.estados(ctx)

    def visitInicial(self, ctx):
        return self.inicial(ctx)

    def visitFinales(self, ctx):
        return self.finales(ctx)

    def visitUsa_subrutina(self, ctx):
        return self.usa_subrutina(ctx)

    def visitTransiciones(self, ctx):
        return self.transiciones(ctx)

    def visitReglas(self, ctx):
        return self.reglas(ctx)

    def visitRegla(self, ctx):
        return self.regla(ctx)

    # Procesa el programa
    def programa(
        self,
        ctx: TuringDSLParser.ProgramaContext
    ):
        # Listas para almacenar subrutinas y máquinas
        subs = []
        maqs = []

        # Recorre los elementos que forman el programa
        for i in ctx.children:
            # Si el elemento es una subrutina, se agrega a la lista
            if isinstance(
                i,
                TuringDSLParser.SubrutinaContext
            ):
                subs.append(self.visit(i))

            # Si el elemento es una maquina, se agrega a la lista
            elif isinstance(
                i,
                TuringDSLParser.MaquinaContext
            ):
                maqs.append(self.visit(i))
 
        return ProgramaAST(subs, maqs) # Devuelve el AST del programa

    # Definición de una subrutina
    def subrutina(
        self,
        ctx: TuringDSLParser.SubrutinaContext
    ):
        nombre = ctx.CNAME(0).getText() # Nombre de la subrutina
        param = ctx.CNAME(1).getText() # Nombre del parámetro
        reglas = self.visit(ctx.reglas()) #  Reglas que forman la subrutina

         # Construye el nodo AST
        return SubrutinaAST(
            nombre,
            param,
            reglas
        )

    # Definición de una máquina
    def maquina(
        self,
        ctx: TuringDSLParser.MaquinaContext
    ):
        nombre = ctx.CNAME().getText() # Nombre de la máquina
        alf = self.visit(ctx.alfabeto()) # Alfabeto de la máquina
        est = self.visit(ctx.estados()) # Estados de la máquina
        ini = self.visit(ctx.inicial()) # Estado inicial de la máquina
        fin = self.visit(ctx.finales()) # Estados finales de la máquina

        # Subrutinas utilizadas por la máquina
        subs = [
            self.visit(u)
            for u in ctx.usa_subrutina()
        ]

        trans = self.visit(ctx.transiciones())  # Transiciones de la máquina

        # Construye el nodo AST de la máquina
        return MaquinaAST(
            nombre,
            alf,
            "_", # Símbolo blanco
            est,
            ini,
            fin,
            subs,
            trans
        )

    # Alfabeto de la máquina
    def alfabeto(
        self,
        ctx: TuringDSLParser.AlfabetoContext
    ):
        # Obtiene todos los símbolos declarados y los almacena
        return {
            s.getText()
            for s in ctx.simbolo()
        }

    # Estados declarados de la máquina
    def estados(
        self,
        ctx: TuringDSLParser.EstadosContext
    ):
        return {
            e.getText()
            for e in ctx.CNAME()
        }

    # Estado inicial de la máquina
    def inicial(
        self,
        ctx: TuringDSLParser.InicialContext
    ):
        return ctx.CNAME().getText()  # Devuelve el nombre del estado inicial

    # Estados finales de la máquina
    def finales(
        self,
        ctx: TuringDSLParser.FinalesContext
    ):
        return {
            e.getText()
            for e in ctx.CNAME()
        }

    # Uso de una subrutina
    def usa_subrutina(
        self,
        ctx: TuringDSLParser.Usa_subrutinaContext
    ):
        # Obtiene el nombre de la subrutina
        return InvocacionSubrutinaAST(
            ctx.CNAME().getText(),
            int(ctx.INT().getText())
        )

    # Transiciones de una máquina
    def transiciones(
        self,
        ctx: TuringDSLParser.TransicionesContext
    ):
        return self.visit(ctx.reglas())

    # Reglas de transición de una máquina
    def reglas(
        self,
        ctx: TuringDSLParser.ReglasContext
    ):
        return [
            self.visit(r)
            for r in ctx.regla()
        ]

    # Regla de transición individual
    def regla(
        self,
        ctx: TuringDSLParser.ReglaContext
    ):
        orig = ctx.CNAME(0).getText() # Estado de origen
        lee = ctx.simbolo(0).getText() # Símbolo que se lee
        dest = ctx.CNAME(1).getText() # Estado de destino
        esc = ctx.simbolo(1).getText() # Símbolo que se escribe en la cinta

        # Busca dentro del Enum Direccion el elemento que coincide con el texto de la dirección obtenida 
        mov = Direccion[
            ctx.DIRECCION().getText() 
        ]
        # Construye el nodo AST de la regla
        return ReglaAST(
            orig,
            lee,
            dest,
            esc,
            mov
        )

# Procesa un archivo .tm y lo devuelve como AST
def procesar_archivo(
    ruta_archivo: str
) -> ProgramaAST:

    # Abre el archivo
    input_stream = FileStream(
        ruta_archivo,
        encoding="utf-8"
    )

    lexer = TuringDSLLexer(input_stream) # Lexer de ANTLR para reconocer los token

    # Capturar errores léxicos
    errores_lexer = ErrorANTLR() 
    lexer.removeErrorListeners()
    lexer.addErrorListener(errores_lexer)

    stream = CommonTokenStream(lexer) # Crea el flujo de tokens generado por el lexer

    parser = TuringDSLParser(stream) # Crea el parser utilizando los tokens

     # Capturar errores sintácticos
    errores_parser = ErrorANTLR()
    parser.removeErrorListeners()
    parser.addErrorListener(errores_parser)

    tree = parser.programa() # Comienza el análisis desde la regla inicial

    # Junta los errores léxicos y sintácticos.
    errores = (
        errores_lexer.errores
        + errores_parser.errores
    )

    # Informa error
    if errores:
        mensaje = "\n".join(errores)

        raise ValueError(
            "Error de sintaxis en el archivo DSL:\n"
            + mensaje
        )

    visitor = TransformadorAST() # Crea el "Visitor" que recorrerá el árbol

    return visitor.visit(tree) # Convierte el árbol sintáctico en AST