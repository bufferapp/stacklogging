from stacklogging.main import StackloggingHandler
import logging


def getLogger(name=None, level=logging.DEBUG, formatter=None):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    logger_handler = StackloggingHandler()
    logger_handler.setLevel(level)
    if formatter:
        logger_handler.setFormatter(formatter)

    logger.addHandler(logger_handler)

    return logger
