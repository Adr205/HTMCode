from lark import Token, Visitor
from classes.VariablesTable import VariablesTable
from classes.Variable import Variable
from classes.Cuadruplos import Cuadruplos
from classes.Semantic_cube import SemanticCube
from classes.Function import Function
from classes.FunctionDirectory import FunctionDirectory
from classes.TablaConstantes import TablaConstantes
from classes.Memoria import Memoria

funcDirectory = FunctionDirectory() 

#! Clases para los puntos neurales
semantic_Cube = SemanticCube() #* Cubo semantico
cuadruplos = Cuadruplos() #* Cuadruplos generados
tablaDeVariables = VariablesTable() #* Tabla de variables
tablaDeConstantes = TablaConstantes() #* Tabla de constantes
memoria = Memoria() #* Memoria

#! Pilas
pSaltos = []  # * pila de saltos 
pOper = []  # * pila de operadores
pOp = []  # * pila de operandos
pMem = []  # * pila de memoria de operandos
pType = []  # * pila de tipos
pVars = []  # * pila de variables
pFor = [] # * pila de for
pContadores = [] # * pila de contadores
pResultFuncs = [] # * pila de resultados de funciones
pContexto = ["global"] # * pila de contexto por si se esta en el el global, main o en una funcion
pIsVar = [] # * pila de si es variable o no

global VC, VF, contVariablesTemporales, contadores
funcVars = 0
VC = -1 
VF = -1
contVariablesTemporales = 0 #* Contador de variables temporales
# * Object contadores  [{operation:, value:}]
contadores = []

# TODO: Separacion de memoria para el tipado de variables
pTempInt = [] # * pila de variables temporales de tipo int
pTempFloat = [] # * pila de variables temporales de tipo float
pTempString = [] # * pila de variables temporales de tipo string
pTempBool = [] # * pila de variables temporales de tipo bool
contInt = 0 # * contador de variables temporales de tipo int
contFloat = 0 # * contador de variables temporales de tipo float
contString = 0 # * contador de variables temporales de tipo string
contBool = 0 # * contador de variables temporales de tipo bool
contTempInt = 0 # * contador de variables temporales de tipo int
contTempFloat = 0 # * contador de variables temporales de tipo float
contTempString = 0 # * contador de variables temporales de tipo string
contTempBool = 0 # * contador de variables temporales de tipo bool
contIntVars = 0 # * contador de variables de tipo int
contFloatVars = 0 # * contador de variables de tipo float
contStringVars = 0 # * contador de variables de tipo string
contBoolVars = 0 # * contador de variables de tipo bool


# TODO: Punto neuralgico Read
# TODO: Punto neuralgico Input


class NeuralPoints(Visitor):

    def start(self, tree):
        pSaltos.append(cuadruplos.contador)
        cuadruplos.addCuadruplo("GOTO-MAIN", None, None, "N/A")

    def np_main(self, tree):
        cuadruplos.fillCuadruplo(pSaltos.pop(), cuadruplos.contador)
        #* Resetear el valor de las variables locales
        global contVariablesTemporales
        contVariablesTemporales = 1
        memoria.intLocal = memoria.memoria["local"]["int"]
        memoria.floatLocal = memoria.memoria["local"]["float"]
        memoria.stringLocal = memoria.memoria["local"]["string"]
        memoria.booleanLocal = memoria.memoria["local"]["boolean"]
        memoria.intTemporal = memoria.memoria["temporal"]["int"]
        memoria.floatTemporal = memoria.memoria["temporal"]["float"]
        memoria.stringTemporal = memoria.memoria["temporal"]["string"]
        memoria.booleanTemporal = memoria.memoria["temporal"]["boolean"]
        # func = Function(pOp.pop(), pType.pop(), cuadruplos.contador, params) # Crear funcion
        # funcDirectory.addFunction(func) # Agregar funcion al directorio de funciones
        funcMain = Function("main", "void", cuadruplos.contador, []) # Crear funcion
        funcDirectory.addFunction(funcMain) # Agregar funcion al directorio de funciones

    # * Funcion para declarar variables globales en la tabla de variables
    def simpleglobal(self, tree):
        varName = tree.children[1].value
        varType = tree.children[3].children[0].value
        varIgual = tree.children[4].value
        varValue = 0  # TODO: Agarrar el valor de la pila de operandos y asignar el valor a la variable
        if(varIgual == "="):
            # print(pOp)
            # varValue = pOp.pop()  # TODO: Agarrar el valor de la pila de operandos y asignar el valor a la variable
            varValue = -1  # TODO: Agarrar el valor de la pila de operandos y asignar el valor a la variable
        else:
            varValue = "N/A"  # : No tiene valor
        dirV = -1
        if varType == 'int':
            dirV = memoria.intGlobal
            memoria.intGlobal += 1
        elif varType == 'float':
            dirV = memoria.floatGlobal
            memoria.floatGlobal += 1
        elif varType == 'string':
            dirV = memoria.stringGlobal
            memoria.stringGlobal += 1
        elif varType == 'boolean':
            dirV = memoria.booleanGlobal
            memoria.booleanGlobal += 1
        tablaDeVariables.addVariable(Variable(varName, varType, varValue, dirV))
        # TODO: Usar variables temporales y el valor de la pila de operandos
        # cuadruplos.addCuadruplo("=", varValue, None, varName)
        pVars.append(varName)
        # pType.append(varType)

    # * Funcion para declarar arreglos globales en la tabla de variables
    def compuestoglobal(self, tree):
        x = 1  # TODO: Agregar todo lo del uso de arreglos como variables

    # * Funcion para declarar variables en la tabla de variables
    def simpledeclaracion(self, tree):
        global contIntVars, contFloatVars, contStringVars, contBoolVars
        varName = tree.children[1].value  # Nombre de la variable
        varType = tree.children[4].children[0].value  # Tipo de la variable
        # Agregar variable a la tabla de variables
        if varType == 'int':
            dirV = memoria.intLocal
            memoria.intLocal += 1
            contIntVars += 1
        elif varType == 'float':
            dirV = memoria.floatLocal
            memoria.floatLocal += 1
            contFloatVars += 1
        elif varType == 'string':
            dirV = memoria.stringLocal
            memoria.stringLocal += 1
            contStringVars += 1
        elif varType == 'boolean':
            dirV = memoria.booleanLocal
            memoria.booleanLocal += 1
            contBoolVars += 1
        tablaDeVariables.addVariable(Variable(varName, varType, "N/A", dirV))

    # * Funcion para declarar variables en la tabla de variables y asignarles un valor
    def simpleasignacion(self, tree):
        global contIntVars, contFloatVars, contStringVars, contBoolVars
        varName = tree.children[1].value
        pVars.append(varName)
        varType = tree.children[4].children[0].value
        # TODO: Agarrar el valor de la pila de operandos y asignar el valor a la variable y verificar si es de tipo correcto
        varValue = "N/A"
        if varType == 'int':
            dirV = memoria.intLocal
            memoria.intLocal += 1
            contIntVars += 1
        elif varType == 'float':
            dirV = memoria.floatLocal
            memoria.floatLocal += 1
            contFloatVars += 1
        elif varType == 'string':
            dirV = memoria.stringLocal
            memoria.stringLocal += 1
            contStringVars += 1
        elif varType == 'boolean':
            dirV = memoria.booleanLocal
            memoria.booleanLocal += 1
            contBoolVars += 1
        tablaDeVariables.addVariable(Variable(varName, varType, varValue, dirV))

    def compuestadeclaracion(self, tree):
        varName = tree.children[1].value
        # TODO: Agregar el procedimiento para los arreglos
        varSize = tree.children[3].value
        varType = tree.children[6].children[0].value
        tablaDeVariables.addVariable(Variable(varName, varType, "N/A"))

    def compuestaasignacion(self, tree):
        varName = tree.children[1].value
        varSize = tree.children[3].value
        # TODO:Agregar el proceso para los arreglos
        varType = tree.children[6].children[0].value
        # TODO: Agregar el valor a la variable
        tablaDeVariables.addVariable(Variable(varName, varType, "N/A"))

    #* Funcion para asignar el valor a una variable
    def asignacionsimple(self, tree):
        varName = tree.children[0].value # Nombre de la variable
        pVars.append(varName) # Agregar variable a la pila de variables
        var = tablaDeVariables.getVariable(varName)
        if var == None:
            print("Error: Variable no declarada")
            exit()

    #! Funciones para generacion de cuadruplos del condicional IF
    #* Funcion para añadir el gotoF a la pila de saltos y crear el cuadruplo
    def np_if(self,tree):
        result = pOp.pop() # Valor de la condicion
        pType.pop() # Tipo de la condicion
        pSaltos.append(cuadruplos.contador) # Agregar el contador de cuadruplos a la pila de saltos
        cuadruplos.addCuadruplo("GOTOF", result, None, "N/A") # Agregar cuadruplo de salto falso

    #*Funcion para llenar el cuadruplo de salto falso
    def np_if_2(self, tree):
        cuadruplos.fillCuadruplo(pSaltos.pop(), cuadruplos.contador) # Llenar el cuadruplo de salto falso

    #* Funcion para crear cuadruplo GOTO al finalizar el IF
    def np_if_3(self, tree):
        cuadruplos.fillCuadruplo(pSaltos.pop(), cuadruplos.contador + 1) # Llenar el cuadruplo de salto falso
        pSaltos.append(cuadruplos.contador) # Agregar el contador de cuadruplos a la pila de saltos
        cuadruplos.addCuadruplo("GOTO", None, None, "N/A") # Agregar cuadruplo de salto

    #! Funciones para generacion de cuadruplos del ciclo FOR

    #* Funcion para añadir un True a la pila de for's anidados
    def np_for(self, tree):
        pFor.append(True)

    #* Funcion para manejar la asignacion de la variable del ciclo for
    def asignacionfor(self, tree):
        global contIntVars
        varName = tree.children[0].value # Nombre de la variable
        pVars.append(varName) # Agregar variable a la pila de variables
        dirV = memoria.intLocal
        memoria.intLocal += 1
        contIntVars += 1
        tablaDeVariables.addVariable(Variable(varName, "int", 'N/A', dirV)) # Agregar variable a la tabla de variables
    
    #* Funcion para igualar la variable del for y la VC
    def np_for_false(self, tree):
        result = pOp.pop()
        varName = pVars.pop()
        varType = pType.pop()
        #TODO: Añadir contador de VC para manejar anidados, y buscar la dirv de variable y VC y VF
        #TODO: Checar la direcion de VC < VF
        varNameDir = tablaDeVariables.getVariable(varName).dirV
        cuadruplos.addCuadruplo("=", result, None, varNameDir) 
        cuadruplos.addCuadruplo("=", varNameDir, None, "VC")

    #* Funcion para guardar el contador del for y for's anidados
    def contador(self, tree):
        varName = tree.children[0].children[0].value
        operator = tree.children[0].children[1].children[0].value
        cont = 1
        if operator == "+=" or operator == "-=" or operator == "*=" or operator == "/=":
            cont = tree.children[0].children[2].value
        pContadores.append([varName, operator, cont])

    #* Funcion para sumar la VC y llenar el cuadruplo del for y crear el GOTO del for
    def np_for_2(self, tree):
        global contVariablesTemporales
        pContador = pContadores.pop()
        temp = memoria.intTemporal
        memoria.intTemporal += 1
        cuadruplos.addCuadruplo(pContador[1], "VC", pContador[2], 't' + str(temp))
        contVariablesTemporales += 1
        cuadruplos.addCuadruplo("=", 't' + str(temp), None, 'VC')
        cuadruplos.addCuadruplo("=", 't' + str(temp), None, pContador[0])
        fill = pSaltos.pop()
        add = pSaltos.pop()
        cuadruplos.addCuadruplo("GOTO", None, None, add)
        cuadruplos.fillCuadruplo(fill, cuadruplos.contador)

    #! Funciones para generacion de cuadruplos del ciclo WHILE
    #*Funcion para crear el cuadruplo del while
    def np_while(self, tree):
        result = pOp.pop() # Valor de la condicion
        pType.pop() # Tipo de la condicion
        pSaltos.append(cuadruplos.contador) # Agregar el contador de cuadruplos a la pila de saltos
        cuadruplos.addCuadruplo("GOTOF", result, None, "N/A") # Agregar cuadruplo de salto falso

    #* Funcion para llenar el cuadruplo de while y crear el goto de regreso
    def np_while_2(self, tree):
        fill = pSaltos.pop() # Llenar el cuadruplo de salto falso
        add = pSaltos.pop() # Agregar el contador de cuadruplos a la pila de saltos
        cuadruplos.addCuadruplo("GOTO", None, None, add) # Agregar cuadruplo de salto a inicio
        cuadruplos.fillCuadruplo(fill, cuadruplos.contador) # Llenar el cuadruplo de salto falso

    #* Funcion para agregar el salto a la pila de saltos
    def np_while_3(self, tree):
        pSaltos.append(cuadruplos.contador) # Agregar el contador de cuadruplos a la pila de saltos

    #! Funciones para generacion de cuadruplos de funciones
    #* Estructura del directorio de funciones
    # funDirectory = {
    #     "name": {
    #         "type": "int",
    #         "dirV": 0,
    #         "vars" :{
    #             "name" : "name",
    #             "type" : "int",
    #             "dirV" : 0,
    #             "dim" :{
    #                 "limInf": 0,
    #                 "limSup": 0,
    #                 "k" : 0,
    #                 "node": {
    #                     "limInf": 0,
    #                     "limSup": 0,
    #                     "k" : 0,
    #                     "node": {...
    #                     }
    #                 }

    #             }
    #         }
    #     }
    # }

    def funcion(self,tree):
        global contVariablesTemporales
        contVariablesTemporales = 1
        memoria.intLocal = memoria.memoria["local"]["int"]
        memoria.floatLocal = memoria.memoria["local"]["float"]
        memoria.stringLocal = memoria.memoria["local"]["string"]
        memoria.booleanLocal = memoria.memoria["local"]["boolean"]
        memoria.intTemporal = memoria.memoria["temporal"]["int"]
        memoria.floatTemporal = memoria.memoria["temporal"]["float"]
        memoria.stringTemporal = memoria.memoria["temporal"]["string"]
        memoria.booleanTemporal = memoria.memoria["temporal"]["boolean"]
        varName = tree.children[1].value # Nombre de la funcion
        pContexto.append(varName) # Agregar el nombre de la funcion a la pila de contexto
        funcType = tree.children[7].children[0].value # Tipo de la funcion
        pOp.append(varName) # Agregar nombre de la funcion a la pila de operandos
        pType.append(funcType) # Agregar tipo de la funcion a la pila de tipos
        vars = tree.children[4].scan_values(lambda v: isinstance(v, Token))
        global funcVars
        for var in vars:
            if var == "int" or var == "float" or var == "string" or var == "boolean":
                pType.append(var.value)
            elif var == ',' or var == ':':
                pass
            else:
                pOp.append(var.value)
                funcVars +=1

    def np_func_id(self,tree):
        global funcVars
        params = [] #Lista de parametros
        for i in range(funcVars):
            params.append([ pOp.pop(), pType.pop()])
        params.reverse() # Invertir lista de parametros en orden correcto
        func = Function(pOp.pop(), pType.pop(), cuadruplos.contador, params) # Crear funcion
        funcDirectory.addFunction(func) # Agregar funcion al directorio de funciones

    def np_func_result(self,tree):
        global funcVars
        funcVars = 0
        exist = tablaDeVariables.getVariable(pOp[-1])
        if exist != None:
            cuadruplos.addCuadruplo("RETURN", None, None, exist.dirV)
        else:
            cuadruplos.addCuadruplo("RETURN", None, None, pOp[-1])
        funcType = pType.pop() # Tipo de la funcion
        result = pOp.pop() # Nombre de la funcion
        value = "Get Result" #Get value of var
        pResultFuncs.append([result, funcType, value]) # Agregar funcion a la pila de funciones con resultado
        # pIsVar.pop() # Quitar bandera de variable de la pila de banderas

    def np_end_func(self, tree):
        if len(pIsVar) > 0:
            pIsVar.pop()
        contTempInt = memoria.intTemporal - memoria.memoria["temporal"]["int"]
        contTempFloat = memoria.floatTemporal - memoria.memoria["temporal"]["float"]
        contTempString = memoria.stringTemporal - memoria.memoria["temporal"]["string"]
        contTempBool = memoria.booleanTemporal - memoria.memoria["temporal"]["boolean"]
        # print("Temporales utilizados: ", contTempInt, contTempFloat, contTempString, contTempBool) 
        cuadruplos.addCuadruplo("ENDFUNC", None, None, None)
        funcName = pContexto.pop()
        function = funcDirectory.getFunction(funcName)
        function.variables = tablaDeVariables.variables
        funcDirectory.updateFunction(function)
        tablaDeVariables.resetTable()
        # print(function)
        # print(tablaDeVariables)

    #! Funciones para cuadruplos de llamada a funciones
    def llamadavoid(self, tree):
        global pVars
        funcID = tree.children[0].value
        pVars.append(funcID)

    def llamadafunc(self, tree):
        global pVars
        funcID = tree.children[0].value
        pVars.append(funcID)

    def np_func_vars(self, tree):
        global pVars
        funcName = pVars.pop()
        funcVars = []
        for i in range(len(pOp)):
            funcVars.append([pOp.pop(), pType.pop()])
        #Get function
        funcVars.reverse()
        function = funcDirectory.getFunction(funcName)
        
        if len(funcVars) != len(function.params):
            print("Error: Numero de parametros incorrecto, se esperaban " + str(len(function.params)) + " parametros y se recibieron " + str(len(funcVars)))
            exit()

        cuadruplos.addCuadruplo("ERA", None, None, function.name)

        for i in range(len(funcVars)):
            if funcVars[i][1] != function.params[i][1]:
                print("Error: Tipo de parametro incorrecto, se esperaba " + function.params[i][1] + " y se recibio " + funcVars[i][1])
                exit()
            exist = tablaDeVariables.getVariable(funcVars[i][0])
            if exist != None:
                cuadruplos.addCuadruplo("PARAM", exist.dirV, None, function.params[i][0])
            else:
                cuadruplos.addCuadruplo("PARAM", funcVars[i][0], None, function.params[i][0])
        cuadruplos.addCuadruplo("GOSUB", None, None, function.dirV)



    #! Funciones para operaciones aritmeticas

    # *Funcion para añadir el simbolo de suma o resta a la pila de operadores
    def expy(self, tree):
        pOper.append(tree.children[0].value)

    # *Funcion para añadir el simbolo de multiplicacion o division a la pila de operadores
    def terminoy(self, tree):
        pOper.append(tree.children[0].value)

    #* Funcion para añadir los simbolos logicos a la pila de operadores
    def np_logico(self, tree):
        pOper.append(tree.children[0].value)

    #* Funcion para crear el cuadruplo logico
    def np_logico_2(self, tree):
        global contVariablesTemporales, contTempBool
        if len(pOper) > 0:
            right_operand = pOp.pop()
            left_operand = pOp.pop()
            operator = pOper.pop()
            right_type = pType.pop()
            left_type = pType.pop()
            result_type = semantic_Cube.getValue(operator,left_type, right_type)
            if result_type == "error":
                print("Error: Tipo de dato no valido")
                exit()
            temp = memoria.booleanTemporal
            existLeft = tablaDeVariables.getVariable(left_operand)
            existRight = tablaDeVariables.getVariable(right_operand)
            if existLeft != None:
                left_operand = existLeft.dirV
            if existRight != None:
                right_operand = existRight.dirV
            cuadruplos.addCuadruplo(operator, left_operand, right_operand, temp)
            contVariablesTemporales += 1
            memoria.booleanTemporal += 1
            contTempBool += 1
            pOp.append(temp)
            pType.append(result_type)
            if pFor != []: #Si hay un for entonces añadirlos cuadruplos de igual a VF y comparacion de VC y VF
                pFor.pop()
                cuadruplos.addCuadruplo("=", right_operand, None, "VF")
                pSaltos.append(cuadruplos.contador)
                temp = memoria.intTemporal
                cuadruplos.addCuadruplo("<", "VC", "VF",temp)
                contVariablesTemporales += 1
                memoria.intTemporal += 1
                pSaltos.append(cuadruplos.contador)
                cuadruplos.addCuadruplo("GOTOF",temp, None, "N/A")
                pOp.pop()
                pType.pop()

    # *Funcion para crear el cuadruplo de la suma y resta
    def cuadruplo_sr(self, tree):
        if len(pOper) > 0:  # Checar si la pila de operadores esta vacia
            # Checar si el ultimo operador es de suma o resta
            global contVariablesTemporales,contTempInt, contTempFloat, contTempString, contTempBool 
            #! Sacar direcciones de memoria de los operandos
            if pOper[-1] == "+" or pOper[-1] == "-":
                right_operand = pOp.pop()  # Obtener el operando de la derecha
                left_operand = pOp.pop()  # Obtener el operando de la izquierda
                right_type = pType.pop()  # Obtener el tipo del operando de la derecha
                left_type = pType.pop()  # Obtener el tipo del operando de la izquierda
                operator = pOper.pop()  # Obtener el operador
                result_type = semantic_Cube.getValue(operator, left_type, right_type)  # Obtener el tipo de resultado
                temp = -1
                if result_type == "int":
                    temp = memoria.intTemporal
                    memoria.intTemporal += 1
                    contTempInt += 1
                elif result_type == "float":
                    temp = memoria.floatTemporal
                    memoria.floatTemporal += 1
                    contTempFloat += 1
                elif result_type == "string":
                    temp = memoria.stringTemporal
                    memoria.stringTemporal += 1
                    contTempString += 1
                elif result_type == "boolean":
                    temp = memoria.booleanTemporal
                    memoria.booleanTemporal += 1
                    contTempBool += 1
                existLeft = tablaDeVariables.getVariable(left_operand)
                existRight = tablaDeVariables.getVariable(right_operand)
                if existLeft != None:
                    left_operand = existLeft.dirV
                if existRight != None:
                    right_operand = existRight.dirV
                cuadruplos.addCuadruplo(operator, left_operand, right_operand,temp)  # Crear el cuadruplo
                contVariablesTemporales += 1  # Aumentar el contador de variables temporales
                pOp.append(temp) # Agregar el resultado a la pila de operandos #TODO: Agregar el valor de la variable temporal
                pType.append(result_type) # Agregar el tipo de resultado a la pila de tipos

    #*Funcion para crear el cuadruplo de la multiplicacion y division
    def  cuadruplo_md(self, tree):
        if len(pOper) > 0:
            if pOper[-1] == "*" or pOper[-1] == "/":
                global contVariablesTemporales,contTempInt, contTempFloat, contTempString, contTempBool 
                #! Sacar direcciones de memoria de los operandos
                right_operand = pOp.pop()
                left_operand = pOp.pop()
                right_type = pType.pop()
                left_type = pType.pop()
                operator = pOper.pop()
                result_type = semantic_Cube.getValue(operator, left_type, right_type)
                temp = -1
                if result_type == "int":
                    temp = memoria.intTemporal
                    memoria.intTemporal += 1
                    contTempInt += 1
                elif result_type == "float":
                    temp = memoria.floatTemporal
                    memoria.floatTemporal += 1
                    contTempFloat += 1
                elif result_type == "string":
                    temp = memoria.stringTemporal
                    memoria.stringTemporal += 1
                    contTempString += 1
                elif result_type == "boolean":
                    temp = memoria.booleanTemporal
                    memoria.booleanTemporal += 1
                    contTempBool += 1
                existLeft = tablaDeVariables.getVariable(left_operand)
                existRight = tablaDeVariables.getVariable(right_operand)
                if existLeft != None:
                    left_operand = existLeft.dirV
                if existRight != None:
                    right_operand = existRight.dirV
                cuadruplos.addCuadruplo(operator, left_operand, right_operand,temp)
                contVariablesTemporales += 1
                pOp.append(temp)
                pType.append(result_type)


    #! Funciones para guardar en pila de operandos y tipos
    #* Guardar ID en la pila de operandos
    def guardar_id(self, tree):
        varName = tree.children[0].value
        var = tablaDeVariables.getVariable(varName)
        if var == None:
            print("Error: Variable no declarada")
            exit()
        pOp.append(varName)
        pType.append(var.type)
        pIsVar.append(True)

        #TODO: Guardar el valor en la memoria de constantes

    #*Funcion para guardar un entero en la pila de operandos
    def guardar_int(self, tree):
        global contInt
        # pOp.append(int(tree.children[0].value))
        pType.append("int")
        exist = tablaDeConstantes.alreadyExists(int(tree.children[0].value))
        if exist == False:
            #TODO: Añadir el valor a la pila de memoria de constantes
            dirV = memoria.memoria["constante"]["int"] + contInt
            contInt += 1
            tablaDeConstantes.addConstante(dirV, int(tree.children[0].value), "int")
            pOp.append(dirV)
        else:
            #TODO: Añadir el valor a la pila de memoria de constantes
            dirV = tablaDeConstantes.getDirV(int(tree.children[0].value))
            pOp.append(dirV)

    #* Funcion para guardar un float en la pila de operandos
    def guardar_float(self, tree):
        global contFloat
        # pOp.append(float(tree.children[0].value))
        pType.append("float")
        exist = tablaDeConstantes.alreadyExists(float(tree.children[0].value))
        if exist == False:
            dirV = memoria.memoria["constante"]["float"] + contFloat
            contFloat += 1
            tablaDeConstantes.addConstante(dirV, float(tree.children[0].value), "float")
            pOp.append(dirV)
        else:
            dirV = tablaDeConstantes.getDirV(float(tree.children[0].value))
            pOp.append(dirV)
        #TODO: Guardar el valor en la memoria de constantes

    #* Funcion para guardar un string en la pila de operandos
    def guardar_string(self, tree):
        global contString
        # pOp.append(tree.children[0].value.replace('"', ''))
        pType.append("string")
        exist = tablaDeConstantes.alreadyExists(tree.children[0].value.replace('"', ''))
        if exist == False:
            dirV = memoria.memoria["constante"]["string"] + contString
            contString += 1
            tablaDeConstantes.addConstante(dirV,tree.children[0].value.replace('"', ''), "string")
            pOp.append(dirV)
        else:
            dirV = tablaDeConstantes.getDirV(tree.children[0].value.replace('"', ''))
            pOp.append(dirV)
        #TODO: Guardar el valor en la memoria de constantes

    #* Funcion para guardar un booleano en la pila de operandos
    def guardar_boolean(self, tree):
        global contBool
        dirV = memoria.memoria["constante"]["boolean"] + contBool
        contBool += 1
        if(tree.children[0].value == "true"):
            exist = tablaDeConstantes.alreadyExists("True")
            if exist == False:
                tablaDeConstantes.addConstante(dirV, True, "boolean")
                pOp.append(dirV)
            else:
                dirV = tablaDeConstantes.getDirV("True")
                pOp.append(dirV)
            #TODO: Guardar el valor en la memoria de constantes
            # pOp.append(True) 
        elif (tree.children[0].value == "false"):
            exist = tablaDeConstantes.alreadyExists("False")
            if exist == False:
                tablaDeConstantes.addConstante(dirV, False, "boolean")
                pOp.append(dirV)
            else:
                dirV = tablaDeConstantes.getDirV("False")
                pOp.append(dirV)
            # pOp.append(False)
        pType.append("boolean")
        #TODO: Guardar el valor en la memoria de constantes

    #* Funcion para asignar el valor a una variable
    def np_asignacion(self, tree):
        varValue = pOp.pop() # Obtener el valor de la pila de operandos
        varName = pVars.pop() # Obtener el nombre de la variable
        varType = pType.pop() # Obtener el tipo de la variable #TODO: Verificar que el tipo de la variable sea el mismo que el tipo del valor
        var = tablaDeVariables.getVariable(varName)
        valueDir = -1
        if var.type != varType:
            print("Error: Tipos incompatibles")
            exit()
        # if len(pIsVar) > 0:
        #     pIsVar.pop()
        #     print(varValue)
        #     valueDir = tablaDeVariables.getVariable(varValue)
        #     var.value = valueDir.dirV
        exist = tablaDeVariables.getVariable(varValue)
        if exist != None:
            var.value = exist.dirV
            varValue = exist.dirV
        else:
            var.value = varValue
        tablaDeVariables.updateVariable(var)
        varNameDir = tablaDeVariables.getVariable(varName).dirV
        cuadruplos.addCuadruplo("=", varValue, None, varNameDir) # Crear el cuadruplo de asignacion

    def np_asignacion_2(self, tree):
        varValue = pOp.pop()
        varName = pVars.pop()
        varType = pType.pop()
        # varDir = tablaDeVariables.getVariable(varName).dirV
        var = tablaDeVariables.getVariable(varName)
        if var != None:
            if var.type != varType:
                print("Error: Tipos incompatibles")
                exit()
            var.value = varValue
            tablaDeVariables.updateVariable(var)
            varNameDir = tablaDeVariables.getVariable(varName).dirV
            cuadruplos.addCuadruplo("=", varValue, None, varNameDir)
        else:
            cuadruplos.addCuadruplo("=", varValue, None, varName)
    

    def end(self, tree):
        # print(tablaDeVariables)
        cuadruplos.addCuadruplo("END", None, None, None)
        funcMain = funcDirectory.getFunction("main")
        funcMain.intTemp = contTempInt
        funcMain.floatTemp = contTempFloat
        funcMain.stringTemp = contTempString
        funcMain.boolTemp = contTempBool
        funcMain.intVar = contIntVars
        funcMain.floatVar = contFloatVars
        funcMain.stringVar = contStringVars
        funcMain.booleanVar = contBoolVars
        funcDirectory.updateFunction(funcMain)

        # print('pOper' , pOper)
        # print('pOp' , pOp)
        # print('pType' , pType)
        # print('pSaltos' , pSaltos)
        # print('pContadores' , pContadores)
        # print("\n------- Directorio de funciones -------")
        # funcDirectory.printDirectory()
        # print("\n------- Tabla de Constantes -------")
        # print(tablaDeConstantes)
        cuadruplos.writeCuadruplos()
        tablaDeConstantes.writeTable()
