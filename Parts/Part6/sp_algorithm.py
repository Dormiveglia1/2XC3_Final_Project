from abc import ABC, abstractmethod
from graph import Graph

class SPAlgorithm(ABC):
    @abstractmethod
    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        pass