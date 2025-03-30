import random
import time
import matplotlib.pyplot as plt
import heapq
import numpy as np
from memory_profiler import memory_usage
from directed_weighted_graph import DirectedWeightedGraph
from Part2_BellmanFord import bellman_ford
from Part2_Dijkstra import dijkstra
from create_random_graph import create_random_graph

def calculate_edges(nodes, density):
    """ Calculate the number of edges for a given number of nodes and density """
    return int(density * nodes * (nodes - 1))

def draw_plots(bf_total_distance, dj_total_distance, bf_times, dj_times, bf_memory, dj_memory, node, density, k):
    num_trials = len(bf_total_distance)
    x = np.arange(num_trials)
    width = 0.2

    avg_bf_distance = np.mean(bf_total_distance)
    avg_dj_distance = np.mean(dj_total_distance)
    avg_bf_times = np.mean(bf_times)
    avg_dj_times = np.mean(dj_times)
    avg_bf_memory = np.mean(bf_memory)
    avg_dj_memory = np.mean(dj_memory)

    plt.figure(figsize=(21, 6))
    plt.subplot(1, 3, 1)
    plt.bar(x - width/2, bf_total_distance, width, label='BF Total Distance', color='purple')
    plt.bar(x + width/2, dj_total_distance, width, label='DJ Total Distance', color='blue')
    plt.axhline(y=avg_bf_distance, color='purple', linestyle='dashed', label=f'Avg BF Dist: {avg_bf_distance:.2f}')
    plt.axhline(y=avg_dj_distance, color='blue', linestyle='dashed', label=f'Avg DJ Dist: {avg_dj_distance:.2f}')
    plt.xlabel('Trial Number')
    plt.ylabel('Total Distance')
    plt.title(f'Distances Comparison - Node: {node}, Density: {density}, K: {k}')
    plt.legend()

    plt.subplot(1, 3, 2)
    plt.bar(x - width/2, bf_times, width, label='BF Times', color='yellow')
    plt.bar(x + width/2, dj_times, width, label='DJ Times', color='red')
    plt.axhline(y=avg_bf_times, color='yellow', linestyle='dashed', label=f'Avg BF Time: {avg_bf_times:.2f}')
    plt.axhline(y=avg_dj_times, color='red', linestyle='dashed', label=f'Avg DJ Time: {avg_dj_times:.2f}')
    plt.xlabel('Trial Number')
    plt.ylabel('Execution Time (seconds)')
    plt.title(f'Times Comparison - Node: {node}, Density: {density}, K: {k}')
    plt.legend()

    plt.subplot(1, 3, 3)
    plt.bar(x - width/2, bf_memory, width, label='BF Memory Usage', color='green')
    plt.bar(x + width/2, dj_memory, width, label='DJ Memory Usage', color='orange')
    plt.axhline(y=avg_bf_memory, color='green', linestyle='dashed', label=f'Avg BF Memory: {avg_bf_memory:.2f}')
    plt.axhline(y=avg_dj_memory, color='orange', linestyle='dashed', label=f'Avg DJ Memory: {avg_dj_memory:.2f}')
    plt.xlabel('Trial Number')
    plt.ylabel('Memory Usage (MB)')
    plt.title(f'Memory Usage Comparison - Node: {node}, Density: {density}, K: {k}')
    plt.legend()

    plt.tight_layout()
    plt.show()

def run_experiment(nodes_list, density_list):
    for nodes in nodes_list:
        for density in density_list:
            edges = calculate_edges(nodes, density)
            graph = create_random_graph(nodes, edges)
            k_values = [1, max(1, nodes // 4), max(1, nodes // 2)]
            for k in k_values:
                bf_times = []
                dj_times = []
                bf_distances = []
                dj_distances = []
                bf_memory = []
                dj_memory = []

                for _ in range(15):
                    bf_distance = 0
                    start_mem = memory_usage(max_usage=True)
                    start_time = time.perf_counter()
                    distances_bf, paths_bf = bellman_ford(graph, 0, k)
                    bf_time = time.perf_counter() - start_time
                    end_mem = memory_usage(max_usage=True)
                    bf_memory_usage = end_mem - start_mem
                    bf_times.append(bf_time)
                    bf_memory.append(bf_memory_usage)
                    for i in distances_bf:
                        if distances_bf[i] == float('inf'):
                            distances_bf[i] = 0
                        bf_distance += distances_bf[i]
                    bf_distances.append(bf_distance)

                    dj_distance = 0
                    start_mem = memory_usage(max_usage=True)
                    start_time = time.perf_counter()
                    distances_dj, paths_dj = dijkstra(graph, 0, k)
                    dj_time = time.perf_counter() - start_time
                    end_mem = memory_usage(max_usage=True)
                    dj_memory_usage = end_mem - start_mem
                    dj_times.append(dj_time)
                    dj_memory.append(dj_memory_usage)
                    for i in distances_dj:
                        if distances_dj[i] == float('inf'):
                            distances_dj[i] = 0
                        dj_distance += distances_dj[i]
                    dj_distances.append(dj_distance)

                draw_plots(bf_distances, dj_distances, bf_times, dj_times, bf_memory, dj_memory, nodes, density, k)

if __name__ == '__main__':
    nodes_list = [10, 50, 100]
    density_list = [0.2, 0.4, 0.8]
    run_experiment(nodes_list, density_list)
