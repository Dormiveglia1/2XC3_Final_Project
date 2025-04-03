import pickle
from directed_weighted_graph import DirectedWeightedGraph
import time
import timeit 
from Part4_A_star import A_Star
from Part5_dijkstra import dijkstra
import numpy as np
import matplotlib.pyplot as plt

with open('Part5_station_graph_data.pkl', 'rb') as file:
    station_graph = pickle.load(file)

with open('Part5_heuristic.pkl', 'rb') as file:
    heuristics = pickle.load(file)

with open('Part5_line_info.pkl', 'rb') as file:
    line_info = pickle.load(file)

# Make sure the heuristic function can be accepted by A* algorithm
def h(source, destination):
    return heuristics[(source, destination)]

# print(station_graph.adj)
# print(h(5,188))

def dijkstra_paths(graph, source, destination):
    dist, prev = dijkstra(graph, source)
    
    # Trace path: Start from the target node and trace back to the source node
    path = []
    step = destination
    if prev[step] is None and step != source:
        return path  # If the predecessor of the target node is empty and not the starting point, it cannot be reached and an empty list is returned
    while step is not None:
        path.append(step)
        step = prev[step]
    
    # The path is currently in the order from the destination to the source and needs to be reversed
    path.reverse()
    
    return path

def calculate_transfers(path, line_info):
    transfers = 0
    for i in range(1, len(path) - 1):
        if line_info.get((path[i-1], path[i])) != line_info.get((path[i], path[i+1])):
            transfers += 1
    return transfers

def calculate_average_times(results):
    transfers_0 = [dur for (dur, trans) in results if trans == 0]
    transfers_1 = [dur for (dur, trans) in results if trans == 1]
    transfers_2_plus = [dur for (dur, trans) in results if trans > 1]

    avg_0 = np.mean(transfers_0) if transfers_0 else 0
    avg_1 = np.mean(transfers_1) if transfers_1 else 0
    avg_2_plus = np.mean(transfers_2_plus) if transfers_2_plus else 0

    return [avg_0, avg_1, avg_2_plus]

def draw_comparison_chart(avg_a_star, avg_dijkstra, labels, title="Average Time by Number of Transfers and Algorithm", xlabel="Number of Transfers", ylabel="Average Time (s)"):
    """
    Draws a bar chart comparing average times of A* and Dijkstra algorithms.
    """
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, avg_a_star, width, label='A*')
    rects2 = ax.bar(x + width/2, avg_dijkstra, width, label='Dijkstra')

    # Add text for labels, title, and custom x-axis tick labels, etc.
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    # Attach a text label above each bar in rects1 and rects2, displaying its height
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()

################################################# MAIN EXPERIMENT ###########################################################
"""
# A*
start_time = time.time()
_, a_star_path = A_Star(station_graph, 1, 303, h)
a_star_duration = time.time() - start_time
a_star_transfers = calculate_transfers(a_star_path, line_info)

# Dijkstra
start_time = time.time()
dijkstra_path = dijkstra_paths(station_graph, 1, 303)
dijkstra_duration = time.time() - start_time
dijkstra_transfers = calculate_transfers(dijkstra_path, line_info)

print(f"A* Duration: {a_star_duration}s, Transfers: {a_star_transfers}")
print(f"Dijkstra Duration: {dijkstra_duration}s, Transfers: {dijkstra_transfers}")
"""


def main(station_graph, line_info, num_stations=303, skip_station=189):
    a_star_results = []
    dijkstra_results = []
    
    for i in range(1, num_stations+1):
        if i == skip_station:
            continue
        for j in range(i+1, num_stations+1):
            if j == skip_station:
                continue
            
            # A* Algorithm
            start_time = timeit.default_timer()
            _, a_star_path = A_Star(station_graph, i, j, h)
            a_star_duration = timeit.default_timer() - start_time
            
            a_star_transfers = calculate_transfers(a_star_path, line_info)
            a_star_results.append((a_star_duration, a_star_transfers))

            # Dijkstra Algorithm
            start_time = timeit.default_timer()
            dijkstra_path = dijkstra_paths(station_graph, i, j)
            dijkstra_duration = timeit.default_timer() - start_time
            dijkstra_transfers = calculate_transfers(dijkstra_path, line_info)
            dijkstra_results.append((dijkstra_duration, dijkstra_transfers))
            """
            print(i,j,"a_star:",a_star_duration,a_star_transfers)
            print(i, j, "dijkstra:", dijkstra_duration, dijkstra_transfers)
            """
        
    '''
    i = 175
    j = 174

    start_time = timeit.default_timer()
    _, a_star_path = A_Star(station_graph, i, j, h)
    a_star_duration = timeit.default_timer() - start_time
    print(a_star_path)
    a_star_transfers = calculate_transfers(a_star_path, line_info)
    a_star_results.append((a_star_duration, a_star_transfers))

    # Dijkstra Algorithm
    start_time = timeit.default_timer()
    dijkstra_path = dijkstra_paths(station_graph, i, j)
    print(dijkstra_path)
    dijkstra_duration = timeit.default_timer() - start_time
    dijkstra_transfers = calculate_transfers(dijkstra_path, line_info)
    dijkstra_results.append((dijkstra_duration, dijkstra_transfers))
    print(i,j,"a_star:",a_star_duration,a_star_transfers)
    print(i, j, "dijkstra:", dijkstra_duration, dijkstra_transfers)
    '''
    # Calculate average times for A*
    avg_a_star = calculate_average_times(a_star_results)
    # Calculate average times for Dijkstra
    avg_dijkstra = calculate_average_times(dijkstra_results)
    
    print(f"A* Average Times: 0 transfers: {avg_a_star[0]}s, 1 transfer: {avg_a_star[1]}s, >1 transfers: {avg_a_star[2]}s")
    print(f"Dijkstra Average Times: 0 transfers: {avg_dijkstra[0]}s, 1 transfer: {avg_dijkstra[1]}s, >1 transfers: {avg_dijkstra[2]}s")
    labels = ['0 transfers', '1 transfer', '>1 transfers']
    draw_comparison_chart(avg_a_star, avg_dijkstra, labels)

if __name__ == "__main__":
    main(station_graph, line_info)
    # print(station_graph.adj[174])
    