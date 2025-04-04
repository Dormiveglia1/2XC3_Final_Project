from sp_algorithm import SPAlgorithm
from graph import Graph

class Bellman_Ford(SPAlgorithm):

    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        distance = {node: float('inf') for node in range(graph.get_num_of_nodes())}
        predecessor = {node: None for node in range(graph.get_num_of_nodes())}

        distance[source] = 0

        for _ in range(graph.get_num_of_nodes() - 1):
            for u in range(graph.get_num_of_nodes()):
                for v in graph.get_adj_nodes(u):
                    weight = graph.w(u, v)
                    if distance[u] + weight < distance[v]:
                        distance[v] = distance[u] + weight
                        predecessor[v] = u

        return distance[dest]