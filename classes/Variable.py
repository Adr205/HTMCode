class Variable():

    def __init__(self, name, type, value="N/A", dirV = -1, scope= 'global', size = -1 ):
        self.name = name
        self.type = type
        self.value = value
        self.dirV = dirV
        self.scope = scope
        self.size = size

    def __str__(self):
        return "Variable: " + self.name + "\n\tType: " + self.type + "\n\t\tValue: " + str(self.value) + "\n\t\t\tSize: " + str(self.size) + "\n\t\t\t\tDirV: " + str(self.dirV) + "\n\t\t\t\t\tScope: " + self.scope

    def printVariable(self):
        print("Variable: " + self.name + " Type: " + self.type + " Value: " + self.value +  "DirV" + str(self.dirV) + "Scope" + self.scope )