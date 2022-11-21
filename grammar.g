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
FLOATT: "float"
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
WHITESPACE: (" " | /\t/ )+

%ignore WHITESPACE
%ignore NEW_LINE
%import common.ESCAPED_STRING  -> ACCION

start: globales main 

globales: funciones globales| varglobales globales | 
funciones: funcionvoid | funcion
funcionvoid: FUNCION ID np_func_id PARENTESIS_I funcvars PARENTESIS_D DOSPUNTOS VOID bloque np_end_func
funcion: FUNCION ID np_func_id PARENTESIS_I funcvars PARENTESIS_D DOSPUNTOS tipo bloquefunc np_end_func
varglobales: simpleglobal | compuestoglobal
simpleglobal: DECLARE ID DOSPUNTOS tipo IGUAL expresion PUNTOYCOMA np_asignacion | DECLARE ID DOSPUNTOS tipo PUNTOYCOMA
compuestoglobal:DECLARE ID CORCHETE_I INT CORCHETE_D DOSPUNTOS tipo IGUAL expresion PUNTOYCOMA | DECLARE ID CORCHETE_I INT CORCHETE_D DOSPUNTOS tipo PUNTOYCOMA
funcvars: ID DOSPUNTOS tipo funcvarsx |
funcvarsx: COMA funcvars |
main: MAIN np_main PARENTESIS_I PARENTESIS_D bloque end
np_main:
np_func_id:
np_end_func:

bloque: LLAVEI bloq bloqx LLAVED
bloq:  estatuto | declaracion
bloqx: bloq bloqx |
bloquefunc: LLAVEI bloq bloqx RETURN expresion PUNTOYCOMA np_func_result LLAVED
estatuto: asignacion | escritura | read  | llamadavoid | ciclos | condicion
np_func_result:

declaraciones: declaracion declaracionesx
declaracionesx: declaraciones |
declaracion: simple | compuesta
simple: simpledeclaracion | simpleasignacion
simpledeclaracion: VAR ID np_is_var_false DOSPUNTOS tipo PUNTOYCOMA
simpleasignacion: VAR ID np_is_var_false DOSPUNTOS tipo IGUAL expresion PUNTOYCOMA np_asignacion_2
compuesta: compuestadeclaracion | compuestaasignacion
compuestadeclaracion: VAR ID CORCHETE_I INT CORCHETE_D DOSPUNTOS tipo PUNTOYCOMA
compuestaasignacion: VAR ID CORCHETE_I INT CORCHETE_D DOSPUNTOS tipo IGUAL CORCHETE_I expresionasig CORCHETE_D PUNTOYCOMA 
expresionasig: expresion COMA expresionasig | expresion
np_asignacion_2:
np_is_var_false:


asignacion: asignacionsimple | asignacioncompleja
asignacionsimple: ID IGUAL expresion PUNTOYCOMA np_asignacion
np_asignacion:
//np_var:

asignacioncompleja: ID CORCHETE_I INT CORCHETE_D IGUAL expresion PUNTOYCOMA | asignacionlista
asignacionlista: ID IGUAL expresionlista PUNTOYCOMA
expresionlista: CORCHETE_I expresion explista CORCHETE_D
explista: COMA expresion explista |

escritura: PRINT PARENTESIS_I escriturax PARENTESIS_D PUNTOYCOMA
//escriturax: expresion escrituray  | STRING escrituray
escriturax: expresion escrituray  
escrituray:  np_escritura COMA escriturax | np_escritura
np_escritura:

read: INPUT PARENTESIS_I ID PARENTESIS_D PUNTOYCOMA

ciclos: ciclofor | ciclowhile

ciclofor: FOR np_for PARENTESIS_I asignacionfor np_for_false contador PUNTOYCOMA  expresion PARENTESIS_D bloque np_for_2
contador: contadorsimple | contadorcomplejo
contadorsimple: ID contadorhelpersimple 
contadorhelpersimple: MASMAS | MENOSMENOS
contadorcomplejo: ID contadorhelpercomplejo INT
contadorhelpercomplejo: MULTIGUAL | DIVIGUAL | MASIGUAL | MENOSIGUAL
asignacionfor: ID IGUAL expresion PUNTOYCOMA
np_for:
np_for_2:
np_for_false:

ciclowhile: WHILE PARENTESIS_I np_while_3 expresion np_while PARENTESIS_D bloque np_while_2
np_while:
np_while_2:
np_while_3:

condicion: IF PARENTESIS_I expresion PARENTESIS_D np_if bloque  condicionx
condicionx: np_if_3 ELSE bloque np_if_2 | np_if_2
np_if:
np_if_2:
np_if_3:

llamadavoid: ID PARENTESIS_I voidvars  np_func_vars PARENTESIS_D PUNTOYCOMA
llamadafunc: ID PARENTESIS_I voidvars np_func_vars PARENTESIS_D
voidvars: exp vvars |
vvars: COMA exp vvars | 
np_func_vars:
 
expresion: exp expresionx
expresionx: logicos exp np_logico_2 |
logicos: MAYOR -> np_logico | MENOR -> np_logico | MENORIGUAL -> np_logico | MAYORIGUAL -> np_logico | ES_DIFERENTE  -> np_logico | ES_IGUAL -> np_logico
np_logico:
np_logico_2:

exp: termino expx
expx: expy exp cuadruplo_sr |
expy: SUMA | RESTA
cuadruplo_sr:

termino: factor terminox
terminox: terminoy termino cuadruplo_md | 
terminoy: MULTIPLICACION | DIVISION
cuadruplo_md:

factor: PARENTESIS_I expresion PARENTESIS_D | factorx varcte | varcte
factorx: SUMA | RESTA


varcte: llamadafunc | boolean | id  | int  | CORCHETE_I exp CORCHETE_D | float | string | arreglo
id: ID -> guardar_id
int: INT ->  guardar_int
float: FLOAT -> guardar_float
string: STRING -> guardar_string
arreglo: ID CORCHETE_I INT CORCHETE_D | ID CORCHETE_I ID CORCHETE_D


tipo: INTT | FLOATT | STRINGT | BOOLEANT
boolean: TRUE -> guardar_boolean | FALSE -> guardar_boolean

end: