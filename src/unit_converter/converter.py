"""Pure conversion logic. No MCP code here, so it is easy to test."""

# Each unit maps to its size in a base unit (metres for length, grams for weight).
LENGTH = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mi": 1609.344,
}

WEIGHT = {
    "mg": 0.001,
    "g": 1.0,
    "kg": 1000.0,
    "oz": 28.349523125,
    "lb": 453.59237,
}

TEMPERATURE = ("c", "f", "k")


def _normalize(unit: str) -> str:
    return unit.strip().lower()


def convert_linear(value: float, from_unit: str, to_unit: str, table: dict, kind: str) -> float:
    """Convert between units that are simple multiples of a base unit."""
    src, dst = _normalize(from_unit), _normalize(to_unit)
    for u in (src, dst):
        if u not in table:
            raise ValueError(
                f"Unknown {kind} unit '{u}'. Supported: {', '.join(table)}"
            )
    return value * table[src] / table[dst]


def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    return convert_linear(value, from_unit, to_unit, LENGTH, "length")


def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
    return convert_linear(value, from_unit, to_unit, WEIGHT, "weight")


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """Convert between Celsius (c), Fahrenheit (f) and Kelvin (k)."""
    src, dst = _normalize(from_unit), _normalize(to_unit)
    for u in (src, dst):
        if u not in TEMPERATURE:
            raise ValueError(
                f"Unknown temperature unit '{u}'. Supported: {', '.join(TEMPERATURE)}"
            )

    # Step 1: convert to Celsius.
    if src == "c":
        celsius = value
    elif src == "f":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15

    if celsius < -273.15:
        raise ValueError("Temperature is below absolute zero.")

    # Step 2: convert Celsius to the target unit.
    if dst == "c":
        return celsius
    if dst == "f":
        return celsius * 9 / 5 + 32
    return celsius + 273.15
