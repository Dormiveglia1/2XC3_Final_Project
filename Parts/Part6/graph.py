from typing import List, Dict, Tuple, Set
import random

class Graph():
    def __init__(self, nodes):
        self.adj = {}
        self.weights = {}
        for i in range(nodes):
            self.adj[i] = []

    def get_adj_nodes(self, node: int) -> List[int]:
        return self.adj[node]

    def add_node(self, node: int) -> None:
        self.adj[node] = []

    def add_edge(self, start: int, end: int, w: float) -> None:
        if end not in self.adj[start]:
            self.adj[start].append(end)
        self.weights[(start, end)] = w

    def get_num_of_nodes(self) -> int:
        return len(self.adj)

    def w(self, node1: int, node2: int) -> float:
        if (node1, node2) in self.weights:
            return self.weights[(node1, node2)]
    
    def create_random_graph(nodes, edges):
        graph = None

        # your implementation goes here
        
        edge_set = set()
        graph = Graph(nodes)
        
        while len(edge_set) < edges:
            u = random.randint(0, nodes - 1)
            v = random.randint(0, nodes - 1)
            weight = random.randint(0, 20)
            
            if (u != v) and (u, v) not in edge_set:
                graph.add_edge(u, v, weight)
                edge_set.add((u, v))
        
        return graph