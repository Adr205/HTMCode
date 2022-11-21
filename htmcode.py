import ast
from classes.NeuralPoints import *
from classes.Memoria import *
from classes.FunctionDirectory import *
from classes.VariablesTable import *

'''
    TODO:   Guardar variables globales a memoria virtual global
        #!  Hacer que la maquina virtual realize el ciclo FOR
            Hacer la maquina virtual y minimo que resuelva las expresiones aritmeticas y logicas #! Falta hacer <=, >=, !=, ==, and, or
            Hacer la llamada a funciones tipadas
            Guardar el resultado de la funcion en una variable global con el nombre de la funcion
            Todo el codigo de Arreglos
        #!  Arreglar la commutividad por derecha y hacerla por izquierda
        #!  Añadir el uso de parentesis para las expresiones

    TODO: #! Ejemplos de codigo obligatorios
        Factorial recursivo
        Fibonacci recursivo
        Sort de un arreglo
        Find de un arreglo
        Pruebas propias del lenguaje

'''
# Direcciones base de memoria local y temporal para cada tipo de variable
dirIntVar = memoria.memoria['local']['int']
dirFloatVar = memoria.memoria['local']['float']
dirStringVar = memoria.memoria['local']['string']
dirBoolVar = memoria.memoria['local']['boolean']
dirIntTemp = memoria.memoria['temporal']['int']
dirFloatTemp = memoria.memoria['temporal']['float']
dirStringTemp = memoria.memoria['temporal']['string']
dirBoolTemp = memoria.memoria['temporal']['boolean']


memoriaVirtual = memoria.memoriaVirtual
memorias = [] #* Lista de memorias virtuales
goBack = []
cuadruplos = []
tablaConst = {}
tablaGlobal = tablaDeVariables.globales
cuadPointer = 0
tablaVariable = []
dirFunc = {}

def readConstantes():
    c = open('constantes.txt', 'r')
    constantes = c.readlines()
    for constante in constantes:
        dirV,val, typ = constante.split(",")
        dirV = dirV.split('[')[1]
        dirV = int(dirV)
        typ = typ.split(']')[0]
        typ = typ[2:-1]
        if typ == 'int':
            val = int(val)
        elif typ == 'float':
            val = float(val)
        elif typ == 'string':
            val = val[2:-1]
        elif typ == 'boolean':
            if val == ' True':
                val = True
            else:
                val = False
        # tablaConst.append([dirV, val, typ])
        tablaConst[dirV] = [val, typ]

    # print(tablaConst)

def readCuadruplos():
    c = open('cuadruplos.txt', 'r')
    cuadrups = c.readlines()
    # erase \n from each line
    cuadrups = [x.strip() for x in cuadrups]
    # print(cuadrups)
    for cuadruplo in cuadrups:
        cuad = ast.literal_eval(cuadruplo)
        cuadruplos.append(cuad)

#* Funcion para llenar la memoria virtual con las temporales y variables necesarias para la funcion
def fillMemory(funcName):
    func = dirFunc[funcName]
    # print(func.intTemp, func.floatTemp, func.stringTemp, func.boolTemp)
    # print(func.intVar, func.floatVar, func.stringVar, func.booleanVar)
    if func.intVar > 0:
        for i in range(func.intVar):
            memoriaVirtual[dirIntVar + i] = None
    if func.floatVar > 0:
        for i in range(func.floatVar):
            memoriaVirtual[dirFloatVar + i] = None
    if func.stringVar > 0:
        for i in range(func.stringVar):
            memoriaVirtual[dirStringVar + i] = None
    if func.booleanVar > 0:
        for i in range(func.booleanVar):
            memoriaVirtual[dirBoolVar + i] = None
    if func.intTemp > 0:
        for i in range(func.intTemp):
            memoriaVirtual[dirIntTemp + i] = None
    if func.floatTemp > 0:
        for i in range(func.floatTemp):
            memoriaVirtual[dirFloatTemp + i] = None
    if func.stringTemp > 0:
        for i in range(func.stringTemp):
            memoriaVirtual[dirStringTemp + i] = None
    if func.booleanTemp > 0:
        for i in range(func.boolTemp):
            memoriaVirtual[dirBoolTemp + i] = None

def saveMemory():
    memorias.append(memoriaVirtual.copy())
    memoriaVirtual.clear()

def findMain():
    global cuadPointer
    for cuadruplo in cuadruplos:
        if cuadruplo[0] == 'GOTO-MAIN':
            cuadPointer = cuadruplo[3]
            break

def htmlCode():
    global cuadPointer, memoriaVirtual, goBack
    operator = cuadruplos[cuadPointer][0]
    first = False
    while operator != 'END':
        # print(cuadPointer)
        operator = cuadruplos[cuadPointer][0]
        left = cuadruplos[cuadPointer][1]
        right = cuadruplos[cuadPointer][2]
        result = cuadruplos[cuadPointer][3]

        if operator != '=' and first != True :
            first = True
            findMain()
        elif operator == 'GOTO-MAIN':
            fillMemory("main")
            cuadPointer = int(result)
        elif operator == 'ERA':
            saveMemory()
            fillMemory(result)
            cuadPointer += 1
        elif operator == 'PARAM':
            if left in tablaConst:
                memoriaVirtual[result] = tablaConst[left][0]
            else:
                
                memoriaVirtual[result] = memorias[len(memorias)-1][left]
            cuadPointer += 1
        elif operator == 'GOSUB':
            goBack.append(cuadPointer + 1)
            cuadPointer = int(result)
        elif operator == 'ENDFUNC':
            cuadPointer = goBack.pop()
            memoriaVirtual = memorias.pop()
        elif operator == '+':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            elif left >= 1000 and left < 9000:
                var = tablaDeVariables.getVariableGlobalID(left)
                left = var.value
            else:
                # print(memoriaVirtual)
                # print(left)
                left = memoriaVirtual[left]
            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val
            elif right >= 1000 and right < 9000:
                var = tablaDeVariables.getVariableGlobalID(right)
                right = var.value
            else:
                right = memoriaVirtual[right]
            memoriaVirtual[result] = left + right
            cuadPointer += 1
        elif operator == '-':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]
            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val
            else:
                right = memoriaVirtual[right]
            memoriaVirtual[result] = left - right
            cuadPointer += 1
        elif operator == '*':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]
            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val
            else:
                right = memoriaVirtual[right]
            memoriaVirtual[result] = left * right
            cuadPointer += 1
        elif operator == '/':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]
            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    left = val
                        
            else:
                right = memoriaVirtual[right]
            memoriaVirtual[result] = left / right
            cuadPointer += 1

        elif operator == '=':
            if result >= 1000 and result < 9000:
                if left >= 20000 and left < 29000:
                    val,type = tablaConst[left]
                    if type == 'int':
                        left = int(val)
                    elif type == 'float':
                        left = float(val)
                    elif type == 'string':
                        left = val
                    elif type == 'boolean':
                        left = val
                elif left >= 1000 and left < 9000:
                    left = tablaGlobal[left]
                else:
                    left = memoriaVirtual[left]
                
                var = tablaDeVariables.getVariableGlobalID(result)
                var.value = left
                tablaDeVariables.updateVariableGlobal(var)
                
            else:
                if left >= 20000 and left < 29000:
                    val,type = tablaConst[left]
                    if type == 'int':
                        left = int(val)
                    elif type == 'float':
                        left = float(val)
                    elif type == 'string':
                        left = val
                    elif type == 'boolean':
                        left = val
                elif left >= 1000 and left < 9000:
                    left = tablaGlobal[left]
                else:
                    left = memoriaVirtual[left]

                memoriaVirtual[result] = left
            cuadPointer += 1
        elif operator == '++':
            # ['++', 10003, 1, 30004]
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]
            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val
            else:
                right = memoriaVirtual[right]
            memoriaVirtual[result] = left + right
            cuadPointer += 1
        elif operator == '<':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]
            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val
            else:
                right = memoriaVirtual[right]
            if left < right:
                memoriaVirtual[result] = True
            else:
                memoriaVirtual[result] = False
            cuadPointer += 1
        elif operator == '>':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]
            if right >= 20000 and right < 29000:
                val,type = tablaConst[right]
                if type == 'int':
                    right = int(val)
                elif type == 'float':
                    right = float(val)
                elif type == 'string':
                    right = val
                elif type == 'boolean':
                    right = val
            else:
                right = memoriaVirtual[right]
            if left > right:
                memoriaVirtual[result] = True
            else:
                memoriaVirtual[result] = False
            cuadPointer += 1
        elif operator == 'GOTOF':
            if left >= 20000 and left < 29000:
                val,type = tablaConst[left]
                if type == 'int':
                    left = int(val)
                elif type == 'float':
                    left = float(val)
                elif type == 'string':
                    left = val
                elif type == 'boolean':
                    left = val
            else:
                left = memoriaVirtual[left]
            if left == False:
                cuadPointer = result
            else:
                cuadPointer += 1
        elif operator == 'GOTO':
            cuadPointer = result
        elif operator == 'PRINT':
            if result >= 20000 and result < 29000:
                val,type = tablaConst[result]
                if type == 'int':
                    result = str(int(val))
                elif type == 'float':
                    result = str(float(val))
                elif type == 'string':
                    result = val
                elif type == 'boolean':
                    result = val
            elif result >= 1000 and result < 9000:
                # tablaDeVariables.printGlobales()
                var = tablaDeVariables.getVariableGlobalID(result)
                result = var.value
                # result = 99
            else:
                result = memoriaVirtual[result]
            print(result)
            cuadPointer += 1
        elif operator == 'RETURN':
            if result >= 20000 and result < 29000:
                val,type = tablaConst[result]
                if type == 'int':
                    result = int(val)
                elif type == 'float':
                    result = float(val)
                elif type == 'string':
                    result = val
                elif type == 'boolean':
                    result = val
            else:
                result = memoriaVirtual[result]
            tablaGlobal[left] = result
            cuadPointer += 1
        


            
        
def suma(left,right):
    return left + right

    


def virtualMachine():
    global tablaVariables, dirFunc
    tablaVariables = tablaDeVariables
    dirFunc = funcDirectory.funcDirectory
    # print(tabla)
    # print(tablaGlobal)

    readConstantes()
    readCuadruplos()
    htmlCode()