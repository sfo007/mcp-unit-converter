import pytest

from unit_converter import converter


def test_km_to_miles():
    assert converter.convert_length(10, "km", "mi") == pytest.approx(6.2137, rel=1e-4)


def test_feet_to_cm():
    assert converter.convert_length(1, "ft", "cm") == pytest.approx(30.48)


def test_kg_to_lb():
    assert converter.convert_weight(1, "kg", "lb") == pytest.approx(2.20462, rel=1e-4)


def test_celsius_to_fahrenheit():
    assert converter.convert_temperature(100, "c", "f") == pytest.approx(212)


def test_fahrenheit_to_kelvin():
    assert converter.convert_temperature(32, "f", "k") == pytest.approx(273.15)


def test_case_and_spaces_ignored():
    assert converter.convert_length(1, " KM ", "M") == pytest.approx(1000)


def test_unknown_unit():
    with pytest.raises(ValueError):
        converter.convert_length(1, "parsec", "m")


def test_below_absolute_zero():
    with pytest.raises(ValueError):
        converter.convert_temperature(-300, "c", "k")
