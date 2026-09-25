import pytest
from src.logger import get_logger

logger = get_logger()

@pytest.mark.regression
def test_google(page):
    logger.info("Starting test_google")


    # This line will never be reached, but it's fine
    page.goto("https://google.com")
    logger.info("Navigated to google.com")

    assert "Google" in page.title()
    logger.info("Assertion passed")

    page.screenshot(path="screenshots/test_google.png")
    logger.info("Screenshot saved: screenshots/test_google.png")