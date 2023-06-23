# data_loader.py

import json

def load_item_from_file(filename, item_name):
    with open(filename) as file:
        data = json.load(file)
        name = data.get("name")
        attributes = data.get("attributes")
        return name, attributes

