

class VariablesTable:

    def __init__ (self):
        self.variables = {}
        self.globales = {}

    def alreadyExists(self, var):
        if var in self.variables:
            return True
        else:
            return False

    def alreadyExistsGlobal(self, var):
        if var in self.globales:
            return True
        else:
            return False
    
    def addVariable(self, var):
        if not self.alreadyExists(var.name):
            self.variables[var.name] = var
        else: #Quitar en la entrega final
            print("Variable " ,var.name, " already exists in directory")

    def addVariableGlobal(self, var):
        if not self.alreadyExistsGlobal(var.name):
            self.globales[var.name] = var
        else: #Quitar en la entrega final
            print("Variable " ,var.name, " already exists in directory")

    def updateVariable(self, var):
        if self.alreadyExists(var.name):
            self.variables[var.name] = var
        else:
            print("Variable " ,var.name, " does not exist in directory")

    def updateVariableGlobal(self, var):
        if self.alreadyExistsGlobal(var.name):
            self.globales[var.name] = var
        else:
            print("Variable " ,var.name, " does not exist in directory")

    def getVariable(self, varName):
        if varName in self.variables:
            return self.variables[varName]
        else:
            return None

    def getVariableGlobal(self, varName):
        if varName in self.globales:
            return self.globales[varName]
        else:
            return None

    def getVariableGlobalID(self, id):
        for var in self.globales:
            if self.globales[var].dirV == id:
                return self.globales[var]
        return None

    def printTable(self):
        for var in self.variables:
            var.printVariable()

    def printTableFGlobal(self):
        for var in self.globales:
            var.printVariable()

    def resetTable(self):
        self.variables = {}

    def resetTableGlobal(self):
        self.globales = {}
    
    def __str__(self):
        string = ""
        for var in self.variables:
            string += str(self.variables[var]) + "\n"
        return string
    
    def printGlobales(self):
        string = ""
        for var in self.globales:
            string += str(self.globales[var]) + "\n"
        print(string)



# table = VariablesTable()
# # self, name, type, value="N/A", dirV = -1, scope= 'global', size = -1 
# var = Var("a", "int", 5, 0)
# table.addVariable(var)
# var = Var("b", "float", 3.12, 0)
# table.addVariable(var)
# print(table)
