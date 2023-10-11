import logging
from pythonjsonlogger.jsonlogger import JsonFormatter


def setup_logger(name: str, log_file: str, level=logging.INFO) -> logging.Logger:
    """Set up file loggers in json format."""

    handler = logging.FileHandler(log_file)
    handler.setFormatter(JsonFormatter())

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
