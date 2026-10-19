grammar TuringDSL;

// REGLAS SINTÁCTICAS (GLC)
// Un programa contiene una o más subrutinas o máquinas
programa : (subrutina | maquina)+ EOF ;


// Define una subrutina con un nombre, un parámetro y un conjunto de reglas de transición
subrutina : 'subrutina' CNAME '(' CNAME ')' '{' reglas '}' ;

// Define una máquina 
maquina : 'maquina' CNAME '{' 
            alfabeto 
            blanco
            estados 
            inicial 
            finales 
            (usa_subrutina)* 
            transiciones 
          '}' ;

// Define todo lo que construye la máquina.
direccion  : 'direccion' ':' simbolo ;
blanco     : 'blanco' ':' simbolo ;
alfabeto   : 'alfabeto' ':' simbolo (',' simbolo)* ;
estados    : 'estados' ':' CNAME (',' CNAME)* ;
inicial    : 'inicio' ':' CNAME ;
finales    : 'finales' ':' CNAME (',' CNAME)* ;
usa_subrutina : CNAME '(' CNAME ')' ;

transiciones : 'transiciones' ':' '{' reglas '}' ;
reglas       : regla* ;
regla        : CNAME ',' simbolo '->' CNAME ',' simbolo ',' direccion ;

simbolo      : CNAME ;

// REGLAS LÉXICAS (ER). Cómo se reconocen los tokens
CNAME     : [a-zA-Z_][a-zA-Z0-9_]* ;
INT       : [0-9]+ ;

WS          : [ \t\r\n]+ -> skip ;
COMENTARIO  : '#' ~[\r\n]* -> skip ;