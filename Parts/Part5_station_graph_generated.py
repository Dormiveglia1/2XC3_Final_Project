import csv
from math import radians, sin, cos, sqrt, atan2
from directed_weighted_graph import DirectedWeightedGraph
import pickle

def convert_value(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value

def Read_Stations(file_path):
    data_dict = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            id_ = int(row.pop('id'))
            cleaned_row = {
                key: convert_value(value) 
                for key, value in row.items()
            }
            data_dict[id_] = cleaned_row
    return data_dict

file_path = r"F:\Mcmaster\2024~2025_Winter\2XC3\2XC3_Final_Project\london_stations.csv"
station_dict = Read_Stations(file_path)
'''
for id, data in station_dict.items():
    print(f"ID: {id}, Data: {data}")
'''
def Distance(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c

distance_dict = {}

csv_path = r"F:\Mcmaster\2024~2025_Winter\2XC3\2XC3_Final_Project\london_connections.csv"
with open(csv_path, mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        station1 = int(row['station1'])
        station2 = int(row['station2'])
        line = int(row['line'])
        time = int(row['time'])

        st1_info = station_dict.get(station1)
        st2_info = station_dict.get(station2)

        if st1_info and st2_info:
            distance = Distance(
                st1_info['latitude'], st1_info['longitude'],
                st2_info['latitude'], st2_info['longitude']
            )
            
            rounded_distance = round(distance, 4)
            distance_dict[rounded_distance] = (station1, station2, line, time)

station_graph = DirectedWeightedGraph(max(station_dict.keys()) + 1)

for distance, (station1, station2, line, time) in distance_dict.items():
    station_graph.add_edge(station1, station2, distance)
    station_graph.add_edge(station2, station1, distance)

try:
    with open('Part5_station_graph_data.pkl', 'wb') as file:
        pickle.dump(station_graph, file)
except Exception as e:
    print(f"Errpr: {e}")
