# Generated from TuringDSL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,20,122,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,4,0,27,8,0,
        11,0,12,0,28,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,5,2,50,8,2,10,2,12,2,53,9,2,1,2,1,2,1,2,
        1,3,1,3,1,3,1,3,1,3,5,3,63,8,3,10,3,12,3,66,9,3,1,4,1,4,1,4,1,4,
        1,4,5,4,73,8,4,10,4,12,4,76,9,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,
        1,6,5,6,87,8,6,10,6,12,6,90,9,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,
        1,8,1,8,1,8,1,8,1,9,5,9,105,8,9,10,9,12,9,108,9,9,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,0,0,12,0,2,4,6,
        8,10,12,14,16,18,20,22,0,1,1,0,17,18,116,0,26,1,0,0,0,2,32,1,0,0,
        0,4,41,1,0,0,0,6,57,1,0,0,0,8,67,1,0,0,0,10,77,1,0,0,0,12,81,1,0,
        0,0,14,91,1,0,0,0,16,97,1,0,0,0,18,106,1,0,0,0,20,109,1,0,0,0,22,
        119,1,0,0,0,24,27,3,2,1,0,25,27,3,4,2,0,26,24,1,0,0,0,26,25,1,0,
        0,0,27,28,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,30,1,0,0,0,30,31,
        5,0,0,1,31,1,1,0,0,0,32,33,5,1,0,0,33,34,5,17,0,0,34,35,5,2,0,0,
        35,36,5,17,0,0,36,37,5,3,0,0,37,38,5,4,0,0,38,39,3,18,9,0,39,40,
        5,5,0,0,40,3,1,0,0,0,41,42,5,6,0,0,42,43,5,17,0,0,43,44,5,4,0,0,
        44,45,3,6,3,0,45,46,3,8,4,0,46,47,3,10,5,0,47,51,3,12,6,0,48,50,
        3,14,7,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,
        52,54,1,0,0,0,53,51,1,0,0,0,54,55,3,16,8,0,55,56,5,5,0,0,56,5,1,
        0,0,0,57,58,5,7,0,0,58,59,5,8,0,0,59,64,3,22,11,0,60,61,5,9,0,0,
        61,63,3,22,11,0,62,60,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,
        1,0,0,0,65,7,1,0,0,0,66,64,1,0,0,0,67,68,5,10,0,0,68,69,5,8,0,0,
        69,74,5,17,0,0,70,71,5,9,0,0,71,73,5,17,0,0,72,70,1,0,0,0,73,76,
        1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,9,1,0,0,0,76,74,1,0,0,0,77,
        78,5,11,0,0,78,79,5,8,0,0,79,80,5,17,0,0,80,11,1,0,0,0,81,82,5,12,
        0,0,82,83,5,8,0,0,83,88,5,17,0,0,84,85,5,9,0,0,85,87,5,17,0,0,86,
        84,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,13,1,0,0,
        0,90,88,1,0,0,0,91,92,5,13,0,0,92,93,5,17,0,0,93,94,5,2,0,0,94,95,
        5,18,0,0,95,96,5,3,0,0,96,15,1,0,0,0,97,98,5,14,0,0,98,99,5,8,0,
        0,99,100,5,4,0,0,100,101,3,18,9,0,101,102,5,5,0,0,102,17,1,0,0,0,
        103,105,3,20,10,0,104,103,1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,
        0,106,107,1,0,0,0,107,19,1,0,0,0,108,106,1,0,0,0,109,110,5,17,0,
        0,110,111,5,9,0,0,111,112,3,22,11,0,112,113,5,15,0,0,113,114,5,17,
        0,0,114,115,5,9,0,0,115,116,3,22,11,0,116,117,5,9,0,0,117,118,5,
        16,0,0,118,21,1,0,0,0,119,120,7,0,0,0,120,23,1,0,0,0,7,26,28,51,
        64,74,88,106
    ]

class TuringDSLParser ( Parser ):

    grammarFileName = "TuringDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'subrutina'", "'('", "')'", "'{'", "'}'", 
                     "'maquina'", "'alfabeto'", "':'", "','", "'estados'", 
                     "'inicio'", "'finales'", "'usa'", "'transiciones'", 
                     "'->'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "DIRECCION", "CNAME", "INT", "WS", "COMENTARIO" ]

    RULE_programa = 0
    RULE_subrutina = 1
    RULE_maquina = 2
    RULE_alfabeto = 3
    RULE_estados = 4
    RULE_inicial = 5
    RULE_finales = 6
    RULE_usa_subrutina = 7
    RULE_transiciones = 8
    RULE_reglas = 9
    RULE_regla = 10
    RULE_simbolo = 11

    ruleNames =  [ "programa", "subrutina", "maquina", "alfabeto", "estados", 
                   "inicial", "finales", "usa_subrutina", "transiciones", 
                   "reglas", "regla", "simbolo" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    DIRECCION=16
    CNAME=17
    INT=18
    WS=19
    COMENTARIO=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TuringDSLParser.EOF, 0)

        def subrutina(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TuringDSLParser.SubrutinaContext)
            else:
                return self.getTypedRuleContext(TuringDSLParser.SubrutinaContext,i)


        def maquina(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TuringDSLParser.MaquinaContext)
            else:
                return self.getTypedRuleContext(TuringDSLParser.MaquinaContext,i)


        def getRuleIndex(self):
            return TuringDSLParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = TuringDSLParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 24
                    self.subrutina()
                    pass
                elif token in [6]:
                    self.state = 25
                    self.maquina()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==6):
                    break

            self.state = 30
            self.match(TuringDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubrutinaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CNAME(self, i:int=None):
            if i is None:
                return self.getTokens(TuringDSLParser.CNAME)
            else:
                return self.getToken(TuringDSLParser.CNAME, i)

        def reglas(self):
            return self.getTypedRuleContext(TuringDSLParser.ReglasContext,0)


        def getRuleIndex(self):
            return TuringDSLParser.RULE_subrutina

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubrutina" ):
                listener.enterSubrutina(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubrutina" ):
                listener.exitSubrutina(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubrutina" ):
                return visitor.visitSubrutina(self)
            else:
                return visitor.visitChildren(self)




    def subrutina(self):

        localctx = TuringDSLParser.SubrutinaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_subrutina)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(TuringDSLParser.T__0)
            self.state = 33
            self.match(TuringDSLParser.CNAME)
            self.state = 34
            self.match(TuringDSLParser.T__1)
            self.state = 35
            self.match(TuringDSLParser.CNAME)
            self.state = 36
            self.match(TuringDSLParser.T__2)
            self.state = 37
            self.match(TuringDSLParser.T__3)
            self.state = 38
            self.reglas()
            self.state = 39
            self.match(TuringDSLParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MaquinaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CNAME(self):
            return self.getToken(TuringDSLParser.CNAME, 0)

        def alfabeto(self):
            return self.getTypedRuleContext(TuringDSLParser.AlfabetoContext,0)


        def estados(self):
            return self.getTypedRuleContext(TuringDSLParser.EstadosContext,0)


        def inicial(self):
            return self.getTypedRuleContext(TuringDSLParser.InicialContext,0)


        def finales(self):
            return self.getTypedRuleContext(TuringDSLParser.FinalesContext,0)


        def transiciones(self):
            return self.getTypedRuleContext(TuringDSLParser.TransicionesContext,0)


        def usa_subrutina(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TuringDSLParser.Usa_subrutinaContext)
            else:
                return self.getTypedRuleContext(TuringDSLParser.Usa_subrutinaContext,i)


        def getRuleIndex(self):
            return TuringDSLParser.RULE_maquina

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaquina" ):
                listener.enterMaquina(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaquina" ):
                listener.exitMaquina(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMaquina" ):
                return visitor.visitMaquina(self)
            else:
                return visitor.visitChildren(self)




    def maquina(self):

        localctx = TuringDSLParser.MaquinaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_maquina)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(TuringDSLParser.T__5)
            self.state = 42
            self.match(TuringDSLParser.CNAME)
            self.state = 43
            self.match(TuringDSLParser.T__3)
            self.state = 44
            self.alfabeto()
            self.state = 45
            self.estados()
            self.state = 46
            self.inicial()
            self.state = 47
            self.finales()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 48
                self.usa_subrutina()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.transiciones()
            self.state = 55
            self.match(TuringDSLParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlfabetoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simbolo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TuringDSLParser.SimboloContext)
            else:
                return self.getTypedRuleContext(TuringDSLParser.SimboloContext,i)


        def getRuleIndex(self):
            return TuringDSLParser.RULE_alfabeto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlfabeto" ):
                listener.enterAlfabeto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlfabeto" ):
                listener.exitAlfabeto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlfabeto" ):
                return visitor.visitAlfabeto(self)
            else:
                return visitor.visitChildren(self)




    def alfabeto(self):

        localctx = TuringDSLParser.AlfabetoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_alfabeto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(TuringDSLParser.T__6)
            self.state = 58
            self.match(TuringDSLParser.T__7)
            self.state = 59
            self.simbolo()
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 60
                self.match(TuringDSLParser.T__8)
                self.state = 61
                self.simbolo()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EstadosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CNAME(self, i:int=None):
            if i is None:
                return self.getTokens(TuringDSLParser.CNAME)
            else:
                return self.getToken(TuringDSLParser.CNAME, i)

        def getRuleIndex(self):
            return TuringDSLParser.RULE_estados

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEstados" ):
                listener.enterEstados(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEstados" ):
                listener.exitEstados(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEstados" ):
                return visitor.visitEstados(self)
            else:
                return visitor.visitChildren(self)




    def estados(self):

        localctx = TuringDSLParser.EstadosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_estados)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(TuringDSLParser.T__9)
            self.state = 68
            self.match(TuringDSLParser.T__7)
            self.state = 69
            self.match(TuringDSLParser.CNAME)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 70
                self.match(TuringDSLParser.T__8)
                self.state = 71
                self.match(TuringDSLParser.CNAME)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InicialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CNAME(self):
            return self.getToken(TuringDSLParser.CNAME, 0)

        def getRuleIndex(self):
            return TuringDSLParser.RULE_inicial

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicial" ):
                listener.enterInicial(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicial" ):
                listener.exitInicial(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicial" ):
                return visitor.visitInicial(self)
            else:
                return visitor.visitChildren(self)




    def inicial(self):

        localctx = TuringDSLParser.InicialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_inicial)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(TuringDSLParser.T__10)
            self.state = 78
            self.match(TuringDSLParser.T__7)
            self.state = 79
            self.match(TuringDSLParser.CNAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FinalesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CNAME(self, i:int=None):
            if i is None:
                return self.getTokens(TuringDSLParser.CNAME)
            else:
                return self.getToken(TuringDSLParser.CNAME, i)

        def getRuleIndex(self):
            return TuringDSLParser.RULE_finales

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinales" ):
                listener.enterFinales(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinales" ):
                listener.exitFinales(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinales" ):
                return visitor.visitFinales(self)
            else:
                return visitor.visitChildren(self)




    def finales(self):

        localctx = TuringDSLParser.FinalesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_finales)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(TuringDSLParser.T__11)
            self.state = 82
            self.match(TuringDSLParser.T__7)
            self.state = 83
            self.match(TuringDSLParser.CNAME)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 84
                self.match(TuringDSLParser.T__8)
                self.state = 85
                self.match(TuringDSLParser.CNAME)
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Usa_subrutinaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CNAME(self):
            return self.getToken(TuringDSLParser.CNAME, 0)

        def INT(self):
            return self.getToken(TuringDSLParser.INT, 0)

        def getRuleIndex(self):
            return TuringDSLParser.RULE_usa_subrutina

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsa_subrutina" ):
                listener.enterUsa_subrutina(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsa_subrutina" ):
                listener.exitUsa_subrutina(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUsa_subrutina" ):
                return visitor.visitUsa_subrutina(self)
            else:
                return visitor.visitChildren(self)




    def usa_subrutina(self):

        localctx = TuringDSLParser.Usa_subrutinaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_usa_subrutina)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(TuringDSLParser.T__12)
            self.state = 92
            self.match(TuringDSLParser.CNAME)
            self.state = 93
            self.match(TuringDSLParser.T__1)
            self.state = 94
            self.match(TuringDSLParser.INT)
            self.state = 95
            self.match(TuringDSLParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransicionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reglas(self):
            return self.getTypedRuleContext(TuringDSLParser.ReglasContext,0)


        def getRuleIndex(self):
            return TuringDSLParser.RULE_transiciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransiciones" ):
                listener.enterTransiciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransiciones" ):
                listener.exitTransiciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransiciones" ):
                return visitor.visitTransiciones(self)
            else:
                return visitor.visitChildren(self)




    def transiciones(self):

        localctx = TuringDSLParser.TransicionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_transiciones)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(TuringDSLParser.T__13)
            self.state = 98
            self.match(TuringDSLParser.T__7)
            self.state = 99
            self.match(TuringDSLParser.T__3)
            self.state = 100
            self.reglas()
            self.state = 101
            self.match(TuringDSLParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReglasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def regla(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TuringDSLParser.ReglaContext)
            else:
                return self.getTypedRuleContext(TuringDSLParser.ReglaContext,i)


        def getRuleIndex(self):
            return TuringDSLParser.RULE_reglas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReglas" ):
                listener.enterReglas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReglas" ):
                listener.exitReglas(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReglas" ):
                return visitor.visitReglas(self)
            else:
                return visitor.visitChildren(self)




    def reglas(self):

        localctx = TuringDSLParser.ReglasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_reglas)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 103
                self.regla()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReglaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CNAME(self, i:int=None):
            if i is None:
                return self.getTokens(TuringDSLParser.CNAME)
            else:
                return self.getToken(TuringDSLParser.CNAME, i)

        def simbolo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TuringDSLParser.SimboloContext)
            else:
                return self.getTypedRuleContext(TuringDSLParser.SimboloContext,i)


        def DIRECCION(self):
            return self.getToken(TuringDSLParser.DIRECCION, 0)

        def getRuleIndex(self):
            return TuringDSLParser.RULE_regla

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegla" ):
                listener.enterRegla(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegla" ):
                listener.exitRegla(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegla" ):
                return visitor.visitRegla(self)
            else:
                return visitor.visitChildren(self)




    def regla(self):

        localctx = TuringDSLParser.ReglaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_regla)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(TuringDSLParser.CNAME)
            self.state = 110
            self.match(TuringDSLParser.T__8)
            self.state = 111
            self.simbolo()
            self.state = 112
            self.match(TuringDSLParser.T__14)
            self.state = 113
            self.match(TuringDSLParser.CNAME)
            self.state = 114
            self.match(TuringDSLParser.T__8)
            self.state = 115
            self.simbolo()
            self.state = 116
            self.match(TuringDSLParser.T__8)
            self.state = 117
            self.match(TuringDSLParser.DIRECCION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimboloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CNAME(self):
            return self.getToken(TuringDSLParser.CNAME, 0)

        def INT(self):
            return self.getToken(TuringDSLParser.INT, 0)

        def getRuleIndex(self):
            return TuringDSLParser.RULE_simbolo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimbolo" ):
                listener.enterSimbolo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimbolo" ):
                listener.exitSimbolo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimbolo" ):
                return visitor.visitSimbolo(self)
            else:
                return visitor.visitChildren(self)




    def simbolo(self):

        localctx = TuringDSLParser.SimboloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_simbolo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            _la = self._input.LA(1)
            if not(_la==17 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





