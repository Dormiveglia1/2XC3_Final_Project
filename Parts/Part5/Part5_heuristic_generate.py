import csv
from math import radians, sin, cos, sqrt, atan2
from directed_weighted_graph import DirectedWeightedGraph
import pickle

def Distance(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c

def read_stations(file_path):
    stations = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id_ = int(row['id'])
            lat = float(row['latitude'])
            lon = float(row['longitude'])
            stations[id_] = (lat, lon)
    return stations

def calculate_distances(stations):
    distances = {}
    ids = list(stations.keys())
    for i in range(len(ids)):
        for j in range(i, len(ids)):  # use i to make sure include self comparison
            id1, id2 = ids[i], ids[j]
            if id1 == id2:
                distances[(id1, id2)] = 0  # Set the distance to 0 if the stations are the same
            else:
                lat1, lon1 = stations[id1]
                lat2, lon2 = stations[id2]
                distance = Distance(lat1, lon1, lat2, lon2)
                distances[(id1, id2)] = distance
                distances[(id2, id1)] = distance  # Make sure the distance is two-way
    return distances


if __name__ == '__main__':
    stations_file = 'london_stations.csv'
    stations = read_stations(stations_file)
    distances = calculate_distances(stations)
    with open('Part5_heuristic.pkl', 'wb') as f:
        pickle.dump(distances, f)
