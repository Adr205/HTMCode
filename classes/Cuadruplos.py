class Cuadruplos():

    def __init__(self):
        self.cuadruplos = []
        self.contador = 0

    def __str__(self):
        return str(self.cuadruplos)

    def addCuadruplo(self, operator, left, right, result):
        self.cuadruplos.append([operator, left, right, result])
        self.contador += 1

    def fillCuadruplo(self, cuadruplo, result):
        self.cuadruplos[cuadruplo][3] = result

    # write cuadruplos on file
    def writeCuadruplos(self):
        with open('cuadruplos.txt', 'w') as f:
            for cuadruplo in self.cuadruplos:
                f.write(str(cuadruplo) + '\n')
