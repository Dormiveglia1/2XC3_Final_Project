from graph import Graph
from typing import List

class WeightedGraph(Graph):
    def __init__(self, nodes: int):
        super().__init__(nodes)

    def w(self, node1: int, node2: int) -> float:
        return super().w(node1, node2)