
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
pSaltos = []  #* pila de saltos
pType = []  #* pila de tipos
pOp = []  #* pila de operandos
pOper = []  #* pila de operadores
global pFor, VC, VF, contVariablesTemporales, contadores
pFor = False
VC = -1
VF = -1
contVariablesTemporales = 0

#* Object contadores  [{operation:, value:}]
contadores = []

# TODO: Separacion de memoria para el tipado de variables

class NeuralPoints(Visitor):

    def start(self, tree):
        cuadruplos.addCuadruplo("GOTO-MAIN", None, None, "N/A")

    #* Funcion para declarar variables en la tabla de variables
    def simpledeclaracion(self,tree): 
        varName = tree.children[1].value # Nombre de la variable
        varType = tree.children[3].children[0].value # Tipo de la variable
        tablaDeVariables.addVariable(Variable(varName, varType)) # Agregar variable a la tabla de variables

    #* Funcion para declarar variables en la tabla de variables y asignarles un valor
    def simpleasignacion(self,tree):
        varName = tree.children[1].value
        varType = tree.children[3].children[0].value
        # TODO: Agarrar el valor de la pila de operandos y asignar el valor a la variable
        varValue = "N/A"
        tablaDeVariables.addVariable(Variable(varName, varType, varValue))

    

    def end(self, tree):
        x = 1
