import random
from directed_weighted_graph import DirectedWeightedGraph

def create_random_graph(nodes, edges):
    graph = None

    # your implementation goes here
    
    edge_set = set()
    graph = DirectedWeightedGraph(nodes)
    
    while len(edge_set) < edges:
        u = random.randint(0, nodes - 1)
        v = random.randint(0, nodes - 1)
        weight = random.randint(0, 20)
        
        if (u != v) and (u, v) not in edge_set:
            graph.add_edge(u, v, weight)
            edge_set.add((u, v))
    
    return graph

