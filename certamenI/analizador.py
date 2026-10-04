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


class TransformadorAST(TuringDSLVisitor):

    def visitPrograma(
        self,
        ctx: TuringDSLParser.ProgramaContext
    ):
        subs = []
        maqs = []

        for child in ctx.children:

            if isinstance(
                child,
                TuringDSLParser.SubrutinaContext
            ):
                subs.append(self.visit(child))

            elif isinstance(
                child,
                TuringDSLParser.MaquinaContext
            ):
                maqs.append(self.visit(child))

        return ProgramaAST(subs, maqs)

    def visitSubrutina(
        self,
        ctx: TuringDSLParser.SubrutinaContext
    ):
        nombre = ctx.CNAME(0).getText()
        param = ctx.CNAME(1).getText()
        reglas = self.visit(ctx.reglas())

        return SubrutinaAST(
            nombre,
            param,
            reglas
        )

    def visitMaquina(
        self,
        ctx: TuringDSLParser.MaquinaContext
    ):
        nombre = ctx.CNAME().getText()
        alf = self.visit(ctx.alfabeto())
        est = self.visit(ctx.estados())
        ini = self.visit(ctx.inicial())
        fin = self.visit(ctx.finales())

        subs = [
            self.visit(u)
            for u in ctx.usa_subrutina()
        ]

        trans = self.visit(ctx.transiciones())

        return MaquinaAST(
            nombre,
            alf,
            "_",
            est,
            ini,
            fin,
            subs,
            trans
        )

    def visitAlfabeto(
        self,
        ctx: TuringDSLParser.AlfabetoContext
    ):
        return {
            s.getText()
            for s in ctx.simbolo()
        }

    def visitEstados(
        self,
        ctx: TuringDSLParser.EstadosContext
    ):
        return {
            e.getText()
            for e in ctx.CNAME()
        }

    def visitInicial(
        self,
        ctx: TuringDSLParser.InicialContext
    ):
        return ctx.CNAME().getText()

    def visitFinales(
        self,
        ctx: TuringDSLParser.FinalesContext
    ):
        return {
            e.getText()
            for e in ctx.CNAME()
        }

    def visitUsa_subrutina(
        self,
        ctx: TuringDSLParser.Usa_subrutinaContext
    ):
        return InvocacionSubrutinaAST(
            ctx.CNAME().getText(),
            int(ctx.INT().getText())
        )

    def visitTransiciones(
        self,
        ctx: TuringDSLParser.TransicionesContext
    ):
        return self.visit(ctx.reglas())

    def visitReglas(
        self,
        ctx: TuringDSLParser.ReglasContext
    ):
        return [
            self.visit(r)
            for r in ctx.regla()
        ]

    def visitRegla(
        self,
        ctx: TuringDSLParser.ReglaContext
    ):
        orig = ctx.CNAME(0).getText()
        lee = ctx.simbolo(0).getText()
        dest = ctx.CNAME(1).getText()
        esc = ctx.simbolo(1).getText()
        mov = Direccion[
            ctx.DIRECCION().getText()
        ]

        return ReglaAST(
            orig,
            lee,
            dest,
            esc,
            mov
        )


def procesar_archivo(
    ruta_archivo: str
) -> ProgramaAST:

    input_stream = FileStream(
        ruta_archivo,
        encoding="utf-8"
    )

    lexer = TuringDSLLexer(input_stream)

    errores_lexer = ErrorANTLR()

    lexer.removeErrorListeners()
    lexer.addErrorListener(errores_lexer)

    stream = CommonTokenStream(lexer)

    parser = TuringDSLParser(stream)

    errores_parser = ErrorANTLR()

    parser.removeErrorListeners()
    parser.addErrorListener(errores_parser)

    tree = parser.programa()

    errores = (
        errores_lexer.errores
        + errores_parser.errores
    )

    if errores:
        mensaje = "\n".join(errores)

        raise ValueError(
            "Error de sintaxis en el archivo DSL:\n"
            + mensaje
        )

    visitor = TransformadorAST()

    return visitor.visit(tree)