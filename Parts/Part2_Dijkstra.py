import heapq
import random
from directed_weighted_graph import DirectedWeightedGraph
from create_random_graph import create_random_graph

# k is the limitation of relaxed times
def dijkstra(graph, source, k):
    dist = {}           # Distance from each node to source
    prev = {}           # The path go through
    relax_count = {}    # Relax count for each node
    path = {}           # Use path but not Q in the pesuducode to show the whole path

    for node in graph.adj:
        dist[node] = float('inf')
        prev[node] = None
        relax_count[node] = 0
        path[node] = []

    dist[source] = 0
    path[source] = [source]

    heap = [(0, source)]

    while heap:
        current_dist, u = heapq.heappop(heap)

        for v in graph.adjacent_nodes(u):
            alt = dist[u] + graph.get_weight(u, v)

            # Allows updating when the relax number is not used up
            if alt < dist[v] and relax_count[v] < k:
                dist[v] = alt
                prev[v] = u
                relax_count[v] += 1
                path[v] = path[u] + [v]
                heapq.heappush(heap, (alt, v))

    # End result: Return distance and path (including points traveled)
    return dist, path


graph = create_random_graph(6, 20)

print(graph.adj)
print(graph.weights)

dist1, path1 = dijkstra(graph, 0, 4)
print("distance:",dist1)
print("path",path1)