import sys
from pathlib import Path
from datetime import datetime
from src.logger import get_logger

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

logger = get_logger()


def test_example(context, page):
    logger.info("Starting test_example")

    page.goto("https://example.com")
    logger.info("Navigated to example.com")

    assert page.title() == "Example Domain"
    logger.info("Assertion passed")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = f"{ROOT_DIR}/screenshots/test_example_{timestamp}.png"
    page.screenshot(path=screenshot_path)
    logger.info(f"Screenshot saved: {screenshot_path}")
