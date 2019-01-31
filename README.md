# Stacklogging

[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)
[![PyPI version](https://badge.fury.io/py/mongoct.svg)](https://badge.fury.io/py/stacklogging)

This small library generates log entries that are understood by Stackdriver Logging. You won't need to authenticate in GCE. The logs emmited will be in [JSON schema understood by Stackdriver API](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) and [Stackdriver Logging](https://cloud.google.com/error-reporting/docs/formatting-error-messages).

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
        "function": "sum",
        "line": 6
    }
}
```

It is also possible to log extra fields at runtime using the `extra` parameter.

```python
logger.info("message", extra={"from": "Alice", "to": "Bob"})
```

Stacklogging will add the extra keys to the final JSON:

```json
{
    "message": "Email sent",
    "timestamp": {
        "seconds": 1548260191,
        "nanos": 256482124
    },
    "thread": 140166127678976,
    "severity": "INFO",
    "sourceLocation": {
        "file": "test.py",
        "function": "sum",
        "line": 9
    },
    "from": "Alice",
    "to": "Bob"
}
```

## License

MIT © Buffer
