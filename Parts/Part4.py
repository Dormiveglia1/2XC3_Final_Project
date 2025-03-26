import heapq
import random

class DirectedWeightedGraph:

    def __init__(self, nodes):
        self.adj = {}
        self.weights = {}
        for i in range(nodes):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        for neighbour in self.adj[node1]:
            if neighbour == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2, weight):
        if node2 not in self.adj[node1]:
            self.adj[node1].append(node2)
        self.weights[(node1, node2)] = weight

    # if two nodes are connnected, get its weight
    def get_weight(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]

    def number_of_nodes(self):
        return len(self.adj)

def A_Star(graph, source, destination, heuristic):
    # initilization
    open_set = [(0, source)]  # initialize the heap with the a tuple: (total estimate weight for the node to reach the target, node)
    visited = set() # make sure each node can be accessed only once
    h = {source: heuristic(source)}  # dictionary to store heuristic values for each node
    g = {source: 0}  # the weight from the source node to the current node
    f = {source: (heuristic(source) + 0)}  # f = g + h
    predecessor = {}  # record the path
    
    while open_set:
        # get the node with the lowest total estimate weight from the heap
        _, current = heapq.heappop(open_set) # we only need the node hence ignore the weight
        
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
        
        # if not, add it into the visited nodes list
        visited.add(current)
        
        # traverse all the neighbor nodes
        for neighbor in graph.adjacent_nodes(current):
            # if the node has been visited, ignore it
            if neighbor in visited:
                continue
            
            # if not, calculate the g value (the total weight required to reach this node)
            g_weight = g[current] + graph.get_weight(current, neighbor)
            
            # if the neighbor node is a new node, or the new path is better, update the information
            if neighbor not in g or g_weight < g[neighbor]:
                predecessor[neighbor] = current
                g[neighbor] = g_weight
                h[neighbor] = heuristic(neighbor)  # store the heuristic value for the neighbor
                f[neighbor] = g[neighbor] + h[neighbor]
                heapq.heappush(open_set, (f[neighbor], neighbor))
    
    # if no path was found, return the predecessor dictionary and a null list
    return predecessor, []

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

# just return 0
def heuristic(node):
    return 0

graph = create_random_graph(10, 12)

print(graph.adj)
print(graph.weights)

predecessor, path = A_Star(graph, 0, 7, heuristic)
print(predecessor)
print(path)