"""Base page: common behaviour and navigation. All pages inherit from this."""
from selenium.webdriver.remote.webdriver import WebDriver

from config.settings import BASE_URL
from core.base_actions import BaseActions


class BasePage:
    """Base for all page objects. Uses BaseActions for all element interactions."""

    def __init__(self, driver: WebDriver, path: str = "") -> None:
        self.driver = driver
        self.actions = BaseActions(driver)
        self._base_url = BASE_URL
        self._path = path.strip("/")
        self._url = f"{self._base_url.rstrip('/')}/{self._path}" if self._path else self._base_url

    def open(self) -> None:
        """Navigate to this page URL."""
        self.driver.get(self._url)

    @property
    def current_url(self) -> str:
        """Current browser URL."""
        return self.driver.current_url
