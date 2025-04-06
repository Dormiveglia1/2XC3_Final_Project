import heapq

## Dijkstra without relax limitation

def dijkstra(graph, source):
    dist = {}
    prev = {}
    visited = set()

    for node in graph.adj:
        dist[node] = float('inf')
        prev[node] = None
    dist[source] = 0

    heap = [(0, source)]

    while heap:
        current_dist, u = heapq.heappop(heap)

        if u in visited:
            continue
        visited.add(u)

        for v in graph.adjacent_nodes(u):
            alt = dist[u] + graph.get_weight(u, v)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(heap, (alt, v))

    return dist, prev
