from src.display import render_table

def test_render_table_returns_string():
    stars = [
        {"name": "Sirius", "ra": 6.75, "dec": -16.71, "mag": -1.46},
    ]

    table = render_table(stars)

    assert isinstance(table, str)
    assert "Sirius" in table

from src.display import colorize_magnitude

def test_colorize_magnitude_adds_color():
    result = colorize_magnitude(-1.5)
    assert "\x1b[" in result
    assert "1.5" in result