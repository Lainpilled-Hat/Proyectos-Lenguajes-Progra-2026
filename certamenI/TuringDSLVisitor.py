# Generated from TuringDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TuringDSLParser import TuringDSLParser
else:
    from TuringDSLParser import TuringDSLParser

# This class defines a complete generic visitor for a parse tree produced by TuringDSLParser.

class TuringDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TuringDSLParser#programa.
    def visitPrograma(self, ctx:TuringDSLParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuringDSLParser#subrutina.
    def visitSubrutina(self, ctx:TuringDSLParser.SubrutinaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuringDSLParser#maquina.
    def visitMaquina(self, ctx:TuringDSLParser.MaquinaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuringDSLParser#alfabeto.
    def visitAlfabeto(self, ctx:TuringDSLParser.AlfabetoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuringDSLParser#estados.
    def visitEstados(self, ctx:TuringDSLParser.EstadosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuringDSLParser#inicial.
    def visitInicial(self, ctx:TuringDSLParser.InicialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuringDSLParser#finales.
    def visitFinales(self, ctx:TuringDSLParser.FinalesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuringDSLParser#usa_subrutina.
    def visitUsa_subrutina(self, ctx:TuringDSLParser.Usa_subrutinaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuringDSLParser#transiciones.
    def visitTransiciones(self, ctx:TuringDSLParser.TransicionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuringDSLParser#reglas.
    def visitReglas(self, ctx:TuringDSLParser.ReglasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuringDSLParser#regla.
    def visitRegla(self, ctx:TuringDSLParser.ReglaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TuringDSLParser#simbolo.
    def visitSimbolo(self, ctx:TuringDSLParser.SimboloContext):
        return self.visitChildren(ctx)



del TuringDSLParser