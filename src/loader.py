import csv
import json

def load_stars(file_path):
    if file_path.endswith(".json"):
        with open(file_path, 'r') as f:
            return json.load(f)
    elif file_path.endswith(".csv"):
        with open(file_path, 'r') as f:
            return list(csv.DictReader(f))
    else:
        raise ValueError("Unsupported file format. Use. json or .csv")

def filter_stars_by_magnitude(stars, max_mag):
    return [s for s in stars if s["mag"] <= max_mag]

def sort_stars(stars, key="mag"):
    return sorted(stars, key = lambda s: s[key])

