import sys
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright
from src.logger import get_logger
import os

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

logger = get_logger()

def test_example():
    logger.info("Starting test_example")

    # Ensure folders exist
    os.makedirs(ROOT_DIR / "screenshots", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://example.com")
        logger.info("Navigated to example.com")

        assert page.title() == "Example Domain"
        logger.info("Assertion passed")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = ROOT_DIR / "screenshots" / f"test_example_{timestamp}.png"
        page.screenshot(path=str(screenshot_path))
        logger.info(f"Screenshot saved: {screenshot_path}")

        browser.close()
        logger.info("Browser closed")
