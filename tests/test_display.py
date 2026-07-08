from src.display import render_table

def test_render_table_returns_string():
    stars = [
        {"name": "Sirius", "ra": 6.75, "dec": -16.71, "mag": -1.46},
    ]

    table = render_table(stars)

    assert isinstance(table, str)
    assert "Sirius" in table