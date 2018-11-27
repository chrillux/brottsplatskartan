# brottsplatskartan [![Build Status](https://travis-ci.com/chrillux/brottsplatskartan.svg?branch=master)](https://travis-ci.com/chrillux/brottsplatskartan)

A simple API wrapper for [Brottsplatskartan](https://brottsplatskartan.se)

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
