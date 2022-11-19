class FunctionDirectory:

    def __init__(self):
        self.funcDirectory = {}

    def alreadyExists(self, func):
        if func.name in self.funcDirectory:
            return True
        else:
            return False

    def addFunction(self, func):
        if not self.alreadyExists(func):
            self.funcDirectory[func.name] = func
        else: #Quitar en la entrega final
            print("Function already exists in directory")

    def getFunction(self, funcName):
        if funcName in self.funcDirectory:
            return self.funcDirectory[funcName]
        else:
            return None

    def updateFunction(self, func):
        if self.alreadyExists(func):
            self.funcDirectory[func.name] = func
        else:
            print("Function ", func.name, " does not exist in directory")

            
    def printDirectory(self):
        for func in self.funcDirectory:
            print(self.funcDirectory[func].name)
            self.funcDirectory[func].printFunction()
            
    def __str__(self):
        return str(self.funcDirectory)