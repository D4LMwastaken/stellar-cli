import pytest
import json
import os
from src.loader import load_stars

def test_load_stars_return_expected_data():
    file_path = "data/stars.json"

    data = load_stars(file_path)

    assert len(data) == 2
    assert data[0]["name"] == "Sirius"
    assert data[1]["mag"] == 0.03

from src.loader import filter_stars_by_magnitude
def test_filter_stars_by_magnitude():
    stars = [
        {"name": "Dim", "mag": 5.0},
        {"name": "Bright", "mag": -1.0}
    ]

    filtered = filter_stars_by_magnitude(stars, 0.0)

    assert len(filtered) == 1
    assert filtered[0]["name"] == "Bright"

from src.loader import sort_stars

def test_sort_stars_by_magnitude():
    stars = [
        {"name": "Dim", "mag": 5.0},
        {"name": "Bright", "mag": -1.0}
    ]
    sorted_stars = sort_stars(stars, key="mag")
    assert sorted_stars[0]["name"] == "Bright"
    assert sorted_stars[1]["name"] == "Dim"
