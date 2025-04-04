from sp_algorithm import SPAlgorithm
from graph import Graph
import heapq

class Dijkstra(SPAlgorithm):

    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        distance = {node: float('inf') for node in range(graph.get_num_of_nodes())}
        distance[source] = 0
        
        pq = [(0, source)]  # (distance, node)
        visited = set()

        while pq:
            _, current = heapq.heappop(pq)
                            
            if current in visited: 
                continue
                
            visited.add(current)
            
            for neighbor in graph.get_adj_nodes(current):
                if neighbor not in visited:
                    weight = graph.w(current, neighbor)
                    new_distance = distance[current] + weight
                    
                    if new_distance < distance[neighbor]:
                        distance[neighbor] = new_distance
                        heapq.heappush(pq, (new_distance, neighbor))
        
        return distance[dest]