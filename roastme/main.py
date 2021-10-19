import json

from client import TOKEN, RoastMeClient


def load_json_data(file_path):
    f = open(file_path, mode='r')
    data = json.load(f)
    f.close()
    return data


if __name__ == "__main__":
    data = load_json_data(file_path='data.json')
    roastme = RoastMeClient(data)
    roastme.run(TOKEN)
