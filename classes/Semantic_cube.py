class SemanticCube():

    '''
        Cubo semantico en el que se accesa con la siguiente estructura:
        semantic_cube[operacion][tipoIzq][tipoDer]
        donde operacion es una de las operaciones que se definen en la gramatica
        y tipoIzq y tipoDer son los tipos de los operandos
    '''


    def __init__(self):
        self.semantic_cube = {
            '+': {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'error',
                    'boolean': 'error'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'error',
                    'boolean': 'error'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'string',
                    'boolean': 'error'
                },
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error'
                }
            },
            '-': {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'error',
                    'boolean': 'error'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'error',
                    'boolean': 'error'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error'
                },
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error'
                }
            },
            '*': {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'error',
                    'boolean': 'error'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'error',
                    'boolean': 'error'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error'
                },
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error'
                }
            },
            '/': {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'error',
                    'boolean': 'error'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'error',
                    'boolean': 'error'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error'
                },
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error'
                }
            },
            '>': {
                'int': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean'
                },
                'float': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error'
                },
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'boolean'
                }
            },
            '<': {
                'int': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean'
                },
                'float': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error'
                },
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'boolean'
                }
            },
            '>=': {
                'int': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean'
                },
                'float': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error'
                },
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'boolean'
                }
            },
            '<=': {
                'int': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean'
                },
                'float': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error'
                },
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'boolean'
                }
            },
            '==': {
                'int': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean'
                },
                'float': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'boolean',
                    'boolean': 'error'
                },
                'boolean': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean'
                }
            },
            '!=': {
                'int': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean'
                },
                'float': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'boolean',
                    'boolean': 'error'
                },
                'boolean': {
                    'int': 'boolean',
                    'float': 'boolean',
                    'string': 'error',
                    'boolean': 'boolean'
                }
            },
            'and': {
                'int': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error'
                },
                'float': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error'
                },
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'boolean'
                }
            },
            'or': {
                'int': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error'
                },
                'float': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error'
                },
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'boolean'
                }
            },
            'not': {
                'int': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error'
                },
                'float': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error'
                },
                'string': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'error'
                },
                'boolean': {
                    'int': 'error',
                    'float': 'error',
                    'string': 'error',
                    'boolean': 'boolean'
                }
            }
        }

    def getValue(self, operation, typeI, typeD):
        return self.semantic_cube[operation][typeI][typeD] 

    def getCube(self):
        return self
        

    def printCube(self):
        print(self.semantic_cube)
