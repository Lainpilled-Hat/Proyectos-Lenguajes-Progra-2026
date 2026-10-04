grammar TuringDSL;

// --- REGLAS SINTÁCTICAS (GLC) ---
programa : (subrutina | maquina)+ EOF ;

subrutina : 'subrutina' CNAME '(' CNAME ')' '{' reglas '}' ;

maquina : 'maquina' CNAME '{' 
            alfabeto 
            estados 
            inicial 
            finales 
            (usa_subrutina)* 
            transiciones 
          '}' ;

alfabeto   : 'alfabeto' ':' simbolo (',' simbolo)* ;
estados    : 'estados' ':' CNAME (',' CNAME)* ;
inicial    : 'inicio' ':' CNAME ;
finales    : 'finales' ':' CNAME (',' CNAME)* ;
usa_subrutina : 'usa' CNAME '(' INT ')' ;

transiciones : 'transiciones' ':' '{' reglas '}' ;
reglas       : regla* ;
regla        : CNAME ',' simbolo '->' CNAME ',' simbolo ',' DIRECCION ;

simbolo      : CNAME | INT ;

// --- REGLAS LÉXICAS (ER) ---
DIRECCION : 'IZQ' | 'DER' | 'QUIETO' ;
CNAME     : [a-zA-Z_][a-zA-Z0-9_]* ;
INT       : [0-9]+ ;

WS          : [ \t\r\n]+ -> skip ;
COMENTARIO  : '#' ~[\r\n]* -> skip ;