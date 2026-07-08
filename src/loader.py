import json

def load_stars(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def filter_stars_by_magnitude(stars, max_mag):
    return [s for s in stars if s["mag"] <= max_mag]

def sort_stars(stars, key="mag"):
    return sorted(stars, key = lambda s: s[key])

