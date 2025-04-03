import heapq
import random
from directed_weighted_graph import DirectedWeightedGraph
from create_random_graph import create_random_graph

def A_Star(graph, source, destination, heuristic):
    # initilization
    open_set = [(0, source)]  # initialize the heap with the a tuple: (total estimate weight for the node to reach the target, node)
    h = {source: heuristic(source, destination)}  # dictionary to store heuristic values for each node
    g = {source: 0}  # the weight from the source node to the current node
    f = {source: (heuristic(source, destination) + 0)}  # f = g + h
    predecessor = {}  # record the path
    visited = set()

    while open_set:
        # get the node with the lowest total estimate weight from the heap
        _, current = heapq.heappop(open_set) # we only need the node hence ignore the weight
        
        visited.add(current)
        
        # if destination has been reached then...
        if current == destination:
            # build and return the path
            path = []
            while current in predecessor:
                path.append(current)
                current = predecessor[current]
            path.append(source)
            path.reverse()
            return predecessor, path
        
        # traverse all the neighbor nodes
        for neighbor in graph.adjacent_nodes(current):     
            if neighbor in visited:
                continue
                
            # calculate the g value (the total weight required to reach this node)
            g_weight = g[current] + graph.get_weight(current, neighbor)
            
            # if the neighbor node is a new node, or the new path is better, update the information
            if neighbor not in g or g_weight < g[neighbor]:
                predecessor[neighbor] = current
                g[neighbor] = g_weight
                h[neighbor] = heuristic(neighbor, destination)  # store the heuristic value for the neighbor
                f[neighbor] = g[neighbor] + h[neighbor]
                heapq.heappush(open_set, (f[neighbor], neighbor))
    
    # if no path was found, return the predecessor dictionary and a null list
    return predecessor, []

# # just return 0
# def heuristic(node, destination):
#     return 0

# graph = create_random_graph(10, 20)

# print(graph.adj)
# print(graph.weights)

# predecessor, path = A_Star(graph, 0, 7, heuristic)
# print(predecessor)
# print(path)