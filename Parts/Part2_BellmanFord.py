# import heapq
import random
from directed_weighted_graph import DirectedWeightedGraph
from create_random_graph import create_random_graph

def bellman_ford(graph, source, k):
    num_nodes = graph.number_of_nodes()
    distance = {node: float('inf') for node in graph.adj}
    predecessor = {node: None for node in graph.adj}
    relax_count = {node: 0 for node in graph.adj}  # The number of times each node is relaxed

    distance[source] = 0

    for i in range(k):  # Repeat k rounds at most
        for u in graph.adj:
            for v in graph.adjacent_nodes(u):
                weight = graph.get_weight(u, v)
                if distance[u] + weight < distance[v] and relax_count[v] < k:
                    distance[v] = distance[u] + weight
                    predecessor[v] = u
                    relax_count[v] += 1

    # Generate path dictionary
    path = {}
    for node in graph.adj:
        if distance[node] == float('inf'):
            path[node] = []
        else:
            path[node] = []
            current = node
            while current is not None:
                path[node].insert(0, current)
                current = predecessor[current]

    return distance, path


graph = create_random_graph(6, 20)

print(graph.adj)
print(graph.weights)

dist1, path1 = bellman_ford(graph, 0, 4)
print("distance:",dist1)
print("path",path1)