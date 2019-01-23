import logging
import json
import math


def format_stackdriver_json(record, message):
    subsecond, second = math.modf(record.created)

    payload = {
        "message": message,
        "timestamp": {"seconds": int(second), "nanos": int(subsecond * 1e9)},
        "thread": record.thread,
        "severity": record.levelname,
        "sourceLocation": {"file": record.filename, "function": record.funcName},
    }

    return json.dumps(payload)


class StackloggingHandler(logging.StreamHandler):
    def __init__(self, stream=None):
        super(StackloggingHandler, self).__init__()

    def format(self, record):

        message = super(StackloggingHandler, self).format(record)
        return format_stackdriver_json(record, message)
