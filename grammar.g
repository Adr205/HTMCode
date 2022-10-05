//Javier Adrian Villa Leon
//A01242469
//Tokens
MAIN: "main"
VAR: "var"
IF: "if"
ELSE: "else"
FOR: "for"
WHILE: "while"
INTT: "int"
STRINGT: "string"
BOOLEANT: "boolean"
PRINT: "print"
INPUT: "input"
FUNCION: "function"
RETURN: "return"
DECLARE: "declare"
VOID: "void"
TRUE: "true"
FALSE: "false"
DOSPUNTOS : /:/
PUNTOYCOMA: ";"
COMA: ","
SUMA: /\+/
RESTA: /-/
MULTIPLICACION: /\*/
DIVISION: /\//
MASMAS: /\+/ /\+/
MENOSMENOS: /\-/ /\-/
MASIGUAL: /\+/ /=/
MENOSIGUAL: /\-/ /=/
MULTIGUAL: /\*/ /=/
DIVIGUAL: /\// /=/
PARENTESIS_I: /\(/
PARENTESIS_D: /\)/
CORCHETE_I: /\[/
CORCHETE_D: /\]/
LLAVEI: /{/
LLAVED: /}/
MAYOR: />/
MAYORIGUAL: />/ /=/
MENOR: /</
MENORIGUAL: /</ /=/
ES_DIFERENTE: /!=/
ES_IGUAL: /==/
IGUAL: /=/
NEW_LINE: /\n+/
ID: /[a-zA-Z_][a-zA-Z0-9_]*/
NUMERO: /\d+/
INT: /\d+/
STRING: /\".*\"/
FLOAT: /\d+\.\d+/
FLOATT: "float"
WHITESPACE: (" " | /\t/ )+
%ignore WHITESPACE
%ignore NEW_LINE      

start: globales main 

globales: funciones globales| varglobales globales | 
funciones: funcionvoid | funcion
funcionvoid: FUNCION ID PARENTESIS_I funcvars PARENTESIS_D DOSPUNTOS VOID bloque
funcion: FUNCION ID PARENTESIS_I funcvars PARENTESIS_D DOSPUNTOS tipo bloquefunc 
varglobales: DECLARE ID IGUAL expresion PUNTOYCOMA | DECLARE ID CORCHETE_I INT CORCHETE_D IGUAL expresion PUNTOYCOMA
funcvars: ID DOSPUNTOS tipo funcvarsx |
funcvarsx: COMA funcvars |
main: MAIN PARENTESIS_I PARENTESIS_D bloque

bloque: LLAVEI bloq bloqx LLAVED
bloq: estatuto
bloqx: bloq bloqx |
bloquefunc: LLAVEI bloq bloqx RETURN expresion PUNTOYCOMA LLAVED
estatuto: asignacion | escritura | read  | llamadavoid | ciclos | condicion

asignacion: asignacionsimple | asignacioncompleja
asignacionsimple: ID IGUAL expresion PUNTOYCOMA
asignacioncompleja: ID CORCHETE_I INT CORCHETE_D IGUAL expresion PUNTOYCOMA | asignacionlista
asignacionlista: ID IGUAL expresionlista PUNTOYCOMA
expresionlista: CORCHETE_I expresion explista CORCHETE_D
explista: COMA expresion explista |

escritura: PRINT PARENTESIS_I escriturax PARENTESIS_D PUNTOYCOMA
//escriturax: expresion escrituray  | STRING escrituray
escriturax: expresion escrituray  
escrituray: COMA escriturax |

read: INPUT PARENTESIS_I ID PARENTESIS_D PUNTOYCOMA

ciclos: ciclofor | ciclowhile
ciclofor: FOR PARENTESIS_I asignacionsimple expresion PUNTOYCOMA contador PARENTESIS_D bloque
contador: contadorsimple | contadorcomplejo
contadorsimple: ID contadorhelpersimple 
contadorhelpersimple: MASMAS | MENOSMENOS
contadorcomplejo: ID contadorhelpercomplejo INT
contadorhelpercomplejo: MULTIGUAL | DIVIGUAL | MASIGUAL | MENOSIGUAL
ciclowhile: WHILE PARENTESIS_I expresion PARENTESIS_D bloque

condicion: IF PARENTESIS_I expresion PARENTESIS_D bloque condicionx
condicionx: ELSE bloque |

llamadavoid: ID PARENTESIS_I voidvars PARENTESIS_D PUNTOYCOMA
llamadafunc: ID PARENTESIS_I voidvars PARENTESIS_D
voidvars: exp vvars |
vvars: COMA exp vvars | 

expresion: exp expresionx
expresionx: logicos exp |
logicos: MAYOR | MENOR | MENORIGUAL | MAYORIGUAL | ES_DIFERENTE | ES_IGUAL
exp: termino expx
expx: expy exp |
expy: SUMA | RESTA
termino: factor terminox
terminox: terminoy termino | 
terminoy: MULTIPLICACION | DIVISION
factor: PARENTESIS_I expresion PARENTESIS_D | factorx varcte | varcte
factorx: SUMA | RESTA
varcte: ID | INT | boolean | llamadafunc | CORCHETE_I exp CORCHETE_D | FLOAT | STRING | arreglo
arreglo: ID CORCHETE_I INT CORCHETE_D | ID CORCHETE_I ID CORCHETE_D

tipo: INTT | FLOATT | STRINGT | BOOLEANT
boolean: TRUE | FALSE