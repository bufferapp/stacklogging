# Stacklogging

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

## License

MIT © Buffer
