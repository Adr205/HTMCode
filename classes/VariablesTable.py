

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
            var.printVariable()

    def resetTable(self):
        self.variables = {}
    
    def __str__(self):
        string = ""
        for var in self.variables:
            string += str(self.variables[var]) + "\n"
        return string



# table = VariablesTable()
# # self, name, type, value="N/A", dirV = -1, scope= 'global', size = -1 
# var = Var("a", "int", 5, 0)
# table.addVariable(var)
# var = Var("b", "float", 3.12, 0)
# table.addVariable(var)
# print(table)
