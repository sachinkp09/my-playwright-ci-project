import time
from datetime import datetime
from playwright.sync_api import sync_playwright
from src.logger import get_logger

logger = get_logger()

def run_playwright_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")

        logger.info("Opened example.com")
        logger.info(f"Page title: {page.title()}")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = (
            "C:/Users/sachi/Downloads/Python_Project/CI_CD_Project/"
            "my-playwright-ci-project/screenshots/app_example_"
            f"{timestamp}.png"
        )
        page.screenshot(path=screenshot_path)
        logger.info(f"Screenshot saved: {screenshot_path}")

        time.sleep(5)
        browser.close()
        logger.info("Browser closed")

if __name__ == "__main__":
    run_playwright_test()
