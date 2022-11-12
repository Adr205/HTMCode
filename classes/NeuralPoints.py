
from genericpath import samestat
import pty
from re import I
from turtle import right
from urllib.error import ContentTooShortError
from xml.etree.ElementInclude import include
from lark import Token, Visitor
from classes.VariablesTable import VariablesTable
from classes.Variable import Variable
from classes.Cuadruplos import Cuadruplos
from classes.Semantic_cube import SemanticCube

tablaDeVariables = VariablesTable()
cuadruplos = Cuadruplos()
semantic_Cube = SemanticCube()
pSaltos = []  # * pila de saltos
pType = []  # * pila de tipos
pOp = []  # * pila de operandos
pOper = []  # * pila de operadores
pVars = []  # * pila de variables
global pFor, VC, VF, contVariablesTemporales, contadores
pFor = False
VC = -1
VF = -1
contVariablesTemporales = 0

# * Object contadores  [{operation:, value:}]
contadores = []

# TODO: Separacion de memoria para el tipado de variables
# TODO: Punto neuralgico Read
# TODO: Punto neuralgico Input


class NeuralPoints(Visitor):

    def start(self, tree):
        pSaltos.append(cuadruplos.contador)
        cuadruplos.addCuadruplo("GOTO-MAIN", None, None, "N/A")

    def np_main(self, tree):
        cuadruplos.fillCuadruplo(pSaltos.pop(), cuadruplos.contador)

    # * Funcion para declarar variables globales en la tabla de variables
    def simpleglobal(self, tree):
        varName = tree.children[1].value
        varType = tree.children[3].children[0].value
        varIgual = tree.children[4].value
        if(varIgual == "="):
            varValue = 0  # TODO: Agarrar el valor de la pila de operandos y asignar el valor a la variable
        else:
            varValue = "N/A"  # : No tiene valor

        tablaDeVariables.addVariable(Variable(varName, varType, varValue))
        # TODO: Usar variables temporales y el valor de la pila de operandos
        cuadruplos.addCuadruplo("=", varValue, None, varName)

    # * Funcion para declarar arreglos globales en la tabla de variables
    def compuestoglobal(self, tree):
        x = 1  # TODO: Agregar todo lo del uso de arreglos como variables

    # * Funcion para declarar variables en la tabla de variables
    def simpledeclaracion(self, tree):
        varName = tree.children[1].value  # Nombre de la variable
        varType = tree.children[3].children[0].value  # Tipo de la variable
        # Agregar variable a la tabla de variables
        tablaDeVariables.addVariable(Variable(varName, varType))

    # * Funcion para declarar variables en la tabla de variables y asignarles un valor
    def simpleasignacion(self, tree):
        varName = tree.children[1].value
        pVars.append(varName)
        varType = tree.children[3].children[0].value
        # TODO: Agarrar el valor de la pila de operandos y asignar el valor a la variable y verificar si es de tipo correcto
        varValue = "N/A"
        tablaDeVariables.addVariable(Variable(varName, varType, varValue))

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

    #! Funciones para generacion de cuadruplos del ciclo WHILE
    #*Funcion 
    def np_while(self, tree):
        result = pOp.pop() # Valor de la condicion
        pType.pop() # Tipo de la condicion
        pSaltos.append(cuadruplos.contador) # Agregar el contador de cuadruplos a la pila de saltos
        cuadruplos.addCuadruplo("GOTOF", result, None, "N/A") # Agregar cuadruplo de salto falso


    def np_while_2(self, tree):
        fill = pSaltos.pop() # Llenar el cuadruplo de salto falso
        add = pSaltos.pop() # Agregar el contador de cuadruplos a la pila de saltos
        cuadruplos.addCuadruplo("GOTO", None, None, add) # Agregar cuadruplo de salto a inicio
        cuadruplos.fillCuadruplo(fill, cuadruplos.contador) # Llenar el cuadruplo de salto falso


    def np_while_3(self, tree):
        pSaltos.append(cuadruplos.contador) # Agregar el contador de cuadruplos a la pila de saltos

    # * Funciones para operaciones aritmeticas

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
        global contVariablesTemporales
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
            cuadruplos.addCuadruplo(operator, left_operand, right_operand, "t" + str(contVariablesTemporales))
            contVariablesTemporales += 1
            pOp.append("t" + str(contVariablesTemporales - 1))
            pType.append(result_type)

    # *Funcion para crear el cuadruplo de la suma y resta
    def cuadruplo_sr(self, tree):
        if len(pOper) > 0:  # Checar si la pila de operadores esta vacia
            # Checar si el ultimo operador es de suma o resta
            global contVariablesTemporales
            if pOper[-1] == "+" or pOper[-1] == "-":
                right_operand = pOp.pop()  # Obtener el operando de la derecha
                left_operand = pOp.pop()  # Obtener el operando de la izquierda
                right_type = pType.pop()  # Obtener el tipo del operando de la derecha
                left_type = pType.pop()  # Obtener el tipo del operando de la izquierda
                operator = pOper.pop()  # Obtener el operador
                result_type = semantic_Cube.getValue(operator, left_type, right_type)  # Obtener el tipo de resultado
                cuadruplos.addCuadruplo(operator, left_operand, right_operand,"t" + str(contVariablesTemporales))  # Crear el cuadruplo
                contVariablesTemporales += 1  # Aumentar el contador de variables temporales
                pOp.append("t" + str(contVariablesTemporales - 1)) # Agregar el resultado a la pila de operandos #TODO: Agregar el valor de la variable temporal
                pType.append(result_type) # Agregar el tipo de resultado a la pila de tipos

    #*Funcion para crear el cuadruplo de la multiplicacion y division
    def  cuadruplo_md(self, tree):
        if len(pOper) > 0:
            if pOper[-1] == "*" or pOper[-1] == "/":
                global contVariablesTemporales
                right_operand = pOp.pop()
                left_operand = pOp.pop()
                right_type = pType.pop()
                left_type = pType.pop()
                operator = pOper.pop()
                result_type = semantic_Cube.getValue(operator, left_type, right_type)
                cuadruplos.addCuadruplo(operator, left_operand, right_operand, "t" + str(contVariablesTemporales))
                contVariablesTemporales += 1
                pOp.append("t" + str(contVariablesTemporales - 1))
                pType.append(result_type)

    #* Guardar ID en la pila de operandos
    def guardar_id(self, tree):
        varName = tree.children[0].value
        var = tablaDeVariables.getVariable(varName)
        if var == None:
            print("Error: Variable no declarada")
            exit()
        pOp.append(varName)
        pType.append(var.type)
        #TODO: Guardar el valor en la memoria de constantes

    #*Funcion para guardar un entero en la pila de operandos
    def guardar_int(self, tree):
        pOp.append(tree.children[0].value)
        pType.append("int")
        #TODO: Guardar el valor en la memoria de constantes

    #* Funcion para guardar un float en la pila de operandos
    def guardar_float(self, tree):
        pOp.append(float(tree.children[0].value))
        pType.append("float")
        #TODO: Guardar el valor en la memoria de constantes

    #* Funcion para guardar un string en la pila de operandos
    def guardar_string(self, tree):
        pOp.append(tree.children[0].value.replace('"', ''))
        pType.append("string")
        #TODO: Guardar el valor en la memoria de constantes

    #* Funcion para guardar un booleano en la pila de operandos
    def guardar_boolean(self, tree):
        if(tree.children[0].value == "true"):
            pOp.append(True)
        elif (tree.children[0].value == "false"):
            pOp.append(False)
        pType.append("boolean")
        #TODO: Guardar el valor en la memoria de constantes

    #* Funcion para asignar el valor a una variable
    def np_asignacion(self, tree):
        varValue = pOp.pop() # Obtener el valor de la pila de operandos
        varName = pVars.pop() # Obtener el nombre de la variable
        var = tablaDeVariables.getVariable(varName)
        varType = pType.pop() # Obtener el tipo de la variable #TODO: Verificar que el tipo de la variable sea el mismo que el tipo del valor
        if var.type != varType:
            print("Error: Tipos incompatibles")
            exit()
        
        cuadruplos.addCuadruplo("=", varValue, None, varName) # Crear el cuadruplo de asignacion

    def np_asignacion_2(self, tree):
        varValue = pOp.pop()
        varName = pVars.pop()
        varType = pType.pop()
        cuadruplos.addCuadruplo("=", varValue, None, varName)

    def end(self, tree):
        print('pOper' , pOper)
        print('pOp' , pOp)
        print('pType' , pType)
        print('pSaltos' , pSaltos)
        cuadruplos.writeCuadruplos()
