# Generated from TuringDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TuringDSLParser import TuringDSLParser
else:
    from TuringDSLParser import TuringDSLParser

# This class defines a complete listener for a parse tree produced by TuringDSLParser.
class TuringDSLListener(ParseTreeListener):

    # Enter a parse tree produced by TuringDSLParser#programa.
    def enterPrograma(self, ctx:TuringDSLParser.ProgramaContext):
        pass

    # Exit a parse tree produced by TuringDSLParser#programa.
    def exitPrograma(self, ctx:TuringDSLParser.ProgramaContext):
        pass


    # Enter a parse tree produced by TuringDSLParser#subrutina.
    def enterSubrutina(self, ctx:TuringDSLParser.SubrutinaContext):
        pass

    # Exit a parse tree produced by TuringDSLParser#subrutina.
    def exitSubrutina(self, ctx:TuringDSLParser.SubrutinaContext):
        pass


    # Enter a parse tree produced by TuringDSLParser#maquina.
    def enterMaquina(self, ctx:TuringDSLParser.MaquinaContext):
        pass

    # Exit a parse tree produced by TuringDSLParser#maquina.
    def exitMaquina(self, ctx:TuringDSLParser.MaquinaContext):
        pass


    # Enter a parse tree produced by TuringDSLParser#alfabeto.
    def enterAlfabeto(self, ctx:TuringDSLParser.AlfabetoContext):
        pass

    # Exit a parse tree produced by TuringDSLParser#alfabeto.
    def exitAlfabeto(self, ctx:TuringDSLParser.AlfabetoContext):
        pass


    # Enter a parse tree produced by TuringDSLParser#estados.
    def enterEstados(self, ctx:TuringDSLParser.EstadosContext):
        pass

    # Exit a parse tree produced by TuringDSLParser#estados.
    def exitEstados(self, ctx:TuringDSLParser.EstadosContext):
        pass


    # Enter a parse tree produced by TuringDSLParser#inicial.
    def enterInicial(self, ctx:TuringDSLParser.InicialContext):
        pass

    # Exit a parse tree produced by TuringDSLParser#inicial.
    def exitInicial(self, ctx:TuringDSLParser.InicialContext):
        pass


    # Enter a parse tree produced by TuringDSLParser#finales.
    def enterFinales(self, ctx:TuringDSLParser.FinalesContext):
        pass

    # Exit a parse tree produced by TuringDSLParser#finales.
    def exitFinales(self, ctx:TuringDSLParser.FinalesContext):
        pass


    # Enter a parse tree produced by TuringDSLParser#usa_subrutina.
    def enterUsa_subrutina(self, ctx:TuringDSLParser.Usa_subrutinaContext):
        pass

    # Exit a parse tree produced by TuringDSLParser#usa_subrutina.
    def exitUsa_subrutina(self, ctx:TuringDSLParser.Usa_subrutinaContext):
        pass


    # Enter a parse tree produced by TuringDSLParser#transiciones.
    def enterTransiciones(self, ctx:TuringDSLParser.TransicionesContext):
        pass

    # Exit a parse tree produced by TuringDSLParser#transiciones.
    def exitTransiciones(self, ctx:TuringDSLParser.TransicionesContext):
        pass


    # Enter a parse tree produced by TuringDSLParser#reglas.
    def enterReglas(self, ctx:TuringDSLParser.ReglasContext):
        pass

    # Exit a parse tree produced by TuringDSLParser#reglas.
    def exitReglas(self, ctx:TuringDSLParser.ReglasContext):
        pass


    # Enter a parse tree produced by TuringDSLParser#regla.
    def enterRegla(self, ctx:TuringDSLParser.ReglaContext):
        pass

    # Exit a parse tree produced by TuringDSLParser#regla.
    def exitRegla(self, ctx:TuringDSLParser.ReglaContext):
        pass


    # Enter a parse tree produced by TuringDSLParser#simbolo.
    def enterSimbolo(self, ctx:TuringDSLParser.SimboloContext):
        pass

    # Exit a parse tree produced by TuringDSLParser#simbolo.
    def exitSimbolo(self, ctx:TuringDSLParser.SimboloContext):
        pass



del TuringDSLParser