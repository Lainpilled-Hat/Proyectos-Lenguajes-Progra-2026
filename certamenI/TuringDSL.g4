grammar TuringDSL;

// REGLAS SINTÁCTICAS (GLC)
// Un programa contiene una o más subrutinas o máquinas
programa : (subrutina | maquina)+ EOF ;


// Define una subrutina con un nombre, un parámetro y un conjunto de reglas de transición
subrutina : 'subrutina' CNAME ('(' CNAME ')')? '{' reglas '}' ;

// Define una máquina 
maquina : 'maquina' CNAME '{' 
            alfabeto 
            estados 
            inicial 
            finales 
            (invocacion_subrutina)* 
            transiciones 
          '}' ;

// Define todo lo que construye la máquina.
alfabeto   : 'alfabeto' ':' simbolo (',' simbolo)* ;
estados    : 'estados' ':' CNAME (',' CNAME)* ;
inicial    : 'inicio' ':' CNAME ;
finales    : 'finales' ':' CNAME (',' CNAME)* ;
invocacion_subrutina : CNAME ('(' INT ')')? ;

transiciones : 'transiciones' ':' '{' reglas '}' ;
reglas       : regla* ;
regla        : CNAME ',' simbolo '->' CNAME ',' simbolo ',' DIRECCION ;

simbolo      : BLANCO | CNAME | INT | SIMBOLO ;

// REGLAS LÉXICAS (ER). Cómo se reconocen los tokens
BLANCO    : 'BLANCO' ;
DIRECCION : 'IZQ' | 'DER' | 'QUIETO' ;
CNAME     : [a-zA-Z_][a-zA-Z0-9_]* ;
INT       : [0-9]+ ;
SIMBOLO   : [!$%&'*+./=?@\\^`|~-] ;

WS          : [ \t\r\n]+ -> skip ;
COMENTARIO  : '#' ~[\r\n]* -> skip ;