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
contFor = 0
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
contPointers = 0 # * contador de apuntadores


#* Valores para el uso de recursividad
isRecursive = False
newRecursive = True
recursiveGOTO = -1


class NeuralPoints(Visitor):

    def start(self, tree):
        params = [["page", "string"]]
        var = Variable("page", "string", "N/A", memoria.stringLocal, "local")
        vars = {"page": var}
        funcDirectory.addFunction(Function("newPage", "void", "special", params, vars, 0, 0,0,0,0,0,0,1))
        funcDirectory.addFunction(Function("endPage", "void", "special", params, vars, 0, 0,0,0,0,0,0,1))
        funcDirectory.addFunction(Function("endBody", "void", "special", params, vars, 0, 0,0,0,0,0,0,1))
        funcDirectory.addFunction(Function("startDiv", "void", "special", params, vars, 0, 0,0,0,0,0,0,1))
        funcDirectory.addFunction(Function("endDiv", "void", "special", params, vars, 0, 0,0,0,0,0,0,1))
        funcDirectory.addFunction(Function("newUl", "void", "special", params, vars, 0, 0,0,0,0,0,0,1))
        funcDirectory.addFunction(Function("endUl", "void", "special", params, vars, 0, 0,0,0,0,0,0,1))
        funcDirectory.addFunction(Function("newOl", "void", "special", params, vars, 0, 0,0,0,0,0,0,1))
        funcDirectory.addFunction(Function("endOl", "void", "special", params, vars, 0, 0,0,0,0,0,0,1))
        funcDirectory.addFunction(Function("newLi", "void", "special", params, vars, 0, 0,0,0,0,0,0,1))
        funcDirectory.addFunction(Function("endLi", "void", "special", params, vars, 0, 0,0,0,0,0,0,1))
        funcDirectory.addFunction(Function("newBr", "void", "special", params, vars, 0, 0,0,0,0,0,0,1))
        funcDirectory.addFunction(Function("startTable", "void", "special", params, vars, 0, 0,0,0,0,0,0,1))
        funcDirectory.addFunction(Function("endTable", "void", "special", params, vars, 0, 0,0,0,0,0,0,1))
        funcDirectory.addFunction(Function("startTr", "void", "special", params, vars, 0, 0,0,0,0,0,0,1))
        funcDirectory.addFunction(Function("endTr", "void", "special", params, vars, 0, 0,0,0,0,0,0,1))
        funcDirectory.addFunction(Function("startForm", "void", "special", params, vars, 0, 0,0,0,0,0,0,1))
        funcDirectory.addFunction(Function("endForm", "void", "special", params, vars, 0, 0,0,0,0,0,0,1))
        funcDirectory.addFunction(Function("startNav", "void", "special", params, vars, 0, 0,0,0,0,0,0,1))
        funcDirectory.addFunction(Function("endNav", "void", "special", params, vars, 0, 0,0,0,0,0,0,1))
        funcDirectory.addFunction(Function("newTextArea", "void", "special", params, vars, 0, 0,0,0,0,0,0,1))
        params = [["page", "string"], ["text", "string"]]
        var = Variable("page", "string", "N/A", memoria.stringLocal, "local")
        var2 = Variable("text", "string", "N/A", memoria.stringLocal + 1, "local")
        vars = {"page": var, "text": var2}
        funcDirectory.addFunction(Function("newP", "void", "special", params, vars, 0, 0,0,0,0,0,0,2))
        funcDirectory.addFunction(Function("newLabel", "void", "special", params, vars, 0, 0,0,0,0,0,0,2))
        funcDirectory.addFunction(Function("newB", "void", "special", params, vars, 0, 0,0,0,0,0,0,2))
        funcDirectory.addFunction(Function("newI", "void", "special", params, vars, 0, 0,0,0,0,0,0,2))
        funcDirectory.addFunction(Function("newU", "void", "special", params, vars, 0, 0,0,0,0,0,0,2))
        funcDirectory.addFunction(Function("newButton", "void", "special", params, vars, 0, 0,0,0,0,0,0,2))
        # funcDirectory.addFunction(Function("newA", "void", "special", params, vars, 0, 0,0,0,0,0,0,2))
        funcDirectory.addFunction(Function("newTh", "void", "special", params, vars, 0, 0,0,0,0,0,0,2))
        funcDirectory.addFunction(Function("newTd", "void", "special", params, vars, 0, 0,0,0,0,0,0,2))
        funcDirectory.addFunction(Function("newImg", "void", "special", params, vars, 0, 0,0,0,0,0,0,2))

        params = [["page", "string"], ["size", "int"],["text", "string"]]
        var = Variable("page", "string", "N/A", memoria.stringLocal, "local")
        var2 = Variable("size", "int", "N/A", memoria.intLocal, "local")
        var3 = Variable("text", "string", "N/A", memoria.stringLocal + 1, "local")
        vars = {"page": var, "size": var2, "text": var3}
        funcDirectory.addFunction(Function("newHeader", "void", "special", params, vars, 0,0,0,0,1,0,0,2))

        params = [["page", "string"], ["type", "string"],["id", "string"]]
        var = Variable("page", "string", "N/A", memoria.stringLocal, "local")
        var2 = Variable("type", "string", "N/A", memoria.stringLocal + 1, "local")
        var3 = Variable("id", "string", "N/A", memoria.stringLocal + 2, "local")
        vars = {"page": var, "type": var2, "id": var3}
        funcDirectory.addFunction(Function("newInput", "void", "special", params, vars, 0,0,0,0,0,0,0,3))
        params = [["page", "string"], ["src", "string"],["text", "string"]]
        var = Variable("page", "string", "N/A", memoria.stringLocal, "local")
        var2 = Variable("src", "string", "N/A", memoria.stringLocal + 1, "local")
        var3 = Variable("text", "string", "N/A", memoria.stringLocal + 2, "local")
        vars = {"page": var, "src": var2, "text": var3}
        funcDirectory.addFunction(Function("newA", "void", "special", params, vars, 0, 0,0,0,0,0,0,3))
        


    def np_main(self, tree):
        pSaltos.append(cuadruplos.contador)
        cuadruplos.addCuadruplo("GOTO-MAIN", None, None, "N/A")
        cuadruplos.fillCuadruplo(pSaltos.pop(), cuadruplos.contador)
        #* Resetear el valor de las variables locales
        global contVariablesTemporales, contTempInt, contTempFloat, contTempString, contTempBool, contIntVars, contFloatVars, contStringVars, contBoolVars,contPointers
        contVariablesTemporales = 1
        memoria.intLocal = memoria.memoria["local"]["int"]
        memoria.floatLocal = memoria.memoria["local"]["float"]
        memoria.stringLocal = memoria.memoria["local"]["string"]
        memoria.booleanLocal = memoria.memoria["local"]["boolean"]
        memoria.intTemporal = memoria.memoria["temporal"]["int"]
        memoria.floatTemporal = memoria.memoria["temporal"]["float"]
        memoria.stringTemporal = memoria.memoria["temporal"]["string"]
        memoria.booleanTemporal = memoria.memoria["temporal"]["boolean"]
        memoria.pointerTemporal = memoria.memoria["temporal"]["pointer"]
        contTempInt = 0
        contTempFloat = 0
        contTempString = 0
        contTempBool = 0
        contIntVars = 0
        contFloatVars = 0
        contStringVars = 0
        contBoolVars = 0
        contPointers = 0
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
        tablaDeVariables.addVariableGlobal(Variable(varName, varType, varValue, dirV))
        tablaDeVariables.addVariable(Variable(varName, varType, varValue, dirV))
        # TODO: Usar variables temporales y el valor de la pila de operandos
        # cuadruplos.addCuadruplo("=", varValue, None, varName)
        pVars.append(varName)
        # pType.append(varType)

    # * Funcion para declarar arreglos globales en la tabla de variables
    def compuestoglobal(self, tree):
        x = 1  # TODO: Agregar todo lo del uso de arreglos como variables

    def arreglo(self, tree):
        if len(pOp) < 1:
            global contInt, contPointers
            arrID = tree.children[0].value
            indexDirv = -1
            arrDirv = -1
            arrSizeDirv = -1
            valueDirv = -1
            indexR = -1
            arrType = -1

            arrDirv = tablaDeVariables.getVariable(arrID)

            if arrDirv == None:
                print("Error: Variable " + arrID + " no declarada")
                exit()
            arrType = arrDirv.type
            arrSize = int(arrDirv.size)
            arrSizeDirv = tablaDeConstantes.getDirV(arrSize)

            if arrSizeDirv == None:
                dirV = memoria.memoria["constante"]["int"] + contInt
                contInt += 1
                tablaDeConstantes.addConstante(dirV, arrSize, "int")
                arrSizeDirv = dirV
            arrDirv = arrDirv.dirV
            #! Ya tengo la direccion del arreglo y el tama??o (arrDirv y arrSizeDirv)
            try:
                arrIndex = int(tree.children[2].value)
                constExist = tablaDeConstantes.getDirV(arrIndex)
                if constExist == None:
                    dirV = memoria.memoria["constante"]["int"] + contInt
                    contInt += 1
                    tablaDeConstantes.addConstante(dirV, arrIndex, "int")
                    indexDirv = dirV
                else:
                    indexDirv = constExist
                #! Ya tengo la direccion de memoria del index(indexDirv)
            except:
                arrIndex = tree.children[2].value
                indexDirv = tablaDeVariables.getVariable(arrIndex)
                if indexDirv == None:
                    print("Error: Variable " + arrIndex + " no declarada")
                    exit()
                indexDirv = indexDirv.dirV
                valueDirv = tablaDeVariables.getVariable(arrIndex)
                #! Ya tengo la direccion de memoria del index(indexDirv)
            cuadruplos.addCuadruplo("VER", indexDirv, 0, arrSizeDirv)
            pDirv = memoria.pointerTemporal
            memoria.pointerTemporal += 1
            contPointers += 1
            cuadruplos.addCuadruplo("+A", indexDirv, arrDirv, pDirv)
            pVars.append(pDirv)
            pVars.append(arrID)
            pType.append(arrType)
        else:
            indexDirv = -1
            arrDirv = -1
            arrSize = -1
            arrSizeDirv = -1
            arrID = tree.children[0].value

            arrVar = tablaDeVariables.getVariable(arrID)
            if arrVar == None:
                print("Error: Variable " + arrID + " no declarada")
                exit()
            arrType = arrVar.type
            arrSize = int(arrVar.size)
            arrSizeDirv = tablaDeConstantes.getDirV(arrSize)

            if arrSizeDirv == None:
                dirV = memoria.memoria["constante"]["int"] + contInt
                contInt += 1
                tablaDeConstantes.addConstante(dirV, arrSize, "int")
                arrSizeDirv = dirV
            arrDirv = arrVar.dirV
            #! Ya tengo la direccion del arreglo y el tama??o (arrDirv y arrSizeDirv)
            
            try:
                arrIndex = int(tree.children[2].value)
                constExist = tablaDeConstantes.getDirV(arrIndex)
                if constExist == None:
                    dirV = memoria.memoria["constante"]["int"] + contInt
                    contInt += 1
                    tablaDeConstantes.addConstante(dirV, arrIndex, "int")
                    indexDirv = dirV
                else:
                    indexDirv = constExist
                #! Ya tengo la direccion de memoria del index(indexDirv)
            except:
                arrIndex = tree.children[2].value
                indexDirv = tablaDeVariables.getVariable(arrIndex)
                if indexDirv == None:
                    print("Error: Variable " + arrIndex + " no declarada")
                    exit()
                indexDirv = indexDirv.dirV
                valueDirv = tablaDeVariables.getVariable(arrIndex)
                #! Ya tengo la direccion de memoria del index(indexDirv)
            cuadruplos.addCuadruplo("VER", indexDirv, 0, arrSizeDirv)
            pDirv = memoria.pointerTemporal
            memoria.pointerTemporal += 1
            contPointers += 1
            cuadruplos.addCuadruplo("+A", indexDirv, arrDirv, pDirv)
            pVars.append(pDirv)
            pVars.append(arrID)
            pType.append(arrType)
            cuadruplos.writeCuadruplos()
    
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
        global contIntVars, contFloatVars, contStringVars, contBoolVars
        varName = tree.children[1].value
        # TODO: Agregar el procedimiento para los arreglos
        varSize = tree.children[3].value
        varType = tree.children[6].children[0].value
        if varType == 'int':
            dirV = memoria.intLocal
            memoria.intLocal += int(varSize)
            contIntVars += int(varSize)
        elif varType == 'float':
            dirV = memoria.floatLocal
            memoria.floatLocal += int(varSize)
            contFloatVars += int(varSize)
        elif varType == 'string':
            dirV = memoria.stringLocal
            memoria.stringLocal += int(varSize)
            contStringVars += int(varSize)
        elif varType == 'boolean':
            dirV = memoria.booleanLocal
            memoria.booleanLocal += int(varSize)
            contBoolVars += int(varSize)
        tablaDeVariables.addVariable(Variable(varName, varType, "N/A", dirV, "local", varSize))

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
    
    def asignacioncompleja(self, tree):
        varName = tree.children[0].value
        varIndex = -1 
        arrDirV = -1
        valDirV = -1        
        varIndex = tree.children[2].value
        pVars.append(varName)
        pVars.append(varIndex)    

    def np_arr(self, tree):
        global contInt, contPointers
        index = pVars.pop()
        arr = pVars.pop()
        indexR = -1
        indexDirv = -1
        arrDirV = -1
        valueDirv = -1
        arrSize = -1
        arrSizeDirv = -1

        arrDirV = tablaDeVariables.getVariable(arr)
        if arrDirV == None:
            print("Error: Variable " + arr + " no declarada")
            exit()
        arrSize = int(arrDirV.size)
        arrSizeDirv = tablaDeConstantes.getDirV(arrSize)
        if arrSizeDirv == None:
            dirV = memoria.memoria["constante"]["int"] + contInt
            contInt += 1
            tablaDeConstantes.addConstante(dirV, arrSize, "int")
            arrSizeDirv = dirV
        arrDirV = arrDirV.dirV
        #! YA tengo la direccion del arreglo y su tama??o (arrDirV, arrSizeDirv)
        try:
            indexR = int(index)
            valueDirv = tablaDeConstantes.getDirV(indexR)
            if valueDirv == None:
                
                dirV = memoria.memoria["constante"]["int"] + contInt
                contInt += 1
                tablaDeConstantes.addConstante(dirV, indexR, "int")
                indexDirv = dirV
            else:
                indexDirv = tablaDeConstantes.getDirV(indexR)
        except:
            indexR = index
            indexDirv = tablaDeVariables.getVariable(indexR)
            if indexDirv == None:
                print("Error: Variable ", indexR, "no declarada")
                exit()
            indexDirv = indexDirv.dirV
            valueDirv = tablaDeVariables.getVariable(index)
        #! Ya se tiene la direccion del index (indexDirv)
        cuadruplos.addCuadruplo("VER", indexDirv, 0, arrSizeDirv)
        pDirv = memoria.pointerTemporal
        memoria.pointerTemporal += 1
        contPointers += 1
        cuadruplos.addCuadruplo("+A", indexDirv, arrDirV, pDirv)
        pVars.append(pDirv)
        pVars.append(arr)

    #! Funciones para generacion de cuadruplos del condicional IF
    #* Funcion para a??adir el gotoF a la pila de saltos y crear el cuadruplo
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

    #* Funcion para a??adir un True a la pila de for's anidados
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
        global contFor, contIntVars
        result = pOp.pop()
        varName = pVars.pop()
        varType = pType.pop()
        #TODO: A??adir contador de VC para manejar anidados, y buscar la dirv de variable y VC y VF
        #TODO: Checar la direcion de VC < VF
        contFor += 1
        varNameDir = tablaDeVariables.getVariable(varName).dirV
        cuadruplos.addCuadruplo("=", result, None, varNameDir) 
        dirV = memoria.intLocal
        memoria.intLocal += 1
        contIntVars += 1
        tablaDeVariables.addVariable(Variable("VC" + str(contFor-1), "int", "N/A", dirV))
        cuadruplos.addCuadruplo("=", varNameDir, None, dirV)

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
        global contVariablesTemporales, contFor, contInt, contIntVars, contTempInt
        pContador = pContadores.pop()
        temp = memoria.intTemporal
        memoria.intTemporal += 1
        dirVC = tablaDeVariables.getVariable("VC" + str(contFor-1)).dirV
        # cont = tablaDeConstantes.getConstante(pContador[2]).dirC
        cont = -1
        exist = tablaDeConstantes.alreadyExists(int(pContador[2]))
        if exist == False:
            #TODO: A??adir el valor a la pila de memoria de constantes
            dirV = memoria.memoria["constante"]["int"] + contInt
            contInt += 1
            tablaDeConstantes.addConstante(dirV, int(pContador[2]), "int")
            cont = dirV 
            # pOp.append(dirV)
        else:
            #TODO: A??adir el valor a la pila de memoria de constantes
            cont = tablaDeConstantes.getDirV(int(pContador[2]))
            # pOp.append(dirV)
        cuadruplos.addCuadruplo(pContador[1], dirVC, cont,  temp)
        contVariablesTemporales += 1
        cuadruplos.addCuadruplo("=", temp, None, dirVC)
        contTempInt += 1
        dirContador = tablaDeVariables.getVariable(pContador[0]).dirV
        cuadruplos.addCuadruplo("=", temp, None, dirContador)
        contTempInt += 1
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
        #Resetea los contadores de variables y temporales
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
        dirFuncVar = -1
        #Agrega la variable global con tipo de la funcion
        if funcType == "int":
            dirFuncVar = memoria.intGlobal
            memoria.intGlobal += 1
        elif funcType == "float":
            dirFuncVar = memoria.floatGlobal
            memoria.floatGlobal += 1
        elif funcType == "string":
            dirFuncVar = memoria.stringGlobal
            memoria.stringGlobal += 1
        elif funcType == "boolean":
            dirFuncVar = memoria.booleanGlobal
            memoria.booleanGlobal += 1
        tablaDeVariables.addVariableGlobal(Variable(varName, funcType, "N/A", dirFuncVar))
        global funcVars
        #Guarda las variables y sus tipos de los parametros utilizados en la funcion
        for var in vars:
            if var == "int" or var == "float" or var == "string" or var == "boolean":
                pType.append(var.value)
            elif var == ',' or var == ':':
                pass
            else:
                pOp.append(var.value)
                funcVars +=1

    def funcionvoid(self,tree):
        funcName = tree.children[1].value
        funcType = tree.children[7].value
        pOp.append(funcName)
        pType.append(funcType)
        pContexto.append(funcName) # Agregar el nombre de la funcion a la pila de contexto
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

    #Funcion que se encarga de crear la funcion en el directorio de funciones y agregar sus variables
    def np_func_id(self,tree):
        global funcVars, contIntVars, contFloatVars, contStringVars, contBoolVars
        params = [] #Lista de parametros
        pOp.reverse()
        pType.reverse()
        funcName = pOp.pop()
        funcType = pType.pop()
        dirV = -1
        for i in range(funcVars):

            varType = pType.pop()
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
            
            varName = pOp.pop()
            tablaDeVariables.addVariable(Variable(varName, varType, "N/A", dirV, "local"))
            params.append([ varName, varType])
        funcVars = 0
        func = Function(funcName, funcType, cuadruplos.contador, params) # Crear funcion
        funcDirectory.addFunction(func) # Agregar funcion al directorio de funciones

    def np_func_result(self,tree):
        global funcVars, isRecursive, recursiveGOTO, newRecursive
        funcVars = 0
        exist = tablaDeVariables.getVariable(pOp[-1])
        #! A??adir resultado a la tabla de variable de globales
        funcDirVGlobal = tablaDeVariables.getVariableGlobal(pContexto[-1]).dirV        
        

        if exist != None:
            cuadruplos.addCuadruplo("RETURN", funcDirVGlobal, None, exist.dirV)
            if isRecursive and newRecursive:
                recursiveGOTO = cuadruplos.contador
                cuadruplos.addCuadruplo("GOTO", None, None, "N/A")
                newRecursive = False
        else:
            cuadruplos.addCuadruplo("RETURN", funcDirVGlobal, None, pOp[-1])
            if isRecursive and newRecursive:
                recursiveGOTO = cuadruplos.contador
                cuadruplos.addCuadruplo("GOTO", None, None, "N/A")
                newRecursive = False
        
        

        funcType = pType.pop() # Tipo de la funcion
        result = pOp.pop() # Nombre de la funcion
        value = "Get Result" #Get value of var
        pResultFuncs.append([result, funcType, value]) # Agregar funcion a la pila de funciones con resultado
        # pIsVar.pop() # Quitar bandera de variable de la pila de banderas
    def returnv(self,tree):
        global isRecursive
        isRecursive = True

    # Actualiza los contadores de variables y temporales y los resetea
    def np_end_func(self, tree):
        global contVariablesTemporales, contTempInt, contIntVars, contInt, contFloatVars, contFloat, contBoolVars, contBool, contStringVars, contString, contTempFloat, contTempBool, contTempString, contPointers, isRecursive, recursiveGOTO
        if len(pIsVar) > 0:
            pIsVar.pop()
        # memoria.booleanLocal = memoria.memoria["local"]["boolean"]
        # memoria.intTemporal = memoria.memoria["temporal"]["int"]
        contVInt = memoria.intLocal - memoria.memoria["local"]["int"] 
        contVFloat = memoria.floatLocal - memoria.memoria["local"]["float"] 
        contVString = memoria.stringLocal - memoria.memoria["local"]["string"] 
        contVBoolean = memoria.booleanLocal - memoria.memoria["local"]["boolean"] 
        contTInt = memoria.intTemporal - memoria.memoria["temporal"]["int"]
        contTFloat = memoria.floatTemporal - memoria.memoria["temporal"]["float"]
        contTString = memoria.stringTemporal - memoria.memoria["temporal"]["string"]

        cuadruplos.addCuadruplo("ENDFUNC", None, None, None)
        if isRecursive:
            cuadruplos.fillCuadruplo(recursiveGOTO, cuadruplos.contador-1)
            isRecursive = False

        funcName = pContexto.pop()
        function = funcDirectory.getFunction(funcName)
        function.variables = tablaDeVariables.variables
        function.intTemp = contTInt
        function.floatTemp = contTFloat
        function.stringTemp = contTString
        function.booleanTemp = contTString
        function.intVar = contVInt
        function.floatVar = contVFloat
        function.stringVar = contVString
        function.booleanVar = contVBoolean
        function.pointerTemp = contPointers
        funcDirectory.updateFunction(function)
        tablaDeVariables.resetTable()
        
        contVariablesTemporales = 1
        memoria.intLocal = memoria.memoria["local"]["int"]
        memoria.floatLocal = memoria.memoria["local"]["float"]
        memoria.stringLocal = memoria.memoria["local"]["string"]
        memoria.booleanLocal = memoria.memoria["local"]["boolean"]
        memoria.intTemporal = memoria.memoria["temporal"]["int"]
        memoria.floatTemporal = memoria.memoria["temporal"]["float"]
        memoria.stringTemporal = memoria.memoria["temporal"]["string"]
        memoria.booleanTemporal = memoria.memoria["temporal"]["boolean"]
        memoria.pointerTemporal = memoria.memoria["temporal"]["pointer"]
        contTempInt = 0
        contTempFloat = 0
        contTempString = 0
        contTempBool = 0
        contIntVars = 0
        contFloatVars = 0
        contStringVars = 0
        contBoolVars = 0
        contPointers = 0

    #! Funciones para cuadruplos de llamada a funciones
    def llamadavoid(self, tree):
        global pVars
        funcID = tree.children[0].value
        pVars.append(funcID)

    def llamadafunc(self, tree):
        global pVars
        funcID = tree.children[0].value
        pVars.append(funcID)
    
    #* Funcion para agregar cuadruplos de llamada a funciones
    #* Agrega el Era, los parametros y el GOSUB
    #Y si es una funcion con resultado, agrega el parametro de retorno
    def np_func_vars(self, tree):
        global pVars, isRecursive
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
            cuadruplos.writeCuadruplos()
            #! Agrega las variables en el caso de que sea una recusion
            if(len(function.variables)) == 0:
                
                function.variables = tablaDeVariables.variables
                funcDirectory.updateFunction(function)
                isRecursive = True
                

            varDir = function.variables[function.params[i][0]].dirV
            if exist != None:
                cuadruplos.addCuadruplo("PARAM", exist.dirV, None, varDir)
            else:
                cuadruplos.addCuadruplo("PARAM", funcVars[i][0], None, varDir)
        cuadruplos.addCuadruplo("GOSUB", None, None, function.dirV)
        # if function.dirV == "special":
        #     cuadruplos.addCuadruplo("ENDFUNC", None, None, None)
        if function.type != "void":
            global contTempInt, contTempFloat, contTempString, contTempBool
            dirGlobal = tablaDeVariables.getVariableGlobal(function.name).dirV
            temp = -1
            if function.type == "int":
                temp = memoria.intTemporal
                memoria.intTemporal += 1
                contTempInt += 1
                pType.append("int")
            elif function.type == "float":
                temp = memoria.floatTemporal
                memoria.floatTemporal += 1
                contTempFloat += 1
                pType.append("float")
            elif function.type == "string":
                temp = memoria.stringTemporal
                memoria.stringTemporal += 1
                contTempString += 1
                pType.append("string")
            elif function.type == "boolean":
                temp = memoria.booleanTemporal
                memoria.booleanTemporal += 1
                contTempBool += 1
                pType.append("boolean")
            cuadruplos.addCuadruplo("=", dirGlobal, None, temp)
            pOp.append(temp)

    #! Funciones para Read
    def read(self,tree):
        varID = tree.children[2].value
        exist = tablaDeVariables.getVariable(varID)
        if exist == None:
            print("Error: Variable " + varID + " no declarada")
            exit()
        varType = exist.type
        cuadruplos.addCuadruplo("READ", None, None, exist.dirV)

    #! Funciones para escritura
    def escritura(self, tree):
        arrID = -1
        index = -1
        try:
            arrID = tree.children[2].children[0].value
            try:
                index = int(tree.children[2].children[2].value)
                var = tablaDeVariables.getVariable(arrID)
                indexID = var.dirV
                if var == None:
                    print("Error: Variable " + arrID + " no declarada")
                    exit()
                if var.type != "int":
                    print("Error: El indice del arreglo debe ser de tipo int")
                    exit()
                varSize = int(var.size)
                if index >= varSize:
                    print("Error: El indice del arreglo excede el tama??o del arreglo")
                    exit()
                dirV = indexID + index
                pOp.append(dirV)
                pType.append(var.type)
            except:
                index = tree.children[2].children[2].value
                var = tablaDeVariables.getVariable(index)
                array = tablaDeVariables.getVariable(arrID)
                arrSize = int(array.size)
                index = -1
                if var.value >= 20000 and var.value < 29000:
                    index = tablaDeConstantes.getConstante(var.value)
                    dirV = array.dirV + index
                    if var == None:
                        print("Error: Variable " + index + " no declarada")
                        exit()
                    if var.type != "int":
                        print("Error: El indice del arreglo debe ser de tipo int")
                        exit()
                    varSize = int(var.size)
                    if int(index) >= arrSize:
                        print("Error: El indice del arreglo excede el tama??o del arreglo")
                        exit()
                    pOp.append(dirV)
                    pType.append(var.type)
                else:
                    index = var.value
                    dirV = index
                    varSize = int(var.size)
                    pOp.append(dirV)
                    pType.append(var.type)
                
        except:
            pass

    #Obtener apuntador del arreglo
    # def escriturax(self, tree):
    #     pOp.append(99999)
    

    def np_escritura(self, tree):
        #Print arr con contador
        if len(pOp) == 0:
            x = 0
        else:
            value = pOp.pop()
            pType.pop()
            exist = tablaDeVariables.getVariable(value)
            dirV = -1
            if exist != None:
                if exist.value == "N/A":
                    dirV = exist.dirV
                elif exist.value >= 42000:
                    dirV = exist.value
                else:
                    dirV = exist.dirV
            else:
                dirV = value
            cuadruplos.addCuadruplo("PRINT", None, None, dirV)

    #! Funciones para operaciones aritmeticas

    # *Funcion para a??adir el simbolo de suma o resta a la pila de operadores
    def expy(self, tree):
        pOper.append(tree.children[0].value)

    # *Funcion para a??adir el simbolo de multiplicacion o division a la pila de operadores
    def terminoy(self, tree):
        pOper.append(tree.children[0].value)

    #* Funcion para a??adir los simbolos logicos a la pila de operadores
    def np_logico(self, tree):
        pOper.append(tree.children[0].value)

    #* Funcion para crear el cuadruplo logico
    def np_logico_2(self, tree):
        global contVariablesTemporales, contTempBool
        cuadruplos.writeCuadruplos

        # if len(pVars) > 0:
        #     if len(pVars) == 2:
        #         pVars.pop()
        #     elif len(pVars) == 4:
        #         x=1
        #     else:
        #         pass
             

        if len(pOper) > 0:

            if len(pVars) == 2:
                pVars.pop()
                right_operand = pVars.pop()
                left_operand = pOp.pop()
                operator = pOper.pop()
                right_type = pType.pop()
                left_type = pType.pop()
                result_type = semantic_Cube.getValue(operator,left_type, right_type)
                if result_type == "error":
                    print("Error: Tipos incompatibles en operacion logica")
                    exit()
                temp = memoria.booleanTemporal
                existLeft = tablaDeVariables.getVariable(left_operand)
                if existLeft != None:
                    left_operand = existLeft.dirV
                cuadruplos.addCuadruplo(operator + 'A', left_operand, right_operand, temp)
                memoria.booleanTemporal += 1
                contTempBool += 1
                pOp.append(temp)
                pType.append(result_type)


            else:
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
                if pFor != []: #Si hay un for entonces a??adir los cuadruplos de igual a VF y comparacion de VC y VF
                    global contTempInt, contIntVars
                    pFor.pop()
                    global contFor
                    dirV = memoria.intLocal
                    memoria.intLocal += 1
                    tablaDeVariables.addVariable(Variable("VF" + str(contFor-1), "int", "N/A", dirV))
                    cuadruplos.addCuadruplo("=", right_operand, None, dirV)
                    contIntVars += 1
                    pSaltos.append(cuadruplos.contador)
                    temp = memoria.booleanTemporal
                    dirVC = tablaDeVariables.getVariable("VC" + str(contFor-1)).dirV
                    cuadruplos.addCuadruplo("<", dirVC, dirV,temp)
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

            if len(pVars) >= 4:
                pVars.pop()
                right_operand = pVars.pop()
                right_type = pType.pop()
                pVars.pop()
                left_operand = pVars.pop()
                left_type = pType.pop()
                operator = pOper.pop()
                result_type = semantic_Cube.getValue(operator,left_type, right_type)
                if result_type == "error":
                    print("Error: Tipo de dato no valido")
                    exit()
                temp = memoria.intTemporal
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
                elif result_type == "bool":
                    temp = memoria.booleanTemporal
                    memoria.booleanTemporal += 1
                    contTempBool += 1
                pOp.append(temp)
                pType.append(result_type)
                cuadruplos.addCuadruplo(operator, left_operand, right_operand,temp) 
            else:
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
            #TODO: A??adir el valor a la pila de memoria de constantes
            dirV = memoria.memoria["constante"]["int"] + contInt
            contInt += 1
            tablaDeConstantes.addConstante(dirV, int(tree.children[0].value), "int")
            pOp.append(dirV)
        else:
            #TODO: A??adir el valor a la pila de memoria de constantes
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
        #! Caso de igualar arreglos
        if len(pVars) == 4:
            pVars.pop()
            resultDirv = pVars.pop()
            pVars.pop()
            leftDirv = pVars.pop()
            cuadruplos.addCuadruplo("=", resultDirv, None, leftDirv)
        elif len(pVars) == 3:
            pVars.pop()
            resultDirv = pVars.pop()
            leftDirv = pVars.pop()

            exist = tablaDeVariables.getVariable(leftDirv)
            if exist == None:
                print("Error: Variable ", leftDirv, " no declarada")
                exit()
            leftDirv = exist.dirV
            exist.value = resultDirv
            tablaDeVariables.updateVariable(exist)

            cuadruplos.addCuadruplo("=A", resultDirv, None, leftDirv)
        else:
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
            
            if int(var.size) != -1:
                dirV = pVars.pop()
                cuadruplos.addCuadruplo("=", varValue, None, dirV) # Crear el cuadruplo de asignacion
            else:
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
        funcMain.pointerTemp = contPointers
        funcDirectory.updateFunction(funcMain)

        # print("pVars",pVars)
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
 