# Stacklogging

[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)
[![PyPI version](https://badge.fury.io/py/mongoct.svg)](https://badge.fury.io/py/stacklogging)

Log entries in Stackdriver Logging without having to authenticate in GCE. This package will format logs in the [JSON schema understood by Stackdriver API](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry).

## Installation

You can use `pip` to install `stacklogging`:

```
pip install stacklogging
```

## Usage

```python
from stacklogging import structlog

log = structlog.get_logger("example")

log.info("This is an information message", this_is_a_custom_key=500)
```

This will print to `STDOUT` a JSON similar to this:

```json
{
  "this_is_a_custom_key": 500,
  "message": "This is an information message",
  "severity": "info",
  "timestamp": { "seconds": 1537263851, "nanos": 200867414 },
  "serviceContext": { "service": "example" },
  "context": { "functionName": "example" }
}
```

Stackdriver Logging will be able to read `severity` aswell as `context`.

## License

MIT © Buffer
