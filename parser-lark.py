# Javier Adrian Villa Leon
# A01242469

from lark import Lark

parser = Lark(open("grammar.g", 'r').read())
calc = parser.parse
s = open("test1.txt", 'r').read()
print(calc(s).pretty())
