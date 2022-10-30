class Variable():

    def __init__(self, name, type, value="N/A", size = -1):
        self.name = name
        self.type = type
        self.value = value
        self.size = size

    def __str__(self):
        return "Variable: " + self.name + "\n\tType: " + self.type + "\n\t\tValue: " + str(self.value) + "\n\t\t\tSize: " + str(self.size)

    def printVariable(self):
        print("Variable: " + self.name + " Type: " + self.type + " Value: " + self.value)