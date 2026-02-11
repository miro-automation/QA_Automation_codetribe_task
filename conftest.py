"""
Pytest hooks and fixtures. Driver for tests.
"""
import logging
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from config.settings import BASE_URL, IMPLICIT_WAIT, PAGE_LOAD_TIMEOUT

_log = logging.getLogger(__name__)

# Logging: show INFO in console so we see "Clicked on element ..." etc.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)


def pytest_configure(config):
    """Register custom markers so pytest does not warn."""
    config.addinivalue_line("markers", "pa: run with -m pa to execute these tests.")
    config.addinivalue_line("markers", "ui: tests that use browser (driver fixture).")
    config.addinivalue_line("markers", "smoke: smoke / sanity tests.")
    config.addinivalue_line("markers", "search: search functionality tests.")
    config.addinivalue_line("markers", "product_validation: product name and price validation.")


@pytest.fixture(scope="function")
def driver():
    """Chrome WebDriver; opens BASE_URL. Quit after test."""
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(IMPLICIT_WAIT)
    browser.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
    _log.info("Opening URL: %s", BASE_URL)
    browser.get(BASE_URL)
    yield browser
    time.sleep(2)  # Short pause to see result before closing (can be removed)
    browser.quit()
