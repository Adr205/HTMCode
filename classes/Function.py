from classes.VariablesTable import VariablesTable as vt
from classes.Variable import Variable as var
class Function:

    def __init__(self, name, type, dirV, params=[], variables={}, intTemp = 0, floatTemp = 0, booleanTemp = 0, stringTemp = 0, intVar = 0, floatVar = 0, booleanVar = 0, stringVar = 0, pointerTemp = 0):
        self.name = name
        self.type = type
        self.params = params
        self.dirV = dirV
        self.variables = variables
        self.intTemp = intTemp
        self.floatTemp = floatTemp
        self.booleanTemp = booleanTemp
        self.stringTemp = stringTemp
        self.intVar = intVar
        self.floatVar = floatVar
        self.booleanVar = booleanVar
        self.stringVar = stringVar
        self.pointerTemp = pointerTemp

    def addParameters(self, param, type):
        variable = var.Variable(param, type)
        self.variables.addVariable(variable)

    def addVariable(self, var):
        self.variables.addVariable(var)

    def getFunction(self, funcName):
        if funcName in self.functions:
            return self.functions[funcName]
        else:
            return None

    def updateFunction(self, func):
        if self.alreadyExists(func.name):
            self.functions[func.name] = func
        else:
            print("Function ", func.name, " does not exist in directory")

    def printFunction(self):
        print("Function: " + self.name + " Type: " +
              self.type + "DirV: " + str(self.dirV))
        print("Parameters:")
        for param in self.params:
            print(param)
        print("Variables:")
        for var in self.variables:
            print(var)

    def __str__(self):
        return str(self.name) + " : " + str(self.type) + " ( " + str(self.params) + " " + str(self.dirV) + " " + str(self.variables) + " " + str(self.intTemp) + " " + str(self.floatTemp) + " " + str(self.booleanTemp) + " " + str(self.stringTemp) + " " + str(self.intVar) + " " + str(self.floatVar) + " " + str(self.booleanVar) + " " + str(self.stringVar) + " )"

# f = Function("hola", "int", ["a", "b"])
# f.addVariable(var.Variable("c", "int"))
# f.addVariable(var.Variable("d", "int"))
# f.printFunction()
