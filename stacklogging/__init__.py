import structlog
import logging
import sys

from .processors import (
    add_severity,
    add_timestamp,
    add_service_context,
    add_context,
    rename_event,
)

logging.basicConfig(format="%(message)s", stream=sys.stdout, level=logging.INFO)

structlog.configure(
    processors=[
        rename_event,
        add_severity,
        add_timestamp,
        add_service_context,
        add_context,
        structlog.processors.JSONRenderer(),
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)
