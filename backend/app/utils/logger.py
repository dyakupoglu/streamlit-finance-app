import logging
import os
from logging.handlers import RotatingFileHandler


# Create a function to configure the logger
def get_logger(name: str) -> logging.Logger:
    # Define log directory and file
    LOGS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
    os.makedirs(LOGS_DIR, exist_ok=True)
    LOG_FILE = os.path.join(LOGS_DIR, f"{name}.log")

    # Create logger instance
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Define formatter
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(filename)s | %(funcName)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Create file handler (rotates after 5 MB)
    file_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=5
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    if not logger.hasHandlers():
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
