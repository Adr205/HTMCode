from lark import Lark
from lark import Visitor
from classes.NeuralPoints import NeuralPoints
from classes.Semantic_cube import SemanticCube

test = 'testVar.txt'
parser = Lark(open("grammar.g", 'r').read())
result = ''


def compile():
    input = open(test, 'r').read()
    result = parser.parse(input)
    # write tree to file
    with open('tree.txt', 'w') as f:
        resultPretty = parser.parse(input).pretty()
        f.write(str(resultPretty))

    execute(result)


def execute(result):
    NeuralPoints().visit_topdown(result)
    
def main():
    compile()
    # SemanticCube().printCube()
    # print(SemanticCube().getValue('+', 'int', 'int'))
    # print(SemanticCube().getValue('-', 'int', 'float'))
    # print(SemanticCube().getValue('and', 'boolean', 'int'))
    # print(SemanticCube().getValue('>', 'int', 'string'))


if __name__ == '__main__':
    main()
    # x = []
    # x.append(1)
    # print(x[-1])
    # x.append(2)
    # x.append(3)
    # print(x)
