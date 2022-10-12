class Variable():

    def __init__(self, name, type, value=''):
        self.name = name
        self.type = type
        self.value = value

    def __str__(self):
        return "Variable: " + self.name + " Type: " + self.type + " Value: " + self.value

    def printVariable(self):
        print("Variable: " + self.name + " Type: " + self.type + " Value: " + self.value)