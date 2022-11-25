'''

    Globales:
        int: 1000
        float: 3000
        string: 5000
        boolean: 7000 - 9000

    Locales:
        int: 10,000
        float: 13,000
        string: 15,000
        boolean: 17,000 - 19,000

    Constantes:
        int: 20,000
        float: 23,000
        string: 25,000
        boolean: 27,000 -- 29,000
    
    Temporales:
        int: 30,000
        float: 33,000
        string: 36,000
        boolean: 39,000 - 42,000


'''


class Memoria():

    # __slots__ = ['memoria', 'intGlobal', 'floatGlobal', 'stringGlobal', 'booleanGlobal', 'intLocal', 'floatLocal', 'stringLocal', 'booleanLocal', 'intConstante', 'floatConstante', 'stringConstante', 'booleanConstante', 'intTemporal', 'floatTemporal', 'stringTemporal', 'booleanTemporal']

    def __init__(self):
        #Memoria para manejar las direcciones por tipo
        self.memoria = {
            'global': {
                'int': 1000,
                'float': 3000,
                'string': 5000,
                'boolean': 7000
            },
            'local': {
                'int': 10000,
                'float': 13000,
                'string': 15000,
                'boolean': 17000
            },
            'constante': {
                'int': 20000,
                'float': 23000,
                'string': 25000,
                'boolean': 27000
            },
            'temporal': {
                'int': 30000,
                'float': 33000,
                'string': 36000,
                'boolean': 39000,
                'pointer': 42000
            }
        }
        #* Memoria de ejecucion
        self.memoriaVirtual = {}

        #* Contadores para las direcciones de memoria
        self.intGlobal = 1000
        self.floatGlobal = 3000
        self.stringGlobal = 5000
        self.booleanGlobal = 7000

        self.intLocal = 10000
        self.floatLocal = 13000
        self.stringLocal = 15000
        self.booleanLocal = 17000

        self.intConstante = 20000
        self.floatConstante = 23000
        self.stringConstante = 25000
        self.booleanConstante = 27000

        self.intTemporal = 30000
        self.floatTemporal = 33000
        self.stringTemporal = 36000
        self.booleanTemporal = 39000
        self.pointerTemporal = 42000

    def __str__(self):
        return str(self.memoria)
