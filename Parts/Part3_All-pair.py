def All_Pair_Shortest(graph):
    n = len(graph)
    distance = [[float('inf')] * n for _ in range(n)]
    previous = [[None] * n for _ in range(n)]
    
    # Initialize distance and previous matrices
    for u in range(n):
        distance[u][u] = 0
        for v, weight in graph[u]:
            distance[u][v] = weight
            previous[u][v] = u
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    previous[i][j] = previous[k][j]
    
    # Check for negative cycles
    for u in range(n):
        if distance[u][u] < 0:
            raise ValueError("Graph contains a negative-weight cycle")
    
    return distance, previous

# Time complexity is V^3