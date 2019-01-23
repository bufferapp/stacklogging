# Stacklogging

[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)
[![PyPI version](https://badge.fury.io/py/mongoct.svg)](https://badge.fury.io/py/stacklogging)

This small library generates log entries that are understood by Stackdriver Logging. You won't need to authenticate in GCE. The logs emmited will be in [JSON schema understood by Stackdriver API](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry).

## Installation

You can use `pip` to install `stacklogging`:

```bash
pip install stacklogging
```

## Usage

```python
import stacklogging

logger = stacklogging.getLogger()

def sum(a, b):
    logger.info(f"Adding {a} and {b}")
    return a + b

r = sum(2, 4)
```

This will output a JSON like this one:

```json
{
    "message": "Adding 2 and 4",
    "timestamp": {
        "seconds": 1548239928,
        "nanos": 380779027
    },
    "thread": 140619343472128,
    "severity": "INFO",
    "sourceLocation": {
        "file": "test.py",
        "function": "sum"
    }
}
```

## License

MIT © Buffer
