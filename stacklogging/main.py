import logging
import json
import math

RESERVED = frozenset(
    (
        "args",
        "asctime",
        "created",
        "exc_info",
        "exc_text",
        "filename",
        "funcName",
        "id",
        "levelname",
        "levelno",
        "lineno",
        "module",
        "msecs",
        "message",
        "msg",
        "name",
        "pathname",
        "process",
        "processName",
        "relativeCreated",
        "stack_info",
        "thread",
        "threadName",
    )
)


def get_extra_keys(record, reserved=RESERVED):
    extra_keys = []
    for key, value in record.__dict__.items():
        if key not in reserved and not key.startswith("_"):
            extra_keys.append(key)
    return extra_keys


def format_stackdriver_json(record, message):
    subsecond, second = math.modf(record.created)

    payload = {
        "message": message,
        "timestamp": {"seconds": int(second), "nanos": int(subsecond * 1e9)},
        "thread": record.thread,
        "severity": record.levelname,
    }

    extra_keys = get_extra_keys(record)

    for key in extra_keys:
        try:
            json.dumps(record.__dict__[key])  # serialization/type error check
            payload[key] = record.__dict__[key]
        except TypeError:
            payload[key] = str(record.__dict__[key])

    return json.dumps(payload)


class StackloggingHandler(logging.StreamHandler):
    def __init__(self, stream=None):
        super(StackloggingHandler, self).__init__()

    def format(self, record):

        message = super(StackloggingHandler, self).format(record)
        return format_stackdriver_json(record, message)
