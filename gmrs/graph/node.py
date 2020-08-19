class Node:
    def __init__(self, type):
        self.leaf = False
        self.type = type
        self.edges = []

    def addEdge(self, edge):
        self.edges.append(edge)


class Edge:
    def __init__(self, nodeA, nodeB):
        self.nodeA = nodeA
        self.nodeB = nodeB
