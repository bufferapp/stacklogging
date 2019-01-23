from stacklogging.main import StackloggingHandler
import logging


def getLogger(name=None, level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    logger_handler = StackloggingHandler()
    logger_handler.setLevel(level)
    logger.addHandler(logger_handler)

    return logger
