# brottsplatskartan
A simple API wrapper for [Brottsplatskartan](brottsplatskartan.se)

## Install

`pip install brottsplatskartan`

## Usage

```python
import brottsplatskartan

b = brottsplatskartan.BrottsplatsKartan(app=app, area=area, longitude=longitude, latitude=latitude)

for incident in b.get_incidents():
  print(incident)
```

## Development

Pull requests welcome. Must pass `tox` and include tests.

## Disclaimer

Not affiliated with brottsplatskartan.se. Use at your own risk.
