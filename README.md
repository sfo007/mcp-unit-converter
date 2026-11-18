# mcp-unit-converter

A small [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server that lets Claude convert **length**, **weight**, and **temperature** units accurately instead of guessing.

## Tools

| Tool | What it does | Units |
|------|--------------|-------|
| `convert_length` | Convert a length | mm, cm, m, km, in, ft, yd, mi |
| `convert_weight` | Convert a weight | mg, g, kg, oz, lb |
| `convert_temperature` | Convert a temperature | c, f, k |
| `list_units` | Show all supported units | - |

## Installation

Requires Python 3.10+.

```bash
git clone https://github.com/sfo007/mcp-unit-converter.git
cd mcp-unit-converter
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## Run the tests

```bash
pytest
```

## Try it with the MCP Inspector

```bash
npx @modelcontextprotocol/inspector mcp-unit-converter
```

## Connect to Claude Desktop

Open **Settings > Developer > Edit Config** and add this to `claude_desktop_config.json`
(see `claude_desktop_config.example.json`):

```json
{
  "mcpServers": {
    "unit-converter": {
      "command": "/ABSOLUTE/PATH/TO/mcp-unit-converter/.venv/bin/mcp-unit-converter"
    }
  }
}
```

On Windows, use `.venv\\Scripts\\mcp-unit-converter.exe` as the command path.
Restart Claude Desktop afterwards.

## Connect to Claude Code

```bash
claude mcp add unit-converter -- /ABSOLUTE/PATH/TO/mcp-unit-converter/.venv/bin/mcp-unit-converter
```

## Example prompts

- "Convert 10 km to miles."
- "What is 100 Celsius in Fahrenheit?"
- "How many pounds is 72 kg?"

## Project layout

```
src/unit_converter/converter.py   # pure conversion logic
src/unit_converter/server.py      # MCP tool definitions
tests/test_converter.py           # unit tests
```

## Adding a new unit

Add one line to the `LENGTH` or `WEIGHT` dict in `converter.py` (size relative to the base unit), then add a test.

## License

MIT
