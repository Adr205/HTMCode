from lark import Visitor


class NeuralPoints(Visitor):

    def program(self, tree):
        print("program")
        for child in tree.children:
            self.visit(child)

    def number(self, tree):
        print('sum')
        assert tree.data == "varcte"
        tree.children[0] += 1
        print(tree.children[0])

