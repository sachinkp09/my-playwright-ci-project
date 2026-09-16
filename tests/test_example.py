import sys
from pathlib import Path

# Add project root to sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))
from datetime import datetime
from playwright.sync_api import sync_playwright
from src.logger import get_logger

logger = get_logger()

def test_example():
    logger.info("Starting test_example")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://example.com")
        logger.info("Navigated to example.com")

    # Assertion
        assert page.title() == "Example Domain"
        logger.info("Assertion passed: title is 'Example Domain'")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = (
            f"{ROOT_DIR}/screenshots/test_example_{timestamp}.png"
        )
        page.screenshot(path=screenshot_path)
        logger.info(f"Screenshot saved: {screenshot_path}")

        browser.close()
        logger.info("Browser closed")
