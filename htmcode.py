import ast
from classes.NeuralPoints import *
from classes.Memoria import *
from classes.FunctionDirectory import *
from classes.VariablesTable import *
from classes.specialFuncs import *
import time 

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
dirPointerTemp = memoria.memoria['temporal']['pointer']


memoriaVirtual = memoria.memoriaVirtual
memorias = [] #* Lista de memorias virtuales
goBack = []
cuadruplos = []
tablaConst = {}
tablaGlobal = tablaDeVariables.globales
cuadPointer = 0
tablaVariable = []
dirFunc = {}
pContexto = ["global"]
onFunc = False

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
    if func.pointerTemp > 0:
        for i in range(func.pointerTemp):
            memoriaVirtual[dirPointerTemp + i] = None

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
    global cuadPointer, memoriaVirtual, goBack, onFunc
    operator = cuadruplos[cuadPointer][0]
    first = False
    while operator != 'END':
        operator = cuadruplos[cuadPointer][0]
        left = cuadruplos[cuadPointer][1]
        right = cuadruplos[cuadPointer][2]
        result = cuadruplos[cuadPointer][3]

        if operator != '=' and first != True :
            first = True
            findMain()
            fillMemory('main')
        elif operator == 'GOTO-MAIN':
            fillMemory("main")
            cuadPointer = int(result)
        elif operator == 'ERA':
            saveMemory()
            fillMemory(result)
            pContexto.append(result)
            cuadPointer += 1
        elif operator == 'PARAM':
            if left in tablaConst:
                memoriaVirtual[result] = tablaConst[left][0]
            else:
                memoriaVirtual[result] = memorias[len(memorias)-1][left]
            cuadPointer += 1
        elif operator == 'GOSUB':
            
            if result != "special":
                goBack.append(cuadPointer + 1)
                cuadPointer = int(result)
            else:
                if onFunc == False:
                    goBack.append(cuadPointer + 1)
                    specialFuncs(pContexto[-1])
                    onFunc = True
                else:
                    #delay 1 second
                    # time.sleep(0.1)
                    cuadPointer = goBack.pop()
                    memoriaVirtual = memorias.pop()
                    onFunc = False
                    pass
            
        elif operator == 'ENDFUNC':
            cuadPointer = goBack.pop()
            memoriaVirtual = memorias.pop()
            pContexto.pop()
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
        elif operator == '+A':
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
            memoriaVirtual[result] = left + int(right)
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
            if right == 0:
                print("ERROR: Division by zero")
                exit()
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
            elif result >= 42000:
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
                elif left >= 42000:
                    print(left)
                    print(memoriaVirtual)
                    dirLeft = memoriaVirtual[left]
                    print(left)
                    left = memoriaVirtual[dirLeft]
                else:
                    left = memoriaVirtual[left]
                varResult = memoriaVirtual[result]
                memoriaVirtual[varResult] = left
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
        elif operator == '--':
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
        elif operator == '==':
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
                valLeft = memoriaVirtual[left]
                if valLeft >= 42000:
                    if left >= 10000 and left < 13000:
                        left = memoriaVirtual[valLeft]
                        left = int(memoriaVirtual[left])
                else:
                    left = valLeft

            

            
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
                valRight = memoriaVirtual[right]
                if valRight >= 42000:
                    print(right)
                else:
                    right = valRight

            if left == right:
                memoriaVirtual[result] = True
            else:
                memoriaVirtual[result] = False
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
        elif operator == '<=':
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
            if left <= right:
                memoriaVirtual[result] = True
            else:
                memoriaVirtual[result] = False
            cuadPointer += 1
        elif operator == '>=':
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
            if left >= right:
                memoriaVirtual[result] = True
            else:
                memoriaVirtual[result] = False
            cuadPointer += 1
        elif operator == '!=':
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
            if left != right:
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
        elif operator == 'READ':
            if result >= 1000 and result < 9000:
                var = tablaDeVariables.getVariableGlobalID(result)
                var.value = input( )
                tablaDeVariables.updateVariableGlobal(var)
            else:
                if result >= 10000 and result < 13000:
                    memoriaVirtual[result] = int(input( ))
                elif result >= 13000 and result < 15000:
                    memoriaVirtual[result] = float(input( ))
                elif result >= 15000 and result < 17000:
                    memoriaVirtual[result] = input( )
                elif result >= 17000 and result < 19000:
                    if input( ) == 'True':
                        memoriaVirtual[result] = True
                    else:
                        memoriaVirtual[result] = False
            cuadPointer += 1
        elif operator == 'and':
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
            if left and right:
                memoriaVirtual[result] = True
            else:
                memoriaVirtual[result] = False
            cuadPointer += 1
        elif operator == 'or':
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
            if left or right:
                memoriaVirtual[result] = True
            else:
                memoriaVirtual[result] = False
            cuadPointer += 1
        elif operator == 'not':
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
                memoriaVirtual[result] = True
            else:
                memoriaVirtual[result] = False
            cuadPointer += 1
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
            elif result >= 42000:
                pointer = memoriaVirtual[result]
                result = memoriaVirtual[pointer]
                
            else:
                result = memoriaVirtual[result]
            print(result)
            cuadPointer += 1
        elif operator == '=A':
            memoriaVirtual[result] = left
            cuadPointer += 1
        elif operator == 'VER':
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

            if left < 0 or left >= result:
                print('Error: Index out of range')
                exit()
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
    createRepository()
    htmlCode()



def specialFuncs(funcName):
    global onFunc, cuadPointer
    if funcName == 'newPage':
        # print(memoriaVirtual[15000])
        newPage(memoriaVirtual[15000])
    elif funcName == 'endPage':
        endPage(memoriaVirtual[15000])
    elif funcName == 'endBody':
        endBody(memoriaVirtual[15000])
    elif funcName == 'startDiv':
        startDiv(memoriaVirtual[15000])
    elif funcName == 'endDiv':
        endDiv(memoriaVirtual[15000])
    elif funcName == 'newUl':
        newUl(memoriaVirtual[15000])
    elif funcName == 'endUl':
        endUl(memoriaVirtual[15000])
    elif funcName == 'newLi':
        newLi(memoriaVirtual[15000])
    elif funcName == 'endLi':
        endLi(memoriaVirtual[15000])
    elif funcName == 'newOl':
        newOl(memoriaVirtual[15000])
    elif funcName == 'endOl':
        endOl(memoriaVirtual[15000])
    elif funcName == 'newBr':
        newBr(memoriaVirtual[15000])
    elif funcName == 'startTable':
        startTable(memoriaVirtual[15000])
    elif funcName == 'endTable':
        endTable(memoriaVirtual[15000])
    elif funcName == 'startTr':
        startTr(memoriaVirtual[15000])
    elif funcName == 'endTr':
        endTr(memoriaVirtual[15000])
    elif funcName == 'startForm':
        startForm(memoriaVirtual[15000])
    elif funcName == 'endForm':
        endForm(memoriaVirtual[15000])
    elif funcName == 'startNav':
        startNav(memoriaVirtual[15000])
    elif funcName == 'endNav':
        endNav(memoriaVirtual[15000])
    elif funcName == 'newTextArea':
        newTextArea(memoriaVirtual[15000])
    elif funcName == 'newTh':
        newTh(memoriaVirtual[15000], memoriaVirtual[15001])
    elif funcName == 'newTd':
        newTd(memoriaVirtual[15000], memoriaVirtual[15001])
    elif funcName == 'newP':
        newP(memoriaVirtual[15000], memoriaVirtual[15001])
    elif funcName == 'newLabel':
        newLabel(memoriaVirtual[15000], memoriaVirtual[15001])
    elif funcName == 'newB':
        newB(memoriaVirtual[15000], memoriaVirtual[15001])
    elif funcName == 'newI':
        newI(memoriaVirtual[15000], memoriaVirtual[15001])
    elif funcName == 'newU':
        newU(memoriaVirtual[15000], memoriaVirtual[15001])
    elif funcName == 'newButton':
        newButton(memoriaVirtual[15000], memoriaVirtual[15001])
    elif funcName == 'newA':
        newA(memoriaVirtual[15000], memoriaVirtual[15001], memoriaVirtual[15002])
    elif funcName == 'newHeader':
        newHeader(memoriaVirtual[15000], memoriaVirtual[10000], memoriaVirtual[15001])
    elif funcName == 'newInput':
        newInput(memoriaVirtual[15000], memoriaVirtual[15001], memoriaVirtual[15002])
    elif funcName == 'newImg':
        newImg(memoriaVirtual[15000], memoriaVirtual[15001])

    
    

# def newPage(page):

#     print("page", page)
#     cuadPointer = goBack.pop()
#     onFunc = False