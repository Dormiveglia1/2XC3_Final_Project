import pickle
from directed_weighted_graph import DirectedWeightedGraph

with open('station_graph_data.pkl', 'rb') as file:
    station_graph = pickle.load(file)

print(station_graph.adj)