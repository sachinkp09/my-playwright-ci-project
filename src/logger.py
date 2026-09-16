import logging
import os

def get_logger(name="playwright-tests"):
    # Ensure logs directory exists
    os.makedirs("logs", exist_ok=True)

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers
    if not logger.handlers:
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        console_handler.setFormatter(console_format)
        logger.addHandler(console_handler)

        # File handler
        file_handler = logging.FileHandler("logs/test_log.txt")
        file_handler.setLevel(logging.INFO)
        file_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)

    return logger
