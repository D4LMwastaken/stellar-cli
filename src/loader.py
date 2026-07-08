import json

def load_stars(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)