import ast
from classes.NeuralPoints import *
from classes.Memoria import *
from classes.FunctionDirectory import *

'''
    TODO:   Guardar variables globales a memoria virtual global
            Hacer la maquina virtual y minimo que resuelva las expresiones aritmeticas y logicas
            Hacer la llamada a funciones tipadas
            Guardar el resultado de la funcion en una variable global con el nombre de la funcion
            Contar la cantidad de temporales y variables de las funciones para el ERA
            Todo el codigo de Arreglos
        #!  Arreglar la commutividad por derecha y hacerla por izquierda
        #!  Añadir el uso de parentesis para las expresiones

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
cuadruplos = []
tablaConst = {}
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
        # print(type(val),val)
        # print(typ)
        # print(dirV,val, type)
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
        # print(type(val),val)
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
    if func.boolTemp > 0:
        for i in range(func.boolTemp):
            memoriaVirtual[dirBoolTemp + i] = None

def htmlCode():
    global cuadPointer
    
    operator = cuadruplos[cuadPointer][0]
    while operator != 'END':
        operator = cuadruplos[cuadPointer][0]
        left = cuadruplos[cuadPointer][1]
        right = cuadruplos[cuadPointer][2]
        result = cuadruplos[cuadPointer][3]
        
        if operator == 'GOTO-MAIN':
            fillMemory("main")
            cuadPointer = int(result)
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
            memoriaVirtual[result] = left
            cuadPointer += 1
    print(memoriaVirtual)           

            
        


    


def virtualMachine():
    global tablaVariables, dirFunc
    tablaVariables = tablaDeVariables
    dirFunc = funcDirectory.funcDirectory
    # print(tabla)
    readConstantes()
    readCuadruplos()
    htmlCode()