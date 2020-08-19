from gmrs.graph.edge import Edge


class Decomposition(Edge):

    def __init__(self, type):
        self.type = type


def set_decomposition():
    pass


sequential = Decomposition('Sequential')
