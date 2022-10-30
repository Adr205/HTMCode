
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
pSaltos = []  # pila de saltos
pType = []  # pila de tipos
pOp = []  # pila de operandos
pOper = []  # pila de operadores
contVariablesTemporales = []


class NeuralPoints(Visitor):

    def main(self, tree):
        print('main')

    def number(self, tree):
        print('sum')
        assert tree.data == "varcte"
        tree.children[0] += 1
        print(tree.children[0])

    def declaracion(self, tree):

        x = 1
        # print(declaracion)
        # all_tokens = declaracion.scan_values(lambda v: isinstance(v, Token))
        # cont = 0
        # for token in all_tokens:
        #     print(token)
        #     cont += 1
        # print ('\n','Numero de variables',cont, '\n')

    def simpledeclaracion(self, tree):
        varName = tree.children[1].value
        varType = tree.children[3].children[0].value
        # print(varType, varName)
        tablaDeVariables.addVariable(Variable(varName, varType))

    def simpleasignacion(self, tree):
        varName = tree.children[1]
        varType = tree.children[3].children[0]
        varValue = -1
        allvalues = tree.children[5].scan_values(
            lambda v: isinstance(v, Token))

        for value in allvalues:
            varValue = value

        if '.' in value:
            varValue = float(value)
        elif varValue[0] == '"':
            varValue = str(varValue[1:-1])
        elif varValue == 'true' or varValue == 'false':
            if varValue == 'true':
                varValue = True
            else:
                varValue = False
        else:
            varValue = int(value)

        if varType == 'int':
            if type(varValue) != int:
                print('Error: value type is not the same as the type of the variable')
                return
        elif varType == 'float':
            if type(varValue) != float:
                print('Error: value type is not the same as the type of the variable')
                return
        elif varType == 'string':
            if type(varValue) != str:
                print('Error: value type is not the same as the type of the variable')
                return
        elif varType == 'boolean':
            if type(varValue) != bool:
                print('Error: value type is not the same as the type of the variable')
                return

        tablaDeVariables.addVariable(Variable(varName, varType, varValue))

    def compuestadeclaracion(self, tree):
        varName = tree.children[1]
        varSize = tree.children[3]
        varType = tree.children[6].children[0]
        # print( varName, varSize, varType)
        tablaDeVariables.addVariable(
            Variable(varName, varType, 'N/A', varSize))

    def compuestaasignacion(self, tree):
        varName = tree.children[1]
        varSize = tree.children[3]
        varType = tree.children[6].children[0]
        varValues = []
        # allValues = tree.children[9]
        allValues = tree.children[9].scan_values(
            lambda v: isinstance(v, Token))
        for value in allValues:
            if value[0] == '"':
                value = value.split(',')
                for v in value:
                    varValues.append(v.strip()[1:-1])
                    # varValues.append(v[1:-1])
            else:
                if value != ',':
                    # if value include .
                    if '.' in value:
                        varValues.append(float(value))
                    elif value == 'true' or value == 'false':
                        if value == 'true':
                            varValues.append(True)
                        else:
                            varValues.append(False)
                    else:
                        varValues.append(int(value))
        # print(varName, varSize, varType, varValues
        # error if value type is not the same as the type of the variable
        if varType == 'int':
            for value in varValues:
                if type(value) != int:
                    print(
                        'Error: value type is not the same as the type of the variable')
                    return
        elif varType == 'float':
            for value in varValues:
                if type(value) != float:
                    print(
                        'Error: value type is not the same as the type of the variable')
                    return
        elif varType == 'string':
            for value in varValues:
                if type(value) != str:
                    print(
                        'Error: value type is not the same as the type of the variable')
                    return
        elif varType == 'boolean':
            for value in varValues:
                if type(value) != bool:
                    print(
                        'Error: value type is not the same as the type of the variable')
                    return

        tablaDeVariables.addVariable(
            Variable(varName, varType, varValues, varSize))

    def asignacionsimple(self, tree):
        varName = tree.children[0].value
        pOp.append(varName)
        varValue = tree.children[2]
        for value in varValue.scan_values(lambda v: isinstance(v, Token)):
            varValue = value
        # print(varName, "=", varValue)

        if '.' in value:
            varValue = float(value)
        elif varValue[0] == '"':
            varValue = str(varValue[1:-1])
        elif varValue == 'true' or varValue == 'false':
            if varValue == 'true':
                varValue = True
            else:
                varValue = False
        else:
            varValue = int(value)

        var = tablaDeVariables.getVariable(varName)
        if var is None:
            print('Error: variable not declared')
            return

        var.value = varValue
        if var.type == 'int':
            if type(varValue) != int:
                print('Error: value type is not the same as the type of the variable')
                return
        elif var.type == 'float':
            if type(varValue) != float:
                print('Error: value type is not the same as the type of the variable')
                return
        elif var.type == 'string':
            if type(varValue) != str:
                print('Error: value type is not the same as the type of the variable')
                return
        elif var.type == 'boolean':
            if type(varValue) != bool:
                print('Error: value type is not the same as the type of the variable')
                return
        tablaDeVariables.updateVariable(var)

    def np_var(self, tree):
        pOp = tree
        # print('var',pOp)

    def read(self, tree):
        varName = tree.children[2].value
        value = input('Ingrese el valor de la variable ' + varName + ': ')
        varType = "None"
        if '.' in value:
            varType = "float"
            value = float(value)
        elif value == 'true' or value == 'false':
            varType = "bool"
            if value == 'true':
                value = True
            else:
                value = False
        elif value[0] == '"':
            varType = "string"
            value = value[1:-1]
        elif value[0] == '[':
            varType = "array"
            value = value[1:-1]
        else:
            varType = "int"
            value = int(value)

        cuadruplos.addCuadruplo('read', value, None, varName)

        # print(varName, value, varType)

    def escritura(self, tree):
        varName = tree.children[2].scan_values(lambda v: isinstance(v, Token))
        # for value in varName:
        #     print(value, end='\n')

    def condicion(self, tree):
        value = None
        expresion = tree.children[2].scan_values(
            lambda v: isinstance(v, Token))
        for value in expresion:
            # print(value, end='\n')
            value = value.value
        # pOp.append(value)

    def np_if(self, tree):
        result = pOp.pop()
        pType.pop()
        cuadruplos.addCuadruplo('GOTOF', result, None, "N/A")
        pSaltos.append(cuadruplos.contador - 1)

    def np_if_2(self, tree):
        # cuadruplos.addCuadruplo('GOTO', None, None, "N/A")
        # pSaltos.append(cuadruplos.contador - 1)
        # cuadruplos.cuadruplos[pSaltos.pop()].result = cuadruplos.contador
        cuadruplos.fillCuadruplo(pSaltos.pop(), cuadruplos.contador)
        
    def np_if_3(self, tree):
        cuadruplos.addCuadruplo('GOTO', None, None, "N/A")
        pSaltos.append(cuadruplos.contador - 1)

    def ciclofor(self, tree):
        asignacion = tree.children[2].scan_values(
            lambda v: isinstance(v, Token))
        # for value in asignacion:
        #     print(value, end='\n')
        expresion = tree.children[3].scan_values(
            lambda v: isinstance(v, Token))
        # for value in expresion:
        #     print(value, end='\n')
        contador = tree.children[5].scan_values(lambda v: isinstance(v, Token))
        # for value in contador:
        #     print(value, end='\n')

    def ciclowhile(self, tree):
        expresion = tree.children[2].scan_values(
            lambda v: isinstance(v, Token))
        # for value in expresion:
        #     print(value, end='\n')

    def np_while(self, tree):
        result = pOp.pop()
        pType.pop()
        cuadruplos.addCuadruplo('GOTOF', result, None, "N/A")
        pSaltos.append(cuadruplos.contador - 1)

    def np_while_2(self, tree):
        cuadruplos.addCuadruplo('GOTO', None, None, pSaltos[-1]-1)
        cuadruplos.fillCuadruplo(pSaltos.pop(), cuadruplos.contador)

    def expresion(self, tree):
        # print(tree.pretty())
        x = 1

    def np_logico(self, tree):
        pOper.append(tree.children[0].value)

    def np_logico_2(self, tree):
        if len(pOper) > 0:
            right_operand = pOp.pop()
            left_operand = pOp.pop()
            right_type = pType.pop()
            left_type = pType.pop()
            operator = pOper.pop()

            # print(left_operand, operator, right_operand)
            resultType = semantic_Cube.semantic_cube[operator][left_type][right_type]
            cuadruplos.addCuadruplo(operator, left_operand, right_operand, len(contVariablesTemporales))
            contVariablesTemporales.append(0)
            pOp.append(0) # Añadir el resultado de la operacion a la pila de operandos
            pType.append(resultType) # Añadir el tipo de la operacion a la pila de tipos

    def guardar_id(self, tree):
        varName = tree.children[0].value
        var = tablaDeVariables.getVariable(varName)
        #print(varName, var) #Checar el tipo var.type
        pOp.append(varName)
        pType.append(var.type)


    def guardar_int(self, tree):
        pOp.append(int(tree.children[0].value))
        pType.append("int")
        # Guardar en tabla de contantes y en memoria con el id de la constantes

    def guardar_float(self, tree):
        pOp.append(float(tree.children[0].value))
        pType.append("float")
        # Guardar en tabla de contantes y en memoria con el id de la constantes

    def guardar_string(self, tree):
        pOp.append(tree.children[0].value.replace('"', ''))
        pType.append("string")
        # Guardar en tabla de contantes y en memoria con el id de la constantes

    def guardar_boolean(self, tree):
        pOp.append(bool(tree.children[0].value))
        pType.append("boolean")
        # Guardar en tabla de contantes y en memoria con el id de la constantes

    # Punto Neuralgico para añadir el simbolo de suma o resta a la pila de operadores
    def expy(self, tree):
        pOper.append(tree.children[0].value)
        # print(pOper)

    # Punto Neuralgico para añadir el simbolo de multiplicacion o division a la pila de operadores
    def terminoy(self, tree):
        pOper.append(tree.children[0].value)
        # print(pOper)

    def cuadruplo_sr(self, tree):
        if len(pOper) > 0:
            # print('pOper-SR', pOper)
            if (pOper[-1] == "+") or (pOper[-1] == "-"):
                right_operand = pOp.pop()
                left_operand = pOp.pop()
                right_type = pType.pop()
                left_type = pType.pop()
                operator = pOper.pop()
                # print("Operador: ", operator, ", Operando Izquierdo: ", left_operand, ", Operando Derecho: ", right_operand)
                # Print types
                # print("Operador: ", operator, ", Operando Izquierdo: ", left_type, ", Operando Derecho: ", right_type)
                resultType = semantic_Cube.getValue(operator, left_type, right_type)
                cuadruplos.addCuadruplo(operator, left_operand, right_operand, len(contVariablesTemporales))
                contVariablesTemporales.append(0)
                pOp.append(0) # Añadir el resultado de la operacion a la pila de operandos
                pType.append(resultType) # Añadir el tipo de la operacion a la pila de tipos

    def cuadruplo_md(self, tree):
        if len(pOper) > 0:
            # print('pOper-MD', pOper)
            # print(pOp)
            if (pOper[-1] == "*") or (pOper[-1] == "/"):
                right_operand = pOp.pop()
                left_operand = pOp.pop()
                right_type = pType.pop()
                left_type = pType.pop()
                operator = pOper.pop()
                # print("Operador: ", operator, ", Operando Izquierdo: ", left_operand, ", Operando Derecho: ", right_operand)
                # Print types
                # print("Operador: ", operator, ", Operando Izquierdo: ", left_type, ", Operando Derecho: ", right_type)
                resultType = semantic_Cube.getValue(operator, left_type, right_type)
                cuadruplos.addCuadruplo(operator, left_operand, right_operand, len(contVariablesTemporales))
                contVariablesTemporales.append(0)
                pOp.append(0) # Añadir el resultado de la operacion a la pila de operandos
                pType.append(resultType) # Añadir el tipo de la operacion a la pila de tipos

    def np_asignacion(self, tree):
        varValue = pOp.pop()
        varName = pOp.pop()
        varType = pType.pop()
        cuadruplos.addCuadruplo('=', varValue, None, varName)
        contVariablesTemporales.append(0)


    # Punto Neuralgico para escribir los cuadruplos en un archivo de texto
    def end(self, tree):
        cuadruplos.writeCuadruplos()
        # print(pOper)
        # print(pType)
        # print(pOp)
        # print(pSaltos)
        # print(cuadruplos.contador)
