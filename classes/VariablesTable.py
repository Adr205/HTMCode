import classes.Variable as Var

class VariablesTable:

    def __init__ (self):
        self.variables = {}

    def alreadyExists(self, var):
        if var in self.variables:
            return True
        else:
            return False
    
    def addVariable(self, var):
        if not self.alreadyExists(var.name):
            self.variables[var.name] = var
        else: #Quitar en la entrega final
            print("Variable " ,var.name, " already exists in directory")

    def updateVariable(self, var):
        if self.alreadyExists(var.name):
            self.variables[var.name] = var
        else:
            print("Variable " ,var.name, " does not exist in directory")

    def getVariable(self, varName):
        if varName in self.variables:
            return self.variables[varName]
        else:
            return None

    def printTable(self):
        for var in self.variables:
            print(self.variables[var])
            self.variables[var].printVariable(self.variables[var])
            # self.variables[var].printVariable()
    
    def __str__(self):
        return str(self.variables)