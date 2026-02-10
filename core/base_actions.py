"""
Single file with all reusable UI methods. Used project-wide.
All element interactions go through this class; locators come from JSON.
"""
from pathlib import Path
import json
from typing import List, Tuple

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.settings import IMPLICIT_WAIT

# Map JSON "by" string to Selenium By
BY_MAP = {
    "id": By.ID,
    "xpath": By.XPATH,
    "css": By.CSS_SELECTOR,
    "name": By.NAME,
    "class": By.CLASS_NAME,
    "tag": By.TAG_NAME,
    "link_text": By.LINK_TEXT,
    "partial_link_text": By.PARTIAL_LINK_TEXT,
}


class BaseActions:
    """
    Central place for all UI actions. Loads locators from JSON.
    Every click, type, get_text etc. is done through these methods.
    """

    _locators: dict = {}
    _locators_path: Path = Path(__file__).resolve().parent.parent / "locators" / "locators.json"

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self._load_locators()

    def _load_locators(self) -> None:
        """Load locators from JSON once."""
        if not BaseActions._locators:
            with open(BaseActions._locators_path, encoding="utf-8") as f:
                BaseActions._locators = json.load(f)

    def _get_locator(self, section: str, key: str) -> Tuple[By, str]:
        """Resolve section.key to (By.XXX, value)."""
        section_data = self._locators.get(section)
        if not section_data:
            raise KeyError(f"Locator section '{section}' not found in locators.json")
        item = section_data.get(key)
        if not item:
            raise KeyError(f"Locator key '{key}' not in section '{section}'")
        by_str = item.get("by", "id").lower()
        value = item.get("value", "")
        by = BY_MAP.get(by_str, By.ID)
        return by, value

    def click(self, section: str, key: str, timeout: int = IMPLICIT_WAIT) -> None:
        """Click element identified by section and key in locators.json."""
        by, value = self._get_locator(section, key)
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()

    def send_keys(self, section: str, key: str, text: str, clear_first: bool = True) -> None:
        """Type text into element. Optionally clear before typing."""
        by, value = self._get_locator(section, key)
        element = WebDriverWait(self.driver, IMPLICIT_WAIT).until(
            EC.visibility_of_element_located((by, value))
        )
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_text(self, section: str, key: str, timeout: int = IMPLICIT_WAIT) -> str:
        """Get visible text of element."""
        by, value = self._get_locator(section, key)
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )
        return element.text.strip()

    def get_attribute(self, section: str, key: str, attribute: str) -> str:
        """Get attribute value of element."""
        by, value = self._get_locator(section, key)
        element = WebDriverWait(self.driver, IMPLICIT_WAIT).until(
            EC.presence_of_element_located((by, value))
        )
        return element.get_attribute(attribute) or ""

    def is_displayed(self, section: str, key: str, timeout: int = IMPLICIT_WAIT) -> bool:
        """Check if element is displayed."""
        by, value = self._get_locator(section, key)
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return element.is_displayed()
        except Exception:
            return False

    def wait_visible(self, section: str, key: str, timeout: int = IMPLICIT_WAIT) -> WebElement:
        """Wait until element is visible; return the element."""
        by, value = self._get_locator(section, key)
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )

    def find_element(self, section: str, key: str, timeout: int = IMPLICIT_WAIT) -> WebElement:
        """Find single element by locator from JSON."""
        by, value = self._get_locator(section, key)
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def find_elements(self, section: str, key: str, timeout: int = IMPLICIT_WAIT) -> List[WebElement]:
        """Find all elements matching locator from JSON."""
        by, value = self._get_locator(section, key)
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return self.driver.find_elements(by, value)

    def select_by_value(self, section: str, key: str, value: str) -> None:
        """Select option by value in a dropdown (e.g. sort)."""
        from selenium.webdriver.support.ui import Select
        element = self.find_element(section, key)
        select = Select(element)
        select.select_by_value(value)
