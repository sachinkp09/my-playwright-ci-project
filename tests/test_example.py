import pytest
from src.logger import get_logger

logger = get_logger()

@pytest.mark.smoke
def test_example(page):
    logger.info("Starting test_example")

    page.goto("https://example.com")
    logger.info("Navigated to example.com")

    assert page.title() == "Example Domain"
    logger.info("Assertion passed")

    #  Optional manual screenshot (Playwright already captures on failure)
    page.screenshot(path="screenshots/test_example.png")
    logger.info("Screenshot saved: screenshots/test_example.png")
