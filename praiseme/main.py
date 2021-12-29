import csv, json

from client import TOKEN, PraiseMeClient


def load_csv_data(file_path):
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        praise = []
        for row in reader:
            praise.append(row[0])
    return praise

def load_json_data(file_path):
    f = open(file_path, mode='r')
    complement_pieces = json.load(f)
    f.close()
    return complement_pieces


if __name__ == "__main__":
    praise_parts = load_json_data(file_path='data/praise_parts_file.json')
    praise_full = load_csv_data(file_path='data/praise_full_file.csv')
    praise = PraiseMeClient(praise_parts, praise_full)
    praise.run(TOKEN)
