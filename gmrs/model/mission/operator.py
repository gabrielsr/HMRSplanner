from gmrs.graph.node import Node

from enum import Enum


class Operator(Node):
    def __init__(self):
        pass


class OP(Enum):
    SEQ = Operator()
    FALLBACK = Operator()
