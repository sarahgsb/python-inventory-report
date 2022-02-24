import json


def reader_json(path):
    with open(path) as file:
        json_content = json.load(file)
    return json_content
