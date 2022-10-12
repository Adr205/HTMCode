import VariablesTable as vt
import Variable as var

class Function:
    
    def __init__ (self, name,type,params=[]):
        self.name = name
        self.type = type
        self.params = params
        self.variables = vt.VariableTable()

    def addParameters(self, param, type):
        variable = var.Variable(param, type)
        self.variables.addVariable(variable)

    def addVariable(self, var):
        self.variables.addVariable(var)

    def printFunction(self):
        print("Function: " + self.name + " Type: " + self.type)
        print("Parameters:")
        for param in self.params:
            print(param)
        print("Variables:")
        self.variables.printTable()


# f = Function("hola", "int", ["a", "b"])
# f.addVariable(var.Variable("c", "int"))
# f.addVariable(var.Variable("d", "int"))
# f.printFunction()
