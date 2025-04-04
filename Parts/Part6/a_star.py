from sp_algorithm import SPAlgorithm
from graph import Graph
from typing import Callable
from Old_A_Star import A_Star as OldAStar
from heuristic_graph import HeuristicGraph

class A_Star(SPAlgorithm):
    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        h = HeuristicGraph(graph.get_num_of_nodes())
        heuristic = h.get_heuristic()
        _, path = OldAStar(graph, source, dest, lambda n, d: heuristic.get((n, d), float('inf')))

        current = path[0]
        total_weight = 0

        for i in range(1, len(path)):
            total_weight += graph.w(current, path[i])
            current = path[i]

        return total_weight