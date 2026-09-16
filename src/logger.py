import logging
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

def get_logger():
    logger = logging.getLogger("playwright-tests")
    logger.setLevel(logging.INFO)

    # Console output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # File output
    log_dir = ROOT_DIR / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    file_handler = logging.FileHandler(log_dir / "test_log.txt")
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
