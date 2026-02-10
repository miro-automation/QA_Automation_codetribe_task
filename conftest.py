"""
Pytest hooks and fixtures. Driver for tests.
"""
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from config.settings import BASE_URL, IMPLICIT_WAIT, PAGE_LOAD_TIMEOUT


@pytest.fixture(scope="function")
def driver():
    """Chrome WebDriver; opens BASE_URL. Quit after test."""
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(IMPLICIT_WAIT)
    browser.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
    browser.get(BASE_URL)
    yield browser
    time.sleep(2)  # Short pause to see result before closing (can be removed)
    browser.quit()
