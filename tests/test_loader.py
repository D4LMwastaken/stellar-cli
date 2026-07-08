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