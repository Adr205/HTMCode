# import Variable as Var

class VariableTable:

    def __init__ (self):
        self.variables = {}

    def alreadyExists(self, var):
        if var.name in self.variables:
            return True
        else:
            return False
    
    def addVariable(self, var):
        if not self.alreadyExists(var):
            self.variables[var.name] = var
        else: #Quitar en la entrega final
            print("Variable already exists in directory")

    def getVariable(self, varName):
        if varName in self.variables:
            return self.variables[varName]
        else:
            return None

    def printTable(self):
        for var in self.variables:
            print(self.variables[var].name)
            self.variables[var].printVariable(self.variables[var])
            # self.variables[var].printVariable()
    