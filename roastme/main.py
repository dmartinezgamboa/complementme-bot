import csv, json

from client import TOKEN, RoastMeClient


def load_csv_data(file_path):
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        roasts = []
        for row in reader:
            roasts.append(row[0])
    return roasts

def load_json_data(file_path):
    f = open(file_path, mode='r')
    roast_pieces = json.load(f)
    f.close()
    return roast_pieces


if __name__ == "__main__":
    roasts_parts = load_json_data(file_path='data/roasts_parts_file.json')
    roasts_full = load_csv_data(file_path='data/roasts_full_file.csv')
    roastme = RoastMeClient(roasts_parts, roasts_full)
    roastme.run(TOKEN)
