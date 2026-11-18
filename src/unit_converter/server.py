"""MCP server exposing unit conversion tools to Claude."""

from mcp.server.fastmcp import FastMCP

from . import converter

mcp = FastMCP("unit-converter")


def _fmt(value: float) -> str:
    return f"{value:.6g}"


@mcp.tool()
def convert_length(value: float, from_unit: str, to_unit: str) -> str:
    """Convert a length. Units: mm, cm, m, km, in, ft, yd, mi."""
    result = converter.convert_length(value, from_unit, to_unit)
    return f"{_fmt(value)} {from_unit} = {_fmt(result)} {to_unit}"


@mcp.tool()
def convert_weight(value: float, from_unit: str, to_unit: str) -> str:
    """Convert a weight or mass. Units: mg, g, kg, oz, lb."""
    result = converter.convert_weight(value, from_unit, to_unit)
    return f"{_fmt(value)} {from_unit} = {_fmt(result)} {to_unit}"


@mcp.tool()
def convert_temperature(value: float, from_unit: str, to_unit: str) -> str:
    """Convert a temperature. Units: c (Celsius), f (Fahrenheit), k (Kelvin)."""
    result = converter.convert_temperature(value, from_unit, to_unit)
    return f"{_fmt(value)} {from_unit} = {_fmt(result)} {to_unit}"


@mcp.tool()
def list_units() -> str:
    """List every unit this server supports."""
    return (
        f"Length: {', '.join(converter.LENGTH)}\n"
        f"Weight: {', '.join(converter.WEIGHT)}\n"
        f"Temperature: {', '.join(converter.TEMPERATURE)}"
    )


def main() -> None:
    mcp.run()  # stdio transport by default


if __name__ == "__main__":
    main()
