import csv
import pickle

def read_line_info(file_path):
    line_info = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            station1 = int(row['station1'])
            station2 = int(row['station2'])
            line = int(row['line'])
            line_info[(station1, station2)] = line
            line_info[(station2, station1)] = line
    return line_info

if __name__ == '__main__':
    line_info_file = 'london_stations.csv'
    line_info = read_line_info('london_connections.csv')
    with open('Part5_line_info.pkl', 'wb') as f:
        pickle.dump(line_info, f)

