import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from graph import Graph
from sp_algorithm import SPAlgorithm
from create_random_graph import create_random_graph
from a_star import A_Star
from dijkstra import Dijkstra
from bellman_ford import Bellman_Ford

class ShortPathFinder:
    def __init__(self):
        self._graph = None
        self._algorithm = None

    def calc_short_path(self, source: int, dest: int) -> float:
        if self._graph is None or self._algorithm is None:
            raise ValueError("Graph and algorithm must be set before calculating path")
        return self._algorithm.calc_sp(self._graph, source, dest)

    def set_graph(self, graph: Graph) -> None:
        self._graph = graph

    def set_algorithm(self, algorithm: SPAlgorithm) -> None:
        self._algorithm = algorithm


finder = ShortPathFinder()
graph = Graph.create_random_graph(6, 15)
finder.set_graph(graph)
algorithm = A_Star()
finder.set_algorithm(algorithm)
source = 0
dest = 5
shortest_path_distance = finder.calc_short_path(source, dest)
print(f"Shortest path from {source} to {dest} is {shortest_path_distance}")
