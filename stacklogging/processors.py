import time
import math


def add_timestamp(logger, method_name, event_dict):
    ct = time.time()
    subsecond, second = math.modf(ct)

    event_dict["timestamp"] = {"seconds": int(second), "nanos": int(subsecond * 1e9)}

    return event_dict


def add_severity(logger, method_name, event_dict):
    event_dict["severity"] = method_name
    return event_dict


def add_service_context(logger, method_name, event_dict):

    record = event_dict.get("_record")

    if record is None:
        service = logger.name
    else:
        service = record.name

    event_dict["serviceContext"] = {"service": service}

    return event_dict


def add_context(logger, method_name, event_dict):

    function_name = event_dict.get("function_name", None)

    event_dict["context"] = {"functionName": function_name}
    return event_dict


def rename_event(logger, method_name, event_dict):
    event_dict["message"] = event_dict.pop("event")
    return event_dict
