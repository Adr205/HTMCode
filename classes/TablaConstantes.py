# Clase de la tabla de constantes, donde se guardan 
# todas las constantes utilizadas por compilacion

class TablaConstantes():

    def __init__(self):
        self.tabla = []

    #* Funcion para añadir una constante
    def addConstante(self, dirV, constante, type):
        #TODO: Verificar que no exista la constante para eficientizar el codigo y la memoria
        self.tabla.append([dirV, constante, type])

    #* Funcion para obtener una constante por medio de su direccion virtual
    def getConstante(self, dirV):
        for constante in self.tabla:
            if constante[0] == dirV:
                return constante[1]
        return None

    #* Funcion para obtener una direccion virtual por medio de su constante
    def getDirV(self, const):
        for constante in self.tabla:
            if str(constante[1]) == str(const):
                return constante[0]
        return None

    #*Funcion para verificar si una constante ya existe
    def alreadyExists(self, const):
        for constante in self.tabla:
            if str(constante[1]) == str(const):
                return True
        return False

    def writeTable(self):
        with open('constantes.txt', 'w') as f:
            for constante in self.tabla:
                f.write(str(constante) + '\n')

    #* Funcion para imprimir la tabla de constantes
    def __str__(self):
        return str(self.tabla)