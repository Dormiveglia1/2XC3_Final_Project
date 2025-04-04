from weighted_graph import WeightedGraph
from typing import Dict
import pickle

with open('Part5_heuristic.pkl', 'rb') as file:
    heuristics = pickle.load(file)

class HeuristicGraph(WeightedGraph):
    def __init__(self, nodes: int):
        super().__init__(nodes)
        self.heuristic = heuristics

    def get_heuristic(self) -> Dict[int, float]:
        return self.heuristic
    
    def w(self, node1: int, node2: int) -> float:
        return self.heuristic[node1][node2]
